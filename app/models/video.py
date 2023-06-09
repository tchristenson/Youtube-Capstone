from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.schema import ForeignKey
from sqlalchemy import func
from .likes import user_video_likes
from .playlist_video import playlist_video

class Video(db.Model):
    __tablename__ = 'videos'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(500))
    content = db.Column(db.String, nullable=False)
    thumbnail = db.Column(db.String, nullable=False) ## Will be required for now, can possibly select frames from the video and make it automatic
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    user = db.relationship('User', back_populates='videos')

    comments = db.relationship('Comment', back_populates='video', cascade='all, delete-orphan')

    user_likes = db.relationship('User', secondary=user_video_likes, back_populates='video_likes')
    playlists = db.relationship('Playlist', secondary=playlist_video, back_populates='videos')

    def to_dict(self):
        user_likes = [user.to_dict() for user in self.user_likes]
        playlists = [playlist.to_dict() for playlist in self.playlists]
        return {
            'id': self.id,
            'userId': self.user_id,
            'name': self.name,
            'description': self.description,
            'content': self.content,
            'thumbnail': self.thumbnail,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
            'userLikes': user_likes,
            'playlists': playlists,
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
