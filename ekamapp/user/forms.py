from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField,SelectField, SubmitField
from wtforms.validators import DataRequired,Length,length,Regexp
from ekamapp.constants import COUNTRY_CODES
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import DataRequired,Length,length
from ekamapp.constants import COUNTRIES,COUNTRY_CODES,STATES

#Form to accept the whatsapp number from user
class StartForm(FlaskForm):
    country_code = SelectField('Country Code',validate_choice=False, choices=COUNTRY_CODES,default='+91')
    whatsapp=StringField('Whatsapp Number',
                          validators=[DataRequired(),length(10,10)],render_kw={"placeholder": "Whatsapp"})
    submit=SubmitField('Start')


class RegistrationForm(FlaskForm):
    name = StringField('Full Name',
                       validators=[
                           DataRequired(),
                           Length(min=2, max=30),
                           Regexp('^[A-Za-z ]+$', message="Name must contain only letters and single spaces.")
                       ],
                       render_kw={"placeholder": "Full name"})

    country_code = SelectField('Country Code', validate_choice=False, choices=COUNTRY_CODES, default='+91')

    whatsapp = StringField('Whatsapp Number',
                           validators=[
                               DataRequired(),
                               Length(10, 10),
                               Regexp('^[0-9]+$', message="Whatsapp number must contain only digits.")
                           ],
                           render_kw={"placeholder": "Whatsapp"})

    gender = SelectField('Gender', validate_choice=False, choices=["Female", "Male", "Others"], validators=[DataRequired()])

    age = StringField('Age',
                      validators=[
                          DataRequired(),
                          Length(min=1, max=2),
                          Regexp('^[0-9]+$', message="Age must be a number.")
                      ],
                      render_kw={"placeholder": "Age"})

    country = SelectField('Country', validate_choice=False, choices=COUNTRIES, default='India')

    state = SelectField('State', validate_choice=False, validators=[DataRequired()], default='Kerala')

    place = StringField('Place',
                        validators=[DataRequired(), Length(min=2, max=20)],
                        render_kw={"placeholder": "District"})

    submit = SubmitField('Register')

"""#Form to accept Verification from whatsapp
class VerifyForm(FlaskForm):

    whatsappcode=StringField('whatsapp code',
                          validators=[DataRequired(),length(4,6)])
    submit=SubmitField('Verify')

    from flask_wtf import FlaskForm"""