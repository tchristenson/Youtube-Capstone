from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField
from wtforms.validators import DataRequired
from app.models import Comment

class NewComment(FlaskForm):
    content = StringField('content', validators=[DataRequired()])
