from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='007',
        email='demo@aa.io',
        password='password',
        first_name='James',
        last_name='Bond',
        about='I am James Bond, the renowned secret agent known for my impeccable style, quick wit, and daring adventures. From foiling villains to captivating hearts, I navigate the world of espionage with unmatched suave sophistication.',
        profile_picture='http://capstone-image-bucket2.s3.amazonaws.com/ceecae0c93384ac8b5fb2356065239da.jpg'
    )
    marnie = User(
        username='dude',
        email='marnie@aa.io',
        password='password',
        first_name='The',
        last_name='Dude',
        about="I'm the dude, man.",
        profile_picture='http://capstone-image-bucket2.s3.amazonaws.com/05fb17c6ef0846d0b28ee929665daf6d.jpg'
    )
    bobbie = User(
        username='bluto',
        email='bobbie@aa.io',
        password='password',
        first_name='John',
        last_name='Blutarsky',
        about="I am Bluto, a larger-than-life party animal with a mischievous streak. Known for my wild antics and rebellious spirit, I bring chaos and laughter to the fraternity life. From outrageous pranks to epic toga parties, I'm the life of the party, unapologetically embracing a carefree and spontaneous existence. With a zest for fun and a knack for trouble, I embody the free-spirited energy that defines the unforgettable college experience.",
        profile_picture=''
    )
    george = User(
        username='art-vandelay',
        email='georgecostanza@summerofgeorge.com',
        password='password',
        first_name='George',
        last_name='Costanza',
        about='He is a short, stocky, balding man who struggles with numerous insecurities, often dooming his romantic relationships through his own fear of being dumped. He is also remarkably lazy; during periods of unemployment he actively avoids getting a job, and while employed he often finds ingenious ways to conceal idleness from his bosses.',
        profile_picture='http://capstone-image-bucket2.s3.amazonaws.com/d1d74dc2edb34d2493b9d9329df7297c.png'

    )

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    db.session.add(george)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
