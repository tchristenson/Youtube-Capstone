from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from .likes import user_video_likes
from .subscribers import subscribers


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    about = db.Column(db.String(500))
    profile_picture = db.Column(db.String)

    videos = db.relationship('Video', back_populates='user', cascade='all, delete-orphan')
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete-orphan')
    playlists = db.relationship('Playlist', back_populates='user', cascade='all, delete-orphan')

    video_likes = db.relationship('Video', secondary=user_video_likes, back_populates='user_likes')

    subscribed = db.relationship('User',
        secondary=subscribers,
        primaryjoin=(subscribers.c.following_user_id == id),
        secondaryjoin=(subscribers.c.followed_user_id == id),
        back_populates='subscribers'
        )

    subscribers = db.relationship('User',
        secondary=subscribers,
        primaryjoin=(subscribers.c.followed_user_id == id),
        secondaryjoin=(subscribers.c.following_user_id == id),
        back_populates='subscribed'
        )

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        # print('self.subscribed ==========>>>>>>>>>', self.subscribed)
        # print('self.subscribers ==========>>>>>>>>>', self.subscribers)
        subscribed_ids = [user.id for user in self.subscribed]
        subscribing_ids = [user.id for user in self.subscribers]
        playlists = [playlist.to_dict() for playlist in self.playlists]

        return {
            'id': self.id,
            'username': self.username,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'email': self.email,
            'about': self.about,
            'profilePicture': self.profile_picture,
            'subscribedIds': subscribed_ids,
            'subscribersIds': subscribing_ids,
            'playlists': playlists
        }
