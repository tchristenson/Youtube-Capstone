from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo',
        email='demo@aa.io',
        password='password',
        first_name='Demo',
        last_name='Lition',
        about='A lover of all things art and culture. Embracing anonymity to freely express my thoughts and creativity. Join me on a journey of inspiration and exploration.',
        profile_picture='http://capstone-image-bucket2.s3.amazonaws.com/ceecae0c93384ac8b5fb2356065239da.jpg'
    )
    marnie = User(
        username='marnie',
        email='marnie@aa.io',
        password='password',
        first_name='Marnie',
        last_name='Morning',
        about='A passionate adventurer with an insatiable wanderlust. Finding joy in the unknown, I navigate twists and turns with an open mind. Join me as we embrace the thrill of discovery together.',
        profile_picture='http://capstone-image-bucket2.s3.amazonaws.com/05fb17c6ef0846d0b28ee929665daf6d.jpg'
    )
    bobbie = User(
        username='bobbie',
        email='bobbie@aa.io',
        password='password',
        first_name='Bobbie',
        last_name='Rickie',
        about='Avid reader, writer, and thinker. Seeking solace in the digital realm, I share my musings on life, love, and the human experience. Join me in unraveling the intricacies of our existence through the power of words.',
        profile_picture=''
    )

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
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
