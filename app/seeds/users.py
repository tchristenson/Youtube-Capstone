from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text
from .shared_data import shared_user_list
import random


# Adds a demo user, you can add other users here if you want
def seed_users():
    morgan = User(
        username='morgan-freeman',
        email='morganfreeman@email.com',
        password='password',
        first_name='Morgan',
        last_name='Freeman',
        about="With a voice that resonates through your very being, I draw you in with tales that captivate the soul. Each line etched upon my face tells a story of a life lived fully, and my presence exudes grace and humility. I am Morgan Freeman, a legend whose performances and advocacy have left an indelible mark on the world.",
        profile_picture='http://capstone-image-bucket2.s3.amazonaws.com/f10fbcc7541e44089c16aad00ef53559.jpg'
    )
    ferris = User(
        username='save-ferris',
        email='ferris@email.com',
        password='password',
        first_name='Ferris',
        last_name='Bueller',
        about="I am the epitome of teenage charm and mischief. With an irresistible charisma that captures hearts, I navigate life with a fearless spirit and a mischievous twinkle in my eye. Whether I'm playing hooky from school or orchestrating elaborate schemes, my quick wit and cunning maneuvers keep everyone on their toes.",
        profile_picture='http://capstone-image-bucket2.s3.amazonaws.com/a38de0ed2e7844638c7f7ad2a54db27c.png'
    )
    dude = User(
        username='the-dude',
        email='the-dude@dude.com',
        password='password',
        first_name='The',
        last_name='Dude',
        about="I'm the dude, man.",
        profile_picture='http://capstone-image-bucket2.s3.amazonaws.com/4b9d103000ef49d2a21af176da0eef81.png'
    )
    george = User(
        username='art-vandelay',
        email='georgecostanza@summerofgeorge.com',
        password='password',
        first_name='George',
        last_name='Costanza',
        about='He is a short, stocky, balding man who struggles with numerous insecurities, often dooming his romantic relationships through his own fear of being dumped. He is also remarkably lazy; during periods of unemployment he actively avoids getting a job, and while employed he often finds ingenious ways to conceal idleness from his bosses.',
        profile_picture='http://capstone-image-bucket2.s3.amazonaws.com/38c49ef7ffd04f8b831fc427d0e4c345.png'

    )
    larry = User(
        username='larry-david',
        email='larry@email.com',
        password='password',
        first_name='Larry',
        last_name='David',
        about='I am the unapologetically honest and unabashedly neurotic individual who thrives on the uncomfortable and absurd moments of life. With a knack for finding myself in the most cringe-worthy situations, I navigate through social norms with a refreshing disregard. My signature blend of dry wit and self-deprecating humor keeps audiences laughing and squirming simultaneously.',
        profile_picture='http://capstone-image-bucket2.s3.amazonaws.com/d4604036e0714ff99a5c18187817890c.png'

    )
    tom = User(
        username='tom-cruise',
        email='tom@cruise.com',
        password='password',
        first_name='Tom',
        last_name='Cruise',
        about="I embody the essence of a true Hollywood icon. With a charismatic presence that electrifies the screen, I command attention and captivate audiences worldwide. Whether I'm sprinting through action-packed sequences or delving into complex characters, my commitment to my craft is unparalleled. I bring an intensity and physicality that leaves viewers breathless.",
        profile_picture='http://capstone-image-bucket2.s3.amazonaws.com/3d4d6297c8b54e61b87b28d9d5ee9742.png'

    )
    gordon = User(
        username='gordon-ramsay',
        email='gordon@ramsay.com',
        password='password',
        first_name='Gordon',
        last_name='Ramsay',
        about="I am a culinary force to be reckoned with. With fiery passion and an unyielding commitment to excellence, I command the kitchen with authority and expertise. I am known for my high standards and relentless pursuit of culinary perfection. Beyond the intense persona, I am a skilled chef with an impeccable palate and a deep understanding of flavors.",
        profile_picture='http://capstone-image-bucket2.s3.amazonaws.com/0efadea0604345209635fa24c61544cd.png'

    )
    betty = User(
        username='betty-white',
        email='betty@white.com',
        password='password',
        first_name='Betty',
        last_name='White',
        about="I radiate timeless charm and effervescent wit. With a career spanning decades, I am a beloved icon of television and comedy. My infectious smile and twinkling eyes bring joy to audiences of all ages. Whether delivering punchlines with impeccable timing or enchanting viewers with my endearing warmth, I captivate hearts effortlessly. I have left an indelible mark with my unmatched talent and versatility.",
        profile_picture='http://capstone-image-bucket2.s3.amazonaws.com/d802808082bf467ea81e3863fa95f6a0.png'

    )
    kim = User(
        username='kim-kardashian',
        email='kim@email.com',
        password='password',
        first_name='Kim',
        last_name='Kardashian',
        about='I embody the essence of modern-day fame and influence. With a captivating presence that permeates popular culture, I have become a household name. Known for my impeccable fashion sense and flawless aesthetics, I have redefined beauty standards and shaped trends. From reality TV to business ventures, I have leveraged my platform to build a successful empire.',
        profile_picture='http://capstone-image-bucket2.s3.amazonaws.com/127531253e734dfd90a9234772fbe522.png'

    )
    hermione = User(
        username='hermione-granger',
        email='hermione@email.com',
        password='password',
        first_name='Hermione',
        last_name='Granger',
        about="With a thirst for knowledge and a love for books, I am the brightest witch of my age. My unruly hair and studious nature showcase my relentless pursuit of academic excellence. From casting spells to solving complex puzzles, I am always ready to take on any challenge with unwavering confidence. I am a magical force who reminds us all that bravery and knowledge can change the world.",
        profile_picture='http://capstone-image-bucket2.s3.amazonaws.com/f58284ed395b41b698f1c1fabb6f25f1.png'

    )

    db.session.add(morgan)
    db.session.add(ferris)
    db.session.add(dude)
    db.session.add(george)
    db.session.add(larry)
    db.session.add(tom)
    db.session.add(gordon)
    db.session.add(betty)
    db.session.add(kim)
    db.session.add(hermione)
    db.session.commit()

    user_list = [morgan, ferris, dude, george, larry, tom, gordon, betty, kim, hermione]

    for user in user_list:
        other_users = [u for u in user_list if u != user]

        subscribers = random.sample(other_users, k=random.randint(1, len(other_users)))
        user.subscribed.extend(subscribers)
    db.session.commit()

    shared_user_list.extend([morgan, ferris, dude, george, larry, tom, gordon, betty, kim, hermione])

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
