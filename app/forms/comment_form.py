from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class NewComment(FlaskForm):
    content = StringField('content', validators=[DataRequired()])
    video_id = IntegerField('video_id', validators=[DataRequired()])
