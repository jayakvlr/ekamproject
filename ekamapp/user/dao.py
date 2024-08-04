
import uuid
from ekamapp import db
from ekamapp.models import Event, User
from flask import abort,flash
from datetime import datetime

from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from ekamapp.utils import generate_referral_code

def get_user_by_id(user_id):
    try:
        user = db.session.get(User, user_id)
        if not user:
            abort(404, description="User not found")
        return user
    except Exception as e:
        abort(500, description=f"An error occurred: {str(e)}")



def get_event_by_code(eventcode):
    try:
        event = Event.query.filter_by(event_code=eventcode).first()
        if not event:
            abort(404, description="event not found")
        return event
    except Exception as e:
        abort(500, description=f"An error occurred: {str(e)}")

def get_upcoming_events(registered_event_ids):
    try:
        upcoming_events = Event.query.filter(
            Event.id.notin_(registered_event_ids),
            Event.event_datetime >= datetime.utcnow()
        ).all()
        return upcoming_events
    except Exception as e:
        raise Exception(f"An error occurred while fetching upcoming events: {str(e)}")
    


def save_user(user_obj, event):
    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            user = User()
            user.id = str(uuid.uuid4())
            user.events.append(event)
            user.referral_code = generate_referral_code(user_obj["name"].replace(" ", ""))
            user.set_user_data(user_data=user_obj)
            db.session.add(user)
            db.session.commit()
            return user
        except IntegrityError as e:
            db.session.rollback()
            if "unique constraint" in str(e).lower() and attempt < max_attempts - 1:
                # If it's a unique constraint violation (likely due to ID collision), try again
                continue
            else:
                # If it's another type of integrity error or we've exceeded max attempts, raise the exception
                raise
        except Exception as e:
            db.session.rollback()
            raise

    # If we've exhausted all attempts
    raise Exception("Failed to save user after multiple attempts due to ID collisions")