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
