from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='username')
    password= PasswordField(label='password')
    confirmation = PasswordField(label='confirmation')
    Register = SubmitField(label='Register')
