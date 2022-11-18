from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField("Log In")

class admin_LoginForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class create_patient(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    age = StringField('Age', validators=[DataRequired()])
    sex = StringField('Sex', validators=[DataRequired()])
    condition = StringField('Condition', validators=[])
    affected_hand = StringField('Affected Hand', validators=[])
    dominant_hand = StringField('Dominant Hand', validators=[])
    clinician_id = StringField('Clinician ID', validators=[DataRequired()])
    submit = SubmitField("Add New Patient")

class create_clinician(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Add New Clinician')