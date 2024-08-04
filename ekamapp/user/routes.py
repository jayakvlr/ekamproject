import time
from flask import jsonify, render_template,url_for,flash,redirect,request,make_response,session,Blueprint, current_app as app
from ekamapp.user.dao import get_event_by_code, get_user_by_id,save_user
from ekamapp.user.forms import RegistrationForm, StartForm
from ekamapp.models import  User
from ekamapp.utils import check_login_status, generate_qr_code, generate_qr_code_response, generate_unique_referral_link,parse_event_datetime,login_required,get_user_object
from ekamapp.wati_utils import send_ticket, send_verification_message


users = Blueprint('users', __name__)

WEBHOOK_TRIGGERED = False

@users.route('/webhook/transaction', methods=['POST'])
def transaction_webhook():
    global WEBHOOK_TRIGGERED
    data = request.json
    app.logger.info(f"Received webhook data: {data}")

    if data.get('eventType') == 'sentMessageREPLIED':
        WEBHOOK_TRIGGERED = True
        app.logger.info("Webhook triggered successfully")
        return jsonify({'status': 'success'}), 200
    else:
        app.logger.warning("Invalid webhook event type")
        return jsonify({'status': 'failure'}), 400

@users.route('/<string:event_code>', methods=['GET', 'POST'])
def register(event_code):
    app.logger.info(f"Registration attempt for event code: {event_code}")
    if check_login_status():
        app.logger.info("User already logged in. Redirecting to dashboard.")
        return redirect(url_for('users.dashboard'))
    
    global WEBHOOK_TRIGGERED
    referrer = request.args.get('referrer') or request.form.get('referrer')
    if referrer:
        session['referrer'] = referrer
    else:
        referrer = session.get('referrer')
    
    event = get_event_by_code(event_code)
    event_d = parse_event_datetime(event)
    form = RegistrationForm()
    
    if form.validate_on_submit():
        app.logger.info(f"Form submitted for user: {form.name.data}")
        user_data = get_user_object(form, referrer)
        app.logger.debug(f"User data: {user_data}")
        
        try:
            phone = user_data['country_code'] + user_data['whatsapp']
            user = User.query.filter_by(whatsapp=phone).first()

            if user:
                app.logger.info(f"WhatsApp number already registered: {phone}")
                flash('This WhatsApp number is already registered. Please log in.', 'info')
                return redirect(url_for('users.login', event_code=event_code))
            
            response = send_verification_message(phone, user_data['name'])

            if response == 200:
                app.logger.info(f"Verification message sent successfully to: {phone}")
                WEBHOOK_TRIGGERED = False
                start_time = time.time()

                while True:
                    if WEBHOOK_TRIGGERED:
                        user = save_user(user_data, event)
                        app.logger.info(f"User saved successfully: {user.id}")
                        QRcode = generate_qr_code(user, event)
                        send_ticket(user.name, user.whatsapp, event)
                        flash("Your ticket has been sent to your WhatsApp. Please check")
                        response = make_response(redirect(url_for('users.dashboard')))
                        response.set_cookie('user_id', str(user.id))
                        response.set_cookie('user_name', user.name)
                        response.set_cookie('event_code', event.event_code)
                        session['phone'] = phone
                        flash(f'Congrats, {form.name.data}! You are now registered for Ekam E2!', 'success')
                        flash("Ticket details have been sent to your registered WhatsApp. Please check your WhatsApp.")
                        return response

                    if time.time() - start_time >= 120:
                        app.logger.warning(f"Webhook timeout for user: {user_data['name']}")
                        flash("You haven't responded to our WhatsApp verification. Please try again.", 'danger')
                        return redirect(url_for('users.register', event_code=event_code))

                    time.sleep(1)

            else:
                app.logger.error(f"WhatsApp authentication failed for: {phone}")
                flash("Your WhatsApp authentication has failed. Please try again.", 'danger')
                return render_template('registration_index.html', event=event_d, form=form, title='Register')

        except ValueError as ve:
            app.logger.error(f"ValueError during registration: {str(ve)}")
            flash(str(ve), 'danger')
        except Exception as e:
            app.logger.exception(f"Unexpected error during registration: {str(e)}")
            flash("An error occurred during registration. Please try again later.", 'danger')

    return render_template('registration_index.html', event=event_d, form=form, title='Register')

@login_required
@users.route("/dashboard", methods=['GET', 'POST'])
def dashboard():

    event_obj=parse_event_datetime(get_event_by_code(request.cookies.get('event_code')))
    if request.cookies.get('user_id'):
        
        user_info=get_user_by_id(request.cookies.get('user_id'))
        referral_link=generate_unique_referral_link(user_info,user_info.events[0])
        if user_info:
            registered_event = user_info.events[0]  # Get all events the user has registered for
            event_qr_code =  generate_qr_code_response(user_info, registered_event)
        else:
            registered_event = None
            event_qr_code = None
                # Fetch upcoming events
        
            # Get IDs of registered events
        #registered_event_ids = [event.id for event in registered_events]

            # Query upcoming events excluding already registered ones
        #upcoming_events = get_upcoming_events(registered_event_ids)
        #print(registered_events)
        return render_template('dashboard.html',user=user_info,event= parse_event_datetime(user_info.events[0]),event_qr_code=event_qr_code,referral_link=referral_link,cookies=True)
    else:
        form =RegistrationForm()

        return render_template('registration_index.html',event=event_obj, form=form, title='Register',cookies=False)
    



@users.route("/logout", methods=['GET', 'POST'])
def logout():
    event_obj=parse_event_datetime(get_event_by_code(request.cookies.get('event_code')))   
    response = make_response(redirect(url_for('users.login',event_code=event_obj["event_code"])))
    response.set_cookie('user_id', '', expires=0)
    response.set_cookie('user_name', '', expires=0)
    response.set_cookie('event_code', '', expires=0)

        # Add headers to prevent caching
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    session.clear()
    return response

@users.route("/login/<string:event_code>", methods=['GET', 'POST'])
def login(event_code):
    global WEBHOOK_TRIGGERED
    event=get_event_by_code(event_code)
    event_d=parse_event_datetime(event)
    form =StartForm()
    if form.validate_on_submit():
 
            user_data = {
  
                "country_code":form.country_code.data,
                "whatsapp": form.whatsapp.data,
            }
 
            phone=user_data['country_code'][1:]+user_data['whatsapp']
            user = User.query.filter_by(whatsapp=phone).first()
            if user:
                response = send_verification_message(phone, user.name)
                if response == 200:
                    WEBHOOK_TRIGGERED = False
                    session['phone'] = phone
                    start_time = time.time()
                    
                    while True:
                        if WEBHOOK_TRIGGERED:
                            response = make_response(redirect(url_for('users.dashboard')))
                            response.set_cookie('user_id', str(user.id))
                            response.set_cookie('user_name', user.name)
                            response.set_cookie('event_code', event.event_code)
                            return response

                        # Check if 2 minutes have passed
                        if time.time() - start_time >= 120:  # 2 minutes in seconds
                            flash("You haven't responded to our WhatsApp verification. Please try again.", 'danger')
                            return redirect(url_for('users.register', event_code=event_code))

                        time.sleep(1)  # Sleep for 1 second before checking again

                else:
                    flash("Your WhatsApp authentication has failed. Please try again.", 'danger')
                    return render_template('registration_index.html', event=event_d, form=form, title='Register')



    return render_template('lgn_index.html',form=form,event=event_d)

