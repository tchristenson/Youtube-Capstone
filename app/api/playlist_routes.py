from flask import Blueprint, request
from app.models import Video, Playlist
from flask_login import current_user, login_required, current_user
from ..models import db
from ..forms.playlist_form import NewPlaylist


playlist_routes = Blueprint('playlists', __name__)

# ## ----------------------------------------  CREATE A PLAYLIST  ----------------------------------------
# @playlist_routes.route('/new', methods=['POST'])
# @login_required
# def create_playlist(data, video_id):
#     """Allows a logged in user to create a playlist"""
#     print('data ========>>>>>>>>', data)
#     print('video_id ========>>>>>>>>', video_id)

#     form = NewPlaylist()
#     form['csrf_token'].data = request.cookies['csrf_token']
#     print('form.data before validation ========>>>>>>>>', form.data)

#     if form.validate_on_submit():
#         print('form.data after validation ========>>>>>>>>', form.data)

#         playlist = Playlist(
#             user_id = current_user.id,
#             name = form.data['name']
#         )

#         db.session.add(playlist)
#         db.session.commit()
#         print('playlist ========>>>>>>>>', playlist.to_dict())
#         print('form.data[video_id] ========>>>>>>>>', form.data['video_id'])

#         video = Video.query.get(form.data['video_id'])
#         if not video:
#             return {'error': 'video not found'}

#         print('video ========>>>>>>>>', video.to_dict())


#         return playlist.to_dict()

#     return { "errors": form.errors }


## ----------------------------------------  GET PLAYLIST VIDEO BY ID  ----------------------------------------
@playlist_routes.route('/<int:id>', methods=['GET'])
def get_single_playlist(id):
    """Retrieves a single playlist specified by ID"""

    playlist = Playlist.query.get(id)
    return playlist.to_dict()


## ----------------------------------------  EDIT PLAYLIST  ----------------------------------------
@playlist_routes.route('/<int:id>/edit', methods=['PUT'])
@login_required
def edit_playlist(id):
    """Allows the user to edit a playlist if the owner of the playlist is the logged in user"""

    playlist = Playlist.query.get(id)
    if not playlist:
        return {'error': 'playlist not found'}

    form = NewPlaylist()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        playlist.name = form.data['name']

        db.session.commit()
        return playlist.to_dict()

    return { 'errors': form.errors }

## ----------------------------------------  DELETE A PLAYLIST  ----------------------------------------
@playlist_routes.route('/<int:id>/delete', methods=['DELETE'])
@login_required
def delete_playlist(id):
    """Allows the user to delete a playlist if the owner of the playlist is the logged in user"""

    playlist = Playlist.query.get(id)
    if playlist.user_id == current_user.id:
        db.session.delete(playlist)
        db.session.commit()
        return 'Delete Successful'
    else:
        return 'Must be playlist owner to delete playlist'
