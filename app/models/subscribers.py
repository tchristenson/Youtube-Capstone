# from .db import db, environment, SCHEMA, add_prefix_for_prod
# from sqlalchemy.schema import ForeignKey


# subscribers = db.Table(
#     'video_likes',
#     db.Model.metadata,
#     db.Column('user_id', ForeignKey(add_prefix_for_prod('users.id')), primary_key=True),
#     db.Column('video_id', ForeignKey(add_prefix_for_prod('videos.id')), primary_key=True)
# )
