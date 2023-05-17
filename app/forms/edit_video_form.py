from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, FileField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Video
from app.api.aws_image_helpers import ALLOWED_IMAGE_EXTENSIONS

class EditVideo(FlaskForm):
    # playlist_id = IntegerField("playlist_id", validate_choice=False) ## Placeholder until playlists implemented
    name = StringField('video_name', validators=[DataRequired()])
    description = StringField('video_description')
    thumbnail = FileField("thumbnail", validators=[FileRequired(), FileAllowed(list(ALLOWED_IMAGE_EXTENSIONS))])
