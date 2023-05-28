from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.schema import ForeignKey
from sqlalchemy import func

class Video(db.Model):
    __tablename__ = 'videos'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    # playlist_id = db.Column(db.Integer, ForeignKey(add_prefix_for_prod('playlists.id')), nullable=True) ## Placeholder until playlists implemented
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(500))
    content = db.Column(db.String, nullable=False)
    thumbnail = db.Column(db.String, nullable=False) ## Will be required for now, can possibly select frames from the video and make it automatic
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    user = db.relationship('User', back_populates='videos')

    comments = db.relationship('Comment', back_populates='video', cascade='all, delete-orphan')


    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.user_id,
            #   'playlistId': self.playlist_id, ## Placeholder until playlists implemented
            'name': self.name,
            'description': self.description,
            'content': self.content,
            'thumbnail': self.thumbnail,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
            'user': {
                'id': self.user.id,
                'username': self.user.username,
                'firstName': self.user.first_name,
                'lastName': self.user.last_name,
                'email': self.user.email,
                'about': self.user.about,
                'profilePicture': self.user.profile_picture
            }
      }
