from flask import Blueprint, request
from app.models import Video, Playlist
from flask_login import current_user, login_required, current_user
from ..models import db
from ..forms.playlist_form import NewPlaylist


playlist_routes = Blueprint('playlists', __name__)

## ----------------------------------------  CREATE A PLAYLIST  ----------------------------------------
@playlist_routes.route('/new', methods=['POST'])
@login_required
def create_playlist(video_id):
    """Allows a logged in user to create a playlist"""

    video = Video.query.get(video_id)
    if not video:
        return {'error': 'video not found'}

    form = NewPlaylist()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():

        playlist = Playlist(
            user_id = current_user.id,
            name = form.data['name']
        )

        db.session.add(playlist)
        db.session.commit()
        print('playlist ========>>>>>>>>', playlist)
        return playlist.to_dict()

    return { "errors": form.errors }
