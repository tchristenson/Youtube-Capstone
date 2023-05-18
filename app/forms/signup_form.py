from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, FileField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User
from app.api.aws_image_helpers import ALLOWED_IMAGE_EXTENSIONS


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError('Email address is already in use.')


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')

def valid_email(form, field):
# Checking if username is already in use
    email = field.data
    email_error = '@' not in email
    if email_error:
        raise ValidationError('Email is not valid.')


class SignUpForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), username_exists])
    password = StringField('password', validators=[DataRequired()])
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), user_exists, valid_email])
    about = StringField('about')
    profile_picture = FileField("profile_picture", validators=[FileAllowed(list(ALLOWED_IMAGE_EXTENSIONS))])
