from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, FileField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import Video
from app.api.aws_video_helpers import ALLOWED_VIDEO_EXTENSIONS
from app.api.aws_image_helpers import ALLOWED_IMAGE_EXTENSIONS

class NewVideo(FlaskForm):
    # playlist_id = IntegerField("playlist_id", validate_choice=False) ## Placeholder until playlists implemented
    name = StringField('song_name', validators=[DataRequired()])
    content = FileField("content", validators=[FileRequired(), FileAllowed(list(ALLOWED_VIDEO_EXTENSIONS))])
    thumbnail = FileField("thumbnail", validators=[FileRequired(), FileAllowed(list(ALLOWED_IMAGE_EXTENSIONS))])
