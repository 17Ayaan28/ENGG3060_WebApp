from curses import ACS_GEQUAL
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class admin_LoginForm(FlaskForm):
    id = StringField('ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class create_patient(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    sex = StringField('Sex', validators=[DataRequired()])
    clinician_id = StringField('Clinician ID', validators=[DataRequired()])

class create_clinician(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])