from flask import Blueprint, request
from app.models import Video, Playlist
from flask_login import current_user, login_required, current_user
from ..models import db
from ..forms.playlist_form import NewPlaylist


playlist_routes = Blueprint('playlists', __name__)

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


## ----------------------------------------  GET ALL PLAYLISTS  ----------------------------------------
@playlist_routes.route('')
def get_all_playlists():
    """Displays all playlists"""

    playlists = Playlist.query.all()
    return {'Playlists': [playlist.to_dict() for playlist in playlists]}
