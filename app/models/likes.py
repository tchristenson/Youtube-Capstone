from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.schema import ForeignKey


user_video_likes = db.Table(
    'video_likes',
    db.Model.metadata,
    db.Column('user_id', ForeignKey(add_prefix_for_prod('users.id')), primary_key=True),
    db.Column('video_id', ForeignKey(add_prefix_for_prod('videos.id')), primary_key=True)
)

if environment == "production":
    user_video_likes.schema = SCHEMA
