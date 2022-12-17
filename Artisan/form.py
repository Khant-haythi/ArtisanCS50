from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,DateField,TextAreaField
from wtforms.validators import Length,EqualTo,DataRequired
from flask_wtf.file import FileField,FileAllowed

class RegisterForm(FlaskForm):
    username = StringField(label='username',validators=[Length(min=2,max=30),DataRequired()])
    password= PasswordField(label='password',validators=[Length(min=6),DataRequired()])
    confirmation = PasswordField(label='confirmation',validators=[EqualTo('password'),DataRequired()])
    Register = SubmitField(label='Register')

class LoginForm(FlaskForm):
    username = StringField(label='username',validators=[DataRequired()])
    password= PasswordField(label='password',validators=[DataRequired()])
    login = SubmitField(label='Log In')


class BlogPostForm(FlaskForm):
    title = StringField(label='title',validators=[DataRequired()])
    content = TextAreaField(label='content',validators=[DataRequired()])
    author = StringField(label='author',validators=[DataRequired()])
    created_date = DateField(label='created_dae',validators=[DataRequired()])
    image = StringField (label='image')
    create = SubmitField(label='Create Post')