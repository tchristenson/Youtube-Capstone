from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.schema import ForeignKey


user_video_likes = db.Table(
    'video_likes',
    db.Model.metadata,
    db.Column('user_id', ForeignKey('users.id'), primary_key=True),
    db.Column('video_id', ForeignKey('videos.id'), primary_key=True)
)
