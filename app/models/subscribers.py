from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.schema import ForeignKey


subscribers = db.Table(
    'subscribers',
    db.Model.metadata,
    db.Column('followed_user_id', ForeignKey(add_prefix_for_prod('users.id')), primary_key=True),
    db.Column('following_user_id', ForeignKey(add_prefix_for_prod('users.id')), primary_key=True)
)

if environment == "production":
    subscribers.schema = SCHEMA
