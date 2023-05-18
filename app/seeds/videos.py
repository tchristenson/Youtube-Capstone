from app.models import db, Video, environment, SCHEMA
from sqlalchemy.sql import text

def seed_videos():
    video1 = Video(
        user_id = 1,
        name = 'video1',
        description = 'Here is a short description of video1',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/2ff58445a57f48b5958c6a4d0ead7b30.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/0989bf1bdca845cc8ea9c38bffc418e8.jpg'
    )
    video2 = Video(
        user_id = 2,
        name = 'video2',
        description = 'Here is a short description of video2',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/4ed0e3513d0249e68b28123668cb7876.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/4e5c22b440c6467f8ec703d1199a8d8c.jpg'
    )
    video3 = Video(
        user_id = 3,
        name = 'video3',
        description = 'Here is a short description of video3',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/52d90cf5b54648d891272b18d24a3302.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/5010eff36c194233959534dfb28bb82d.jpg	'
    )
    video4 = Video(
        user_id = 1,
        name = 'video4',
        description = 'Here is a short description of video4',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/afc40a78ccd54e3f82a46e8c0340956e.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/dc231d89ee874905b9236e037786ece1.jpg'
    )
    video5 = Video(
        user_id = 2,
        name = 'video5',
        description = 'Here is a short description of video5',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/c7b8756e40714a04bfa783a2cb3fd92a.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/f3354bf038784fba9ac76b48736f133b.jpg'
    )
    video6 = Video(
        user_id = 3,
        name = 'video6',
        description = 'Here is a short description of video6',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/f3a5f6d7adf64ba5b29c8a2b03af821d.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/fc24945cabc342cd93b1ee14e85fa0b2.jpg'
    )

    db.session.add(video1)
    db.session.add(video2)
    db.session.add(video3)
    db.session.add(video4)
    db.session.add(video5)
    db.session.add(video6)
    db.session.commit()


def undo_videos():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.videos RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM videos"))

    db.session.commit()
