import base64
from flask import url_for,send_file
import pyqrcode
import io
from flask import request
from functools import wraps
from flask import session, redirect, url_for
import random
import string

def check_login_status():
    if request.cookies.get('event_code') and request.cookies.get('event_code') and request.cookies.get('event_code'):
        return True
    else:
        return False
    
def parse_datetime(dt):
    # Format the date as "Date Month Year"
    date_string = dt.strftime("%d %B %Y")
    
    # Format the time as "HH:MM:SS"
    time_string = dt.strftime("%H:%M:%S")
    
    return date_string, time_string
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'phone' not in session:
            return redirect(url_for('users.login'))
        return f(*args, **kwargs)
    return decorated_function

def parse_event_datetime(event):
    return {
        'event_code':event.event_code,
        'name':event.name,
        'date': event.event_datetime.strftime('%d'),
        'month': event.event_datetime.strftime('%B'),  # Full month name
        'year': event.event_datetime.strftime('%Y'),
        'location':event.event_location,
        'place':event.event_place
    }

def generate_qr_code(data,event):
    data = data.id+'-'+str(event.id)
    qr = pyqrcode.create(data)  
    # Convert the QR code to a PNG image in memory
    img_byte_arr = io.BytesIO()
    qr.png(img_byte_arr, scale=6)
    img_byte_arr.seek(0)
    return img_byte_arr

def generate_qr_code_response(user_info,event):
    
    img_byte_arr = generate_qr_code(user_info,event)
    img_base64 = base64.b64encode(img_byte_arr.getvalue()).decode('ascii')
    return img_base64



def remove_all_whitespace(s):
    return s.replace(" ", "")

from ekamapp.models import RoleEnum
def get_user_object(form,referral_code):
        return  {
            "name": form.name.data,
            "country_code":form.country_code.data[1:],
            "whatsapp": form.whatsapp.data,
            "gender": form.gender.data,
            "age": form.age.data,
            "country": form.country.data,
            "state": form.state.data,
            "place": form.place.data,
            "referral_code": referral_code,
            "role":RoleEnum.USER
        }

def generate_random_code(length=4):
    characters = string.ascii_letters + string.digits
    random_code = ''.join(random.choice(characters) for _ in range(length))
    return random_code

def generate_referral_code(name):
    # Normalize the inputs

    name = name.strip().lower()
    rnd_string=generate_random_code()
    
    
    # Concatenate the inputs with a separator
    referral_code = f"{name}-{rnd_string}"
  
    return referral_code


def generate_unique_referral_link(user,event):

    referral_link = url_for('users.register',referrer=user.referral_code, event_code=event.event_code, _external=True)
    return referral_link


