from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.schema import ForeignKey
from sqlalchemy import func
from .playlist_video import playlist_video

class Playlist(db.Model):
    __tablename__ = 'playlists'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    user = db.relationship('User', back_populates='playlists')

    videos = db.relationship('Video', secondary=playlist_video, back_populates='playlists')

    def to_dict(self):
        # videos = [video.id for video in self.videos]

        return {
            'id': self.id,
            'userId': self.user_id,
            'name': self.name,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
            # 'videoIds': videos
        }
