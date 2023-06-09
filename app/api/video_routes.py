from flask import Blueprint, request
from app.models import Video, User, Playlist
from flask_login import current_user, login_required, current_user
from ..forms.video_form import NewVideo
from ..forms.edit_video_form import EditVideo
from ..forms.playlist_form import NewPlaylist
from ..models import db
from ..api.aws_video_helpers import get_unique_video_filename, upload_video_file_to_s3
from ..api.aws_image_helpers import get_unique_image_filename, upload_image_file_to_s3
from ..models.likes import user_video_likes
from ..models.playlist_video import playlist_video
from sqlalchemy import select

video_routes = Blueprint('videos', __name__)

## ----------------------------------------  POST A VIDEO  ----------------------------------------
@video_routes.route('/new', methods=['POST'])
@login_required
def add_video():
    """Displays a new video drag and dropzone, allowing users to upload a video file"""

    form = NewVideo()
    form['csrf_token'].data = request.cookies['csrf_token']

    # print("form.data inside New Video route ======>>", form.data)
    # print("request.files ======>", request.files)

    if form.validate_on_submit():


        content = form.data['content']
        # print("content inside New Video route ======>>", content)
        content.filename = get_unique_video_filename(content.filename)
        # print("content.filename inside New Video route ======>>", content.filename)
        video_upload = upload_video_file_to_s3(content)
        # print("video_upload inside New Video route ======>>", video_upload)

        thumbnail = form.data['thumbnail']
        # print("thumbnail inside New Video route ======>>", thumbnail)
        thumbnail.filename = get_unique_image_filename(thumbnail.filename)
        # print("thumbnail.filename inside New Video route ======>>", thumbnail.filename)
        thumbnail_upload = upload_image_file_to_s3(thumbnail)
        # print("thumbnail_upload inside New Video route ======>>", thumbnail_upload)

        video = Video(user_id = current_user.id,
                      name = form.data['name'],
                      description = form.data['description'],
                      content = video_upload['url'],
                      thumbnail = thumbnail_upload['url'])

        db.session.add(video)
        db.session.commit()
        return video.to_dict()

    return { "errors": form.errors }


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

    videos = Video.query.join(User, Video.user_id == User.id).all()
    videos_check = [video.to_dict() for video in videos]
    # print('videos_check ===========>>>>>>>>>>>', videos_check)
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
        # print("thumbnail inside Edit Video route ======>>", thumbnail)
        thumbnail.filename = get_unique_image_filename(thumbnail.filename)
        # print("thumbnail.filename inside Edit Video route ======>>", thumbnail.filename)
        thumbnail_upload = upload_image_file_to_s3(thumbnail)
        # print("thumbnail_upload inside Edit Video route ======>>", thumbnail_upload)

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


## ----------------------------------------  LIKE OR UNLIKE A VIDEO  ----------------------------------------
@video_routes.route('/<int:id>/likes/<int:user_id>', methods=['POST'])
@login_required
def like_video(id, user_id):
    """Queries for a video and user, and adds the user's like to that video if they have not liked the video.
        Otherwise, the like is removed if the user has already liked the video"""

    video = Video.query.get(id)
    if not video:
        return {'error': 'video not found'}

    user = User.query.get(user_id)
    if not user:
        return {'error': 'user not found'}

    # print('id =============>>>>>>>>>>>>>>', id)
    # print('user_id =============>>>>>>>>>>>>>>', user_id)
    # print('video =============>>>>>>>>>>>>>>', video)
    # print('user =============>>>>>>>>>>>>>>', user)

    query = select([user_video_likes]).where(
        (user_video_likes.c.user_id == user_id) & (user_video_likes.c.video_id == id)
    )

    result = db.session.execute(query)
    print('result =============>>>>>>>>>>>>>>', result)

    has_liked = result.fetchone() is not None
    print('has_liked =============>>>>>>>>>>>>>>', has_liked)

    if has_liked:
        video.user_likes.remove(user)
        db.session.commit()
        return video.to_dict()
    else:
        video.user_likes.append(user)
        db.session.commit()
        return video.to_dict()


## ----------------------------------------  ADD OR REMOVE FROM PLAYLIST  ----------------------------------------
@video_routes.route('/<int:video_id>/playlists/<int:playlist_id>', methods=['POST'])
@login_required
def add_remove_from_playlist(video_id, playlist_id):
    """Queries for a video and playlist, and adds the video to the playlist if it is not already included.
    Otherwise, the video is removed if the playlist already includes the video"""

    video = Video.query.get(video_id)
    if not video:
        return {'error': 'video not found'}

    playlist = Playlist.query.get(playlist_id)
    if not playlist:
        return {'error': 'playlist not found'}

    query = select([playlist_video]).where(
        (playlist_video.c.video_id == video_id) & (playlist_video.c.playlist_id == playlist_id)
    )

    result = db.session.execute(query)
    print('result =============>>>>>>>>>>>>>>', result)

    video_included = result.fetchone() is not None
    print('video_included =============>>>>>>>>>>>>>>', video_included)

    if video_included:
        playlist.videos.remove(video)
        db.session.commit()
        return playlist.to_dict()
    else:
        playlist.videos.append(video)
        db.session.commit()
        return playlist.to_dict()



## ----------------------------------------  CREATE A PLAYLIST  ----------------------------------------
@video_routes.route('/<int:id>/playlists/new', methods=['POST'])
@login_required
def create_playlist(id):
    """Allows a logged in user to create a playlist"""

    form = NewPlaylist()
    form['csrf_token'].data = request.cookies['csrf_token']
    print('form.data ========>>>>>>>>', form.data)

    video = Video.query.get(id)
    if not video:
        return {'error': 'video not found'}

    print('video ========>>>>>>>>', video.to_dict())


    if form.validate_on_submit():

        playlist = Playlist(
            user_id = current_user.id,
            name = form.data['name']
        )

        db.session.add(playlist)
        db.session.commit()
        print('playlist ========>>>>>>>>', playlist.to_dict())

        video.playlists.append(playlist)

        # db.session.execute(playlist_video.insert().values(playlist_id=playlist.id, video_id=video.id))
        db.session.commit()

        return playlist.to_dict()

    return { "errors": form.errors }
