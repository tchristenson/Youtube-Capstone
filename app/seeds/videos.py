from app.models import db, Video, environment, SCHEMA
from sqlalchemy.sql import text

def seed_videos():
    video1 = Video(
        user_id = 1,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/9500b3ed03a440b89e3a758fac4e6828.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/2c0917bba5ce48cb8e01476f28ddb195.png'
    )
    video2 = Video(
        user_id = 2,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/28412f3e38bd4a24bb8ca160a186acbe.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/c39231205f044f4fba0a66c452bc1720.png'
    )
    video3 = Video(
        user_id = 3,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/b0f010c70b514240acd7f873e16bd49e.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/d63f2ff9f0be44b6a19ebfd55851decc.png'
    )
    video4 = Video(
        user_id = 4,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/054b3d83692c4935876714179a0d38c1.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/37946ea902ce4bf3ac54a677d90e330c.png'
    )
    video5 = Video(
        user_id = 5,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/a405cfdcfb5c4335b9390e729d36ca25.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/29f563c3f2fe4073863b46e02995b93c.png'
    )
    video6 = Video(
        user_id = 6,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/33a560a768f04a92a2b171cbd0210c20.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/31a33932604e416ea3038a8b78b9cec4.png'
    )
    video7 = Video(
        user_id = 7,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/5c64b4cd73394362af2ddef7d32486d7.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/6996374e466340eba289f5c11c3a6730.png'
    )
    video8 = Video(
        user_id = 8,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/7346ae4ac5de4c4cb0894ca7097d3916.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/60998de4dd584228bf0163519d091486.png'
    )
    video9 = Video(
        user_id = 9,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/8e4d9386612948a88a1951543d342462.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/5637215d6c284053b13d1f8930ba6485.png'
    )
    video10 = Video(
        user_id = 10,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/da34416910db42bd88dfdc12acc63cbf.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/765f05015e9045f09dd48c9e3c322201.png'
    )
    video11 = Video(
        user_id = 1,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/9f3108c19ce34ceb81bb20a2380882e6.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/ea80630938324ac2976be130e0f6f6d1.png'
    )
    video12 = Video(
        user_id = 2,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/ffd1115447cc4d2d9d6857785753e2cc.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/e8bd6caf6c5a41d3ab8cd9848554a170.png'
    )
    video13 = Video(
        user_id = 3,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/1c8a00096c5e431cb5b83b4380e0255a.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/7729d5819ed24220a193eb1bddb6b20a.png'
    )
    video14 = Video(
        user_id = 4,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/c3ead175f8dd4924bebbc96ce3c09892.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/f77e5f897e5e4fc38d5d85fece92759b.png'
    )
    video15 = Video(
        user_id = 5,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/dae57164b11f444f8c47a8ecb63bea78.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/2c8f6d6faa5d4c3284fcf7c8a3401b59.png'
    )
    video16 = Video(
        user_id = 6,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/ea61933f141a45e082fa80212a439d05.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/f3166c91980c46a8b495454ecfcf574a.png'
    )
    video17 = Video(
        user_id = 7,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/b2c2c145d70b42a38159a0a745be745d.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/b68d9b14862649c9aaed49abe8fd397c.png'
    )
    video18 = Video(
        user_id = 8,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/d8fabd980f1c4af2826012a5d38184b5.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/4da12444e8aa4f018abcacd8f6b779d3.png'
    )
    video19 = Video(
        user_id = 9,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/c3ab279f96e842bd9892db8e53db3a58.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/35154e019bd4400fbb579c3ed3d98f63.png	'
    )
    video20 = Video(
        user_id = 10,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/b5546034bba64ce7ab87ec0380260a9b.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/ac2ba8ff2f264aea875ca037a162f3ee.png'
    )
    video21 = Video(
        user_id = 1,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/360f5f3a2a23488fabffed22d5d76597.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/b5e0fdc442d84e2f8e3d29384d439794.png'
    )
    video22 = Video(
        user_id = 4,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/f5ec5b471f4e40d59aee98df4767bb31.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/310babb09d2d475a8112647bf49616d2.png'
    )
    video23 = Video(
        user_id = 8,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/893a81fc2d2f48caa6de9777766a386a.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/d0609e1a130a417b97cfc0f550218a6f.png'
    )
    video24 = Video(
        user_id = 9,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/d97d3c5d6b514c51974621bb7b522dc6.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/6e5a9ceb54344364aad13c6f8555024f.png'
    )
    video25 = Video(
        user_id = 9,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/d40c5abad1d144128da627bb4f7aee47.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/4e4bf994bdc34a57a11884db6e74aeb0.png'
    )
    video26 = Video(
        user_id = 2,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/dfaf88bcaa864954a3e55c274bd24f25.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/34d5f78c7ee74535b886ae6869e097ed.png'
    )
    video27 = Video(
        user_id = 3,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/ce5e8613769244ca951e0b3446101634.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/3dbf7419fd264a129e4c652f28f527f6.png'
    )
    video28 = Video(
        user_id = 4,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/ca461cc293784dea85badf2b2e22b9f3.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/68bd83eb2bf2462fa4d88a9c5b70a718.png'
    )
    video29 = Video(
        user_id = 4,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/1a8f7e61732e4d0292f4c8f596d6e74e.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/71bcf8ca052248af8a6dc98437f81860.png'
    )
    video30 = Video(
        user_id = 7,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/2b596da4e9f8439ebf5cb618004ee93e.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/438e939346634848b64eb58eb56e12d1.png'
    )
    video31 = Video(
        user_id = 9,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/2a03182a723b44c398d0cec00e9579bd.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/c43aae32c3004032a3218f07d4520d3c.png'
    )
    video32 = Video(
        user_id = 10,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/7df2dd09f02d46c78adaa19942dd4f57.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/267175c98e584f178da3b03e3c38c69d.png'
    )
    video33 = Video(
        user_id = 8,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/77e6d16460ec4725a56ef7a5c13488b6.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/c63cd0f851b4445794316cd5d3154a05.png'
    )
    video34 = Video(
        user_id = 1,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/976f345fe40d4c43ae40bf611db8fd36.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/3bbc5bc7cd854ca284a68bb15b3e1654.png'
    )
    video35 = Video(
        user_id = 3,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/7893acd551b24bb3b781a242a106bc34.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/b601d4e7534640e89e51284f03cfbdbf.png'
    )
    video36 = Video(
        user_id = 4,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/7c2ffbe17a084aa5a20a7271c1f0e422.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/3309a9d45a97402690cc62e9b38cc41c.png'
    )
    video37 = Video(
        user_id = 6,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/529366187cea43799c8dea39c78f16d0.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/fd1836bb5beb4145b8896c3a54bca2cf.png'
    )
    video38 = Video(
        user_id = 7,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/b1bd516bc8994401920a34666a71f39f.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/b732d4cac9d84ef5b9ad088c48925366.png'
    )
    video39 = Video(
        user_id = 9,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/5bc95f8e55d4475f8b3f653acf9bf1f2.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/414706e913fb4210952e49f6078ac46a.png'
    )
    video40 = Video(
        user_id = 6,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/4e38fe8160524fe7a5c19d482d36701f.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/6544443bea544a98b0c27473eabbdf10.png'
    )
    video41 = Video(
        user_id = 2,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/5c90dacdfb2f4e6f999dd259c962e861.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/b96daebb389f49a49a4ffc12e5f9fdd0.png'
    )
    video42 = Video(
        user_id = 3,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/4862034f6d804454b3fe6538018bdb64.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/f480677d63fe4eb4a084e413d771aa92.png'
    )
    video43 = Video(
        user_id = 5,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/c3bd5c6821d640d6a587c83c19205edf.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/7dd0b59853e84168a1bfba97bca0dd56.png'
    )
    video44 = Video(
        user_id = 6,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/37900192df784e08831e0ef724e68a3c.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/ff585e7cc02041d98f47a993691da2b9.png'
    )
    video45 = Video(
        user_id = 7,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/bfb2b03c9f99432aa79166d6a47da303.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/1b9353d76d504a8cb8c564bbd5fc73e1.png'
    )
    video46 = Video(
        user_id = 8,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/ac222daaf9444481a39999e03504fbdb.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/09c97398a3f74f938ceabd282074c2aa.png'
    )
    video47 = Video(
        user_id = 9,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/7c185cd2c7074c28b8033c4e6600ec2a.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/ad86831e6a6549939ae154d66054ea86.png'
    )
    video48 = Video(
        user_id = 2,
        name = '',
        description = '',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/46df9c40a10149fa8b793a72b2dbfb85.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/c432f034f354448d9d76fa9266e37b6c.png'
    )

    db.session.add(video1)
    db.session.add(video2)
    db.session.add(video3)
    db.session.add(video4)
    db.session.add(video5)
    db.session.add(video6)
    db.session.add(video7)
    db.session.add(video8)
    db.session.add(video9)
    db.session.add(video10)
    db.session.add(video11)
    db.session.add(video12)
    db.session.add(video13)
    db.session.add(video14)
    db.session.add(video15)
    db.session.add(video16)
    db.session.add(video17)
    db.session.add(video18)
    db.session.add(video19)
    db.session.add(video20)
    db.session.add(video21)
    db.session.add(video22)
    db.session.add(video23)
    db.session.add(video24)
    db.session.add(video25)
    db.session.add(video26)
    db.session.add(video27)
    db.session.add(video28)
    db.session.add(video29)
    db.session.add(video30)
    db.session.add(video31)
    db.session.add(video32)
    db.session.add(video33)
    db.session.add(video34)
    db.session.add(video35)
    db.session.add(video36)
    db.session.add(video37)
    db.session.add(video38)
    db.session.add(video39)
    db.session.add(video40)
    db.session.add(video41)
    db.session.add(video42)
    db.session.add(video43)
    db.session.add(video44)
    db.session.add(video45)
    db.session.add(video46)
    db.session.add(video47)
    db.session.add(video48)
    db.session.commit()


def undo_videos():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.videos RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM videos"))

    db.session.commit()
