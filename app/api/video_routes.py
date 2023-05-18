from flask import Blueprint, request
from app.models import Video, User
from flask_login import current_user, login_required, current_user
from ..forms.video_form import NewVideo
from ..forms.edit_video_form import EditVideo
from ..models import db
from ..api.aws_video_helpers import get_unique_video_filename, upload_video_file_to_s3
from ..api.aws_image_helpers import get_unique_image_filename, upload_image_file_to_s3

video_routes = Blueprint('videos', __name__)

## ----------------------------------------  POST A VIDEO  ----------------------------------------
@video_routes.route('/new', methods=['POST'])
@login_required
def add_video():
    """Displays a new video drag and dropzone, allowing users to upload a video file"""

    form = NewVideo()
    form['csrf_token'].data = request.cookies['csrf_token']

    print("form.data inside New Video route ======>>", form.data)
    print("request.files ======>", request.files)

    if form.validate_on_submit():


        content = form.data['content']
        print("content inside New Video route ======>>", content)
        content.filename = get_unique_video_filename(content.filename)
        print("content.filename inside New Video route ======>>", content.filename)
        video_upload = upload_video_file_to_s3(content)
        print("video_upload inside New Video route ======>>", video_upload)

        thumbnail = form.data['thumbnail']
        print("thumbnail inside New Video route ======>>", thumbnail)
        thumbnail.filename = get_unique_image_filename(thumbnail.filename)
        print("thumbnail.filename inside New Video route ======>>", thumbnail.filename)
        thumbnail_upload = upload_image_file_to_s3(thumbnail)
        print("thumbnail_upload inside New Video route ======>>", thumbnail_upload)

        video = Video(user_id = current_user.id,
                      name = form.data['name'],
                      description = form.data['description'],
                      content = video_upload['url'],
                      thumbnail = thumbnail_upload['url'])

        db.session.add(video)
        db.session.commit()
        return video.to_dict()

    return { "errors": form.errors}


## ----------------------------------------  GET SINGLE VIDEO BY ID  ----------------------------------------
@video_routes.route('/<int:id>', methods=['GET'])
def get_single_video(id):
    """Displays the single video selected by the user"""

    video = Video.query.get(id)
    return video.to_dict()


## ----------------------------------------  GET ALL VIDEOS  ----------------------------------------
@video_routes.route('')
def get_all_videos():
    """Displays all videos"""

    videos = Video.query.all()
    return {'Videos': [video.to_dict() for video in videos]}


## ----------------------------------------  EDIT A VIDEO  ----------------------------------------
@video_routes.route('/<int:id>/edit', methods=['PUT'])
@login_required
def edit_video(id):
    """Allows the user to edit a video if the owner of the video is the logged in user"""

    video = Video.query.get(id)
    if not video:
        return {'error': 'video not found'}

    form = EditVideo()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        video.name = form.data['name']
        video.description = form.data['description']

        thumbnail = form.data['thumbnail']
        print("thumbnail inside Edit Video route ======>>", thumbnail)
        thumbnail.filename = get_unique_image_filename(thumbnail.filename)
        print("thumbnail.filename inside Edit Video route ======>>", thumbnail.filename)
        thumbnail_upload = upload_image_file_to_s3(thumbnail)
        print("thumbnail_upload inside Edit Video route ======>>", thumbnail_upload)

        video.thumbnail = thumbnail_upload['url']

        db.session.commit()
        return video.to_dict()

    return { "errors": form.errors}


## ----------------------------------------  DELETE A VIDEO  ----------------------------------------
@video_routes.route('/<int:id>/delete', methods=['DELETE'])
@login_required
def delete_video(id):
    """Allows the user to delete a video if the owner of the video is the logged in user"""

    video = Video.query.get(id)
    if video.user_id == current_user.id:
        db.session.delete(video)
        db.session.commit()
        return 'Delete Successful'
    else:
        return 'Must be video owner to delete video'
