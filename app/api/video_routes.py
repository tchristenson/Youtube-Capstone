from flask import Blueprint, request
from app.models import Video, User
from flask_login import current_user, login_required, current_user
from ..forms.video_form import NewVideo
from ..models import db
from ..api.aws_video_helpers import get_unique_video_filename, upload_video_file_to_s3
from ..api.aws_image_helpers import get_unique_image_filename, upload_image_file_to_s3

video_routes = Blueprint('videos', __name__)

@video_routes.route('/new')
@login_required
def add_video():
    """Displays a new video drag and dropzone, allowing users to upload a video file"""

    form = NewVideo()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
