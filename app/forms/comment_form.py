from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from app.models import Comment

class NewComment(FlaskForm):
    content = StringField('content', validators=[DataRequired()])
    video_id = IntegerField('video_id', validators=[DataRequired()])
