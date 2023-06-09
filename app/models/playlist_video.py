from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.schema import ForeignKey


playlist_video = db.Table(
    'playlist_video',
    db.Model.metadata,
    db.Column('playlist_id', ForeignKey(add_prefix_for_prod('playlists.id')), primary_key=True),
    db.Column('video_id', ForeignKey(add_prefix_for_prod('videos.id')), primary_key=True)
)

if environment == "production":
    playlist_video.schema = SCHEMA
