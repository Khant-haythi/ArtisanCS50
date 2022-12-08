from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label='username',validators=[Length(min=2,max=30),DataRequired()])
    password= PasswordField(label='password',validators=[Length(min=6),DataRequired()])
    confirmation = PasswordField(label='confirmation',validators=[EqualTo('password'),DataRequired()])
    Register = SubmitField(label='Register')

class LoginForm(FlaskForm):
    username = StringField(label='username',validators=[DataRequired()])
    password= PasswordField(label='password',validators=[DataRequired()])
    login = SubmitField(label='Log In')