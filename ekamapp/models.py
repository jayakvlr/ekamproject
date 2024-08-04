
from datetime import datetime
from ekamapp import db
import uuid

from enum import Enum
from ekamapp import db
import uuid
from sqlalchemy import Enum as SQLAlchemyEnum,DateTime

class AttendanceStatus(Enum):
    REGISTERED = 'registered'
    ATTENDED = 'attended'
    ABSENT = 'absent'

class RoleEnum(Enum):
    USER = 'user'
    ADMIN = 'admin'

class TicketTypeEnum(Enum):
    REGULAR='regular'
    VIP='vip'

user_event = db.Table('user_event',
    db.Column('user_id', db.String(20), db.ForeignKey('user.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
    db.Column('registered_time', DateTime, default=datetime.utcnow, nullable=False),
    db.Column('attendance_time', DateTime, nullable=True),
    db.Column('status', SQLAlchemyEnum(AttendanceStatus), nullable=False, default=AttendanceStatus.REGISTERED)
)

class User(db.Model):

    id=db.Column(db.String(20),primary_key=True,nullable=False,default=str(uuid.uuid4()))
    name=db.Column(db.String(20),nullable=False)
    whatsapp=db.Column(db.String(20),unique=True,nullable=False)
    gender=db.Column(db.String(10),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    country=db.Column(db.String(10),nullable=False)
    state=db.Column(db.String(10),nullable=False)
    place=db.Column(db.String(10),nullable=False)
    referral_code=db.Column(db.String(100),nullable=False)
    referred_by = db.Column(db.String(20), nullable=True)
    role = db.Column(SQLAlchemyEnum(RoleEnum), nullable=False, default=RoleEnum.USER) # Role, with limited choices, required
    events = db.relationship('Event', secondary=user_event, back_populates='users')


    def set_user_data(self, user_data):
        """
        Sets user data from a dictionary.

        Args:
            user_data (dict): A dictionary containing user information.

        Raises:
            ValueError: If required keys are missing from the user_data dictionary.
        """

        # Check for required keys
        required_keys = {"name", "whatsapp", "gender", "age", "country", "state", "place"}
        missing_keys = required_keys - set(user_data.keys())
        if missing_keys:
            raise ValueError(f"Missing required keys: {', '.join(missing_keys)}")
        self.name = user_data["name"]
        self.whatsapp =(user_data["country_code"]+user_data["whatsapp"]).replace(" ", "")
        self.gender = user_data["gender"]
        self.age = user_data["age"]
        self.country = user_data["country"]
        self.state = user_data["state"]
        self.place = user_data["place"]
        self.referred_by = user_data["referral_code"]
        
        self.role=user_data["role"]

    def __repr__(self):
        return f"User({self.id}','{self.name})"
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'whatsapp': self.whatsapp,
            'gender': self.gender,
            'age': self.age,
            'country': self.country,
            'state': self.state,
            'place': self.place,
            'referred_by': self.referred_by,
        }
    


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_code = db.Column(db.String(10),unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(SQLAlchemyEnum(TicketTypeEnum), nullable=False, default=TicketTypeEnum.REGULAR) # Role, with limited choices, required
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    event_datetime=db.Column(db.DateTime, nullable=False)
    event_location=db.Column(db.Text, nullable=False)
    event_place=db.Column(db.Text, nullable=False)
    users = db.relationship('User', secondary=user_event, back_populates='events')
    #event_image = db.Column(db.LargeBinary, nullable=True) 

    def __repr__(self):
        return f"Post('{self.name}', '{self.date_posted}')"
    
class VerifyEnum(Enum):
    INTIATED = 'intiated'
    VERIFIED = 'verified'



class VerificationAttempt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(5), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    verification_status = db.Column(SQLAlchemyEnum(VerifyEnum), nullable=False, default=VerifyEnum.INTIATED)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<VerificationAttempt {self.code+self.phone} - {self.verification_status}>"

