from app.models import db, Comment, environment, SCHEMA
from sqlalchemy.sql import text

def seed_comments():
    comment1 = Comment(
        user_id = 1,
        video_id = 2,
        content = "Who else is watching this at 3 a.m. instead of getting some sleep?"
    )
    comment2 = Comment(
        user_id = 2,
        video_id = 3,
        content = "I can't believe how time flies! Feels like just yesterday this video came out."
    )
    comment3 = Comment(
        user_id = 3,
        video_id = 4,
        content = "This video is so entertaining, it made my day!"
    )
    comment4 = Comment(
        user_id = 1,
        video_id = 5,
        content = "Can we take a moment to appreciate the editing skills in this video? Amazing!"
    )
    comment5 = Comment(
        user_id = 2,
        video_id = 6,
        content = "The comment section is always the best part. Let the scrolling begin!"
    )
    comment6 = Comment(
        user_id = 3,
        video_id = 1,
        content = "I've watched this video five times already, and it's still hilarious!"
    )
    comment7 = Comment(
        user_id = 1,
        video_id = 2,
        content = "Is it just me, or does the background music give this video an epic vibe?"
    )
    comment8 = Comment(
        user_id = 2,
        video_id = 3,
        content = "Please bless us with more videos like this. The world can't have enough, really."
    )
    comment9 = Comment(
        user_id = 3,
        video_id = 4,
        content = "Hold on, let me pause this video so I can appreciate the sheer mediocrity of it all."
    )
    comment10 = Comment(
        user_id = 1,
        video_id = 5,
        content = "This video is so entertaining, it makes me want to take a nap."
    )
    comment11 = Comment(
        user_id = 2,
        video_id = 6,
        content = "The comment section is always filled with enlightening conversations. Can't wait!"
    )
    comment12 = Comment(
        user_id = 3,
        video_id = 1,
        content = "I'm so grateful that this video can read my mind and deliver the most generic content imaginable."
    )
    comment13 = Comment(
        user_id = 1,
        video_id = 2,
        content = "This video is the perfect cure for a boring Sunday afternoon."
    )
    comment14 = Comment(
        user_id = 2,
        video_id = 3,
        content = "I can't believe how relatable this content is. You read my mind!"
    )
    comment15 = Comment(
        user_id = 3,
        video_id = 4,
        content = "I can't stop laughing at that unexpected plot twist. Genius!"
    )

    db.session.add(comment1)
    db.session.add(comment2)
    db.session.add(comment3)
    db.session.add(comment4)
    db.session.add(comment5)
    db.session.add(comment6)
    db.session.add(comment7)
    db.session.add(comment8)
    db.session.add(comment9)
    db.session.add(comment10)
    db.session.add(comment11)
    db.session.add(comment12)
    db.session.add(comment13)
    db.session.add(comment14)
    db.session.add(comment15)
    db.session.commit()


def undo_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comments"))

    db.session.commit()
