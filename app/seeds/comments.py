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
    comment16 = Comment(
        user_id=4,
        video_id=12,
        content="This video blew my mind! Such incredible content."
    )
    comment17 = Comment(
        user_id=7,
        video_id=32,
        content="Wow, just wow! I couldn't take my eyes off the screen."
    )

    comment18 = Comment(
        user_id=2,
        video_id=18,
        content="I'm speechless! This video deserves all the awards."
    )

    comment19 = Comment(
        user_id=9,
        video_id=7,
        content="I can't stop watching this video, it's addicting!"
    )

    comment20 = Comment(
        user_id=3,
        video_id=24,
        content="Absolutely mind-blowing! This video deserves millions of views."
    )

    comment21 = Comment(
        user_id=8,
        video_id=41,
        content="Brilliant video! It left me in awe from start to finish."
    )

    comment22 = Comment(
        user_id=5,
        video_id=15,
        content="This video is pure gold. Kudos to the creators!"
    )

    comment23 = Comment(
        user_id=1,
        video_id=29,
        content="I'm completely mesmerized by this video. Great job!"
    )

    comment24 = Comment(
        user_id=6,
        video_id=3,
        content="I can't get enough of this video. So captivating!"
    )

    comment25 = Comment(
        user_id=10,
        video_id=46,
        content="This video has exceeded all my expectations. Well done!"
    )
    comment26 = Comment(
        user_id=2,
        video_id=14,
        content="This video is pure perfection. I'm in awe!"
    )

    comment27 = Comment(
        user_id=7,
        video_id=38,
        content="Wow, what a video! It had me on the edge of my seat."
    )

    comment28 = Comment(
        user_id=5,
        video_id=5,
        content="This video deserves all the praise. Incredible work!"
    )

    comment29 = Comment(
        user_id=10,
        video_id=33,
        content="I'm hooked on this video. Can't get enough of it!"
    )

    comment30 = Comment(
        user_id=6,
        video_id=19,
        content="Bravo! This video is a true masterpiece."
    )

    comment31 = Comment(
        user_id=9,
        video_id=8,
        content="This video is a feast for the eyes. Absolutely stunning!"
    )

    comment32 = Comment(
        user_id=3,
        video_id=25,
        content="I'm completely blown away by this video. So impressive!"
    )

    comment33 = Comment(
        user_id=8,
        video_id=42,
        content="This video has left me speechless. Incredible work!"
    )

    comment34 = Comment(
        user_id=1,
        video_id=30,
        content="I can't stop watching this video. It's addictive!"
    )

    comment35 = Comment(
        user_id=4,
        video_id=13,
        content="This video is a true gem. I'm in awe of its brilliance."
    )
    comment36 = Comment(
        user_id=2,
        video_id=16,
        content="This video is pure gold! I'm amazed by the quality."
    )

    comment37 = Comment(
        user_id=7,
        video_id=6,
        content="Wow, this video blew me away. So well done!"
    )

    comment38 = Comment(
        user_id=5,
        video_id=27,
        content="This video is a masterpiece. It deserves recognition!"
    )

    comment39 = Comment(
        user_id=10,
        video_id=42,
        content="I can't get enough of this video. It's mesmerizing!"
    )

    comment40 = Comment(
        user_id=6,
        video_id=13,
        content="Brilliant work! This video is truly captivating."
    )

    comment41 = Comment(
        user_id=9,
        video_id=32,
        content="This video is a visual treat. I'm in awe of it!"
    )

    comment42 = Comment(
        user_id=3,
        video_id=21,
        content="Impressive! This video showcases incredible talent."
    )

    comment43 = Comment(
        user_id=8,
        video_id=35,
        content="This video is outstanding. It left me speechless."
    )

    comment44 = Comment(
        user_id=1,
        video_id=11,
        content="I'm hooked on this video. Can't stop watching it!"
    )

    comment45 = Comment(
        user_id=4,
        video_id=26,
        content="Kudos to the creators! This video is pure magic."
    )
    comment46 = Comment(
        user_id=4,
        video_id=33,
        content="This video is absolutely incredible. I'm blown away!"
    )

    comment47 = Comment(
        user_id=1,
        video_id=9,
        content="Wow, this video is a masterpiece. I'm in awe!"
    )

    comment48 = Comment(
        user_id=8,
        video_id=22,
        content="I can't get enough of this video. It's captivating!"
    )

    comment49 = Comment(
        user_id=3,
        video_id=41,
        content="Impressive work! This video deserves recognition."
    )

    comment50 = Comment(
        user_id=9,
        video_id=17,
        content="This video is a true gem. It's captivating from start to finish."
    )

    comment51 = Comment(
        user_id=2,
        video_id=31,
        content="Bravo! This video showcases incredible talent."
    )

    comment52 = Comment(
        user_id=7,
        video_id=13,
        content="This video is top-notch. The editing is superb!"
    )

    comment53 = Comment(
        user_id=6,
        video_id=36,
        content="I'm hooked on this video. It's an absolute delight."
    )

    comment54 = Comment(
        user_id=10,
        video_id=7,
        content="This video is mesmerizing. I can't look away!"
    )

    comment55 = Comment(
        user_id=5,
        video_id=25,
        content="Incredible work! This video is a visual masterpiece."
    )
    comment56 = Comment(
        user_id=6,
        video_id=38,
        content="This video is pure art. It deserves all the praise."
    )

    comment57 = Comment(
        user_id=10,
        video_id=15,
        content="Wow, this video is mind-blowing. I'm in awe!"
    )

    comment58 = Comment(
        user_id=5,
        video_id=28,
        content="I can't stop watching this video. It's addictive!"
    )

    comment59 = Comment(
        user_id=1,
        video_id=12,
        content="This video is a masterpiece. It's truly inspiring!"
    )

    comment60 = Comment(
        user_id=9,
        video_id=23,
        content="Brilliant work! This video is a visual feast."
    )

    comment61 = Comment(
        user_id=4,
        video_id=40,
        content="This video is exceptional. It's a true work of art."
    )

    comment62 = Comment(
        user_id=2,
        video_id=19,
        content="Impressive editing skills! This video is top-notch."
    )

    comment63 = Comment(
        user_id=7,
        video_id=35,
        content="I'm captivated by this video. It's simply amazing!"
    )

    comment64 = Comment(
        user_id=3,
        video_id=9,
        content="This video is a true gem. It's captivating and beautiful."
    )

    comment65 = Comment(
        user_id=8,
        video_id=26,
        content="Incredible visuals! This video is a visual delight."
    )
    comment66 = Comment(
        user_id=8,
        video_id=17,
        content="This video is absolutely stunning. I'm in awe!"
    )

    comment67 = Comment(
        user_id=3,
        video_id=32,
        content="Wow, this video is breathtaking. It's a must-watch!"
    )

    comment68 = Comment(
        user_id=7,
        video_id=25,
        content="I can't get enough of this video. It's so mesmerizing!"
    )

    comment69 = Comment(
        user_id=2,
        video_id=14,
        content="This video is a true masterpiece. It's captivating."
    )

    comment70 = Comment(
        user_id=6,
        video_id=22,
        content="Bravo to the creators! This video is outstanding."
    )

    comment71 = Comment(
        user_id=10,
        video_id=37,
        content="This video blew my mind. The visuals are stunning."
    )

    comment72 = Comment(
        user_id=5,
        video_id=16,
        content="I'm hooked on this video. It's pure entertainment."
    )

    comment73 = Comment(
        user_id=1,
        video_id=29,
        content="This video is a visual treat. I can't stop watching!"
    )

    comment74 = Comment(
        user_id=9,
        video_id=11,
        content="This video is pure magic. It's incredibly well-crafted."
    )

    comment75 = Comment(
        user_id=4,
        video_id=24,
        content="Incredible work! This video is a true masterpiece."
    )
    comment76 = Comment(
        user_id=4,
        video_id=33,
        content="This video is absolutely incredible. I'm blown away!"
    )

    comment77 = Comment(
        user_id=1,
        video_id=9,
        content="Wow, this video is a masterpiece. I'm in awe!"
    )

    comment78 = Comment(
        user_id=8,
        video_id=22,
        content="I can't get enough of this video. It's captivating!"
    )

    comment79 = Comment(
        user_id=3,
        video_id=41,
        content="Impressive work! This video deserves recognition."
    )

    comment80 = Comment(
        user_id=9,
        video_id=17,
        content="This video is a true gem. It's captivating from start to finish."
    )

    comment81 = Comment(
        user_id=2,
        video_id=31,
        content="Bravo! This video showcases incredible talent."
    )

    comment82 = Comment(
        user_id=7,
        video_id=13,
        content="This video is top-notch. The editing is superb!"
    )

    comment83 = Comment(
        user_id=6,
        video_id=36,
        content="I'm hooked on this video. It's an absolute delight."
    )

    comment84 = Comment(
        user_id=10,
        video_id=7,
        content="This video is mesmerizing. I can't look away!"
    )

    comment85 = Comment(
        user_id=5,
        video_id=25,
        content="Incredible work! This video is a visual masterpiece."
    )
    comment86 = Comment(
        user_id=5,
        video_id=38,
        content="This video is absolutely amazing. I'm speechless!"
    )

    comment87 = Comment(
        user_id=10,
        video_id=15,
        content="Wow, this video is truly remarkable. It's a must-see!"
    )

    comment88 = Comment(
        user_id=6,
        video_id=28,
        content="I'm obsessed with this video. It's so captivating!"
    )

    comment89 = Comment(
        user_id=1,
        video_id=12,
        content="This video is a true inspiration. It's incredibly well-made."
    )

    comment90 = Comment(
        user_id=9,
        video_id=23,
        content="Kudos to the creators! This video is simply outstanding."
    )

    comment91 = Comment(
        user_id=4,
        video_id=40,
        content="This video is exceptional. It's a visual feast for the eyes."
    )

    comment92 = Comment(
        user_id=2,
        video_id=19,
        content="Impressive editing skills! This video is a true masterpiece."
    )

    comment93 = Comment(
        user_id=7,
        video_id=35,
        content="I'm completely absorbed by this video. It's simply amazing!"
    )

    comment94 = Comment(
        user_id=3,
        video_id=9,
        content="This video is a hidden gem. It deserves more recognition."
    )

    comment95 = Comment(
        user_id=8,
        video_id=26,
        content="Mind-blowing visuals! This video is a visual delight."
    )
    comment96 = Comment(
        user_id=8,
        video_id=16,
        content="This video is absolutely mesmerizing. I'm in awe!"
    )

    comment97 = Comment(
        user_id=3,
        video_id=33,
        content="Wow, this video is breathtaking. It's a must-watch!"
    )

    comment98 = Comment(
        user_id=7,
        video_id=25,
        content="I can't get enough of this video. It's so captivating!"
    )

    comment99 = Comment(
        user_id=2,
        video_id=14,
        content="This video is a true masterpiece. It's captivating."
    )

    comment100 = Comment(
        user_id=6,
        video_id=22,
        content="Bravo to the creators! This video is outstanding."
    )

    comment101 = Comment(
        user_id=10,
        video_id=37,
        content="This video blew my mind. The visuals are stunning."
    )

    comment102 = Comment(
        user_id=5,
        video_id=16,
        content="I'm hooked on this video. It's pure entertainment."
    )

    comment103 = Comment(
        user_id=1,
        video_id=29,
        content="This video is a visual treat. I can't stop watching!"
    )

    comment104 = Comment(
        user_id=9,
        video_id=11,
        content="This video is pure magic. It's incredibly well-crafted."
    )

    comment105 = Comment(
        user_id=4,
        video_id=24,
        content="Incredible work! This video is a true masterpiece."
    )
    comment106 = Comment(
        user_id=4,
        video_id=42,
        content="This video is simply mind-blowing. I'm in awe!"
    )

    comment107 = Comment(
        user_id=9,
        video_id=18,
        content="Wow, this video is absolutely stunning. It's incredible!"
    )

    comment108 = Comment(
        user_id=1,
        video_id=32,
        content="I can't get enough of this video. It's so captivating!"
    )

    comment109 = Comment(
        user_id=6,
        video_id=7,
        content="This video is a true masterpiece. It's incredibly well-made."
    )

    comment110 = Comment(
        user_id=2,
        video_id=26,
        content="Kudos to the creators! This video is outstanding."
    )

    comment111 = Comment(
        user_id=10,
        video_id=10,
        content="This video is exceptional. It's a visual feast for the eyes."
    )

    comment112 = Comment(
        user_id=3,
        video_id=36,
        content="Impressive editing skills! This video is a true masterpiece."
    )

    comment113 = Comment(
        user_id=7,
        video_id=21,
        content="I'm completely absorbed by this video. It's simply amazing!"
    )

    comment114 = Comment(
        user_id=5,
        video_id=9,
        content="This video is a hidden gem. It deserves more recognition."
    )

    comment115 = Comment(
        user_id=8,
        video_id=27,
        content="Mind-blowing visuals! This video is a visual delight."
    )
    comment116 = Comment(
        user_id=8,
        video_id=38,
        content="This video is absolutely mesmerizing. I can't look away!"
    )

    comment117 = Comment(
        user_id=3,
        video_id=15,
        content="Wow, this video is breathtaking. It's a must-see!"
    )

    comment118 = Comment(
        user_id=7,
        video_id=28,
        content="I'm hooked on this video. It's so captivating!"
    )

    comment119 = Comment(
        user_id=2,
        video_id=12,
        content="This video is a true gem. It's incredibly well-made."
    )

    comment120 = Comment(
        user_id=6,
        video_id=23,
        content="Bravo to the creators! This video is outstanding."
    )

    comment121 = Comment(
        user_id=10,
        video_id=40,
        content="This video blew my mind. The visuals are stunning."
    )

    comment122 = Comment(
        user_id=5,
        video_id=19,
        content="I'm obsessed with this video. It's pure entertainment."
    )

    comment123 = Comment(
        user_id=1,
        video_id=35,
        content="This video is a visual treat. It's mesmerizing!"
    )

    comment124 = Comment(
        user_id=9,
        video_id=9,
        content="This video is pure magic. It's incredibly captivating."
    )

    comment125 = Comment(
        user_id=4,
        video_id=26,
        content="Incredible work! This video is a true masterpiece."
    )
    comment126 = Comment(
        user_id=4,
        video_id=43,
        content="This video is mind-blowing. It left me speechless!"
    )

    comment127 = Comment(
        user_id=9,
        video_id=19,
        content="Wow, this video is absolutely stunning. It's incredible!"
    )

    comment128 = Comment(
        user_id=1,
        video_id=33,
        content="I can't get enough of this video. It's so captivating!"
    )

    comment129 = Comment(
        user_id=6,
        video_id=15,
        content="This video is a true masterpiece. It's incredibly well-crafted."
    )

    comment130 = Comment(
        user_id=2,
        video_id=28,
        content="Kudos to the creators! This video is outstanding."
    )

    comment131 = Comment(
        user_id=10,
        video_id=14,
        content="This video is exceptional. It's a visual feast for the eyes."
    )

    comment132 = Comment(
        user_id=3,
        video_id=37,
        content="Impressive editing skills! This video is a true work of art."
    )

    comment133 = Comment(
        user_id=7,
        video_id=22,
        content="I'm completely absorbed by this video. It's simply amazing!"
    )

    comment134 = Comment(
        user_id=5,
        video_id=11,
        content="This video is a hidden gem. It deserves more recognition."
    )

    comment135 = Comment(
        user_id=8,
        video_id=29,
        content="Mind-blowing visuals! This video is a visual delight."
    )
    comment136 = Comment(
        user_id=8,
        video_id=39,
        content="This video is absolutely mesmerizing. I can't look away!"
    )

    comment137 = Comment(
        user_id=3,
        video_id=16,
        content="Wow, this video is breathtaking. It's a must-see!"
    )

    comment138 = Comment(
        user_id=7,
        video_id=29,
        content="I'm hooked on this video. It's so captivating!"
    )

    comment139 = Comment(
        user_id=2,
        video_id=13,
        content="This video is a true gem. It's incredibly well-made."
    )

    comment140 = Comment(
        user_id=6,
        video_id=24,
        content="Bravo to the creators! This video is outstanding."
    )

    comment141 = Comment(
        user_id=10,
        video_id=41,
        content="This video blew my mind. The visuals are stunning."
    )

    comment142 = Comment(
        user_id=5,
        video_id=20,
        content="I'm obsessed with this video. It's pure entertainment."
    )

    comment143 = Comment(
        user_id=1,
        video_id=36,
        content="This video is a visual treat. It's mesmerizing!"
    )

    comment144 = Comment(
        user_id=9,
        video_id=10,
        content="This video is pure magic. It's incredibly captivating."
    )

    comment145 = Comment(
        user_id=4,
        video_id=27,
        content="Incredible work! This video is a true masterpiece."
    )
    comment146 = Comment(
        user_id=4,
        video_id=44,
        content="This video is mind-blowing. It left me speechless!"
    )

    comment147 = Comment(
        user_id=9,
        video_id=20,
        content="Wow, this video is absolutely stunning. It's incredible!"
    )

    comment148 = Comment(
        user_id=1,
        video_id=34,
        content="I can't get enough of this video. It's so captivating!"
    )

    comment149 = Comment(
        user_id=6,
        video_id=16,
        content="This video is a true masterpiece. It's incredibly well-crafted."
    )

    comment150 = Comment(
        user_id=2,
        video_id=29,
        content="Kudos to the creators! This video is outstanding."
    )

    comment151 = Comment(
        user_id=10,
        video_id=15,
        content="This video is exceptional. It's a visual feast for the eyes."
    )

    comment152 = Comment(
        user_id=3,
        video_id=38,
        content="Impressive editing skills! This video is a true work of art."
    )

    comment153 = Comment(
        user_id=7,
        video_id=23,
        content="I'm completely absorbed by this video. It's simply amazing!"
    )

    comment154 = Comment(
        user_id=5,
        video_id=12,
        content="This video is a hidden gem. It deserves more recognition."
    )

    comment155 = Comment(
        user_id=8,
        video_id=30,
        content="Mind-blowing visuals! This video is a visual delight."
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
    db.session.add(comment16)
    db.session.add(comment17)
    db.session.add(comment18)
    db.session.add(comment16)
    db.session.add(comment17)
    db.session.add(comment18)
    db.session.add(comment19)
    db.session.add(comment20)
    db.session.add(comment21)
    db.session.add(comment22)
    db.session.add(comment23)
    db.session.add(comment24)
    db.session.add(comment25)
    db.session.add(comment26)
    db.session.add(comment27)
    db.session.add(comment28)
    db.session.add(comment29)
    db.session.add(comment30)
    db.session.add(comment31)
    db.session.add(comment32)
    db.session.add(comment33)
    db.session.add(comment34)
    db.session.add(comment35)
    db.session.add(comment36)
    db.session.add(comment37)
    db.session.add(comment38)
    db.session.add(comment39)
    db.session.add(comment40)
    db.session.add(comment41)
    db.session.add(comment42)
    db.session.add(comment43)
    db.session.add(comment44)
    db.session.add(comment45)
    db.session.add(comment46)
    db.session.add(comment47)
    db.session.add(comment48)
    db.session.add(comment49)
    db.session.add(comment50)
    db.session.add(comment51)
    db.session.add(comment52)
    db.session.add(comment53)
    db.session.add(comment54)
    db.session.add(comment55)
    db.session.add(comment56)
    db.session.add(comment57)
    db.session.add(comment58)
    db.session.add(comment59)
    db.session.add(comment60)
    db.session.add(comment61)
    db.session.add(comment62)
    db.session.add(comment63)
    db.session.add(comment64)
    db.session.add(comment65)
    db.session.add(comment66)
    db.session.add(comment67)
    db.session.add(comment68)
    db.session.add(comment69)
    db.session.add(comment70)
    db.session.add(comment71)
    db.session.add(comment72)
    db.session.add(comment73)
    db.session.add(comment74)
    db.session.add(comment75)
    db.session.add(comment76)
    db.session.add(comment77)
    db.session.add(comment78)
    db.session.add(comment79)
    db.session.add(comment80)
    db.session.add(comment81)
    db.session.add(comment82)
    db.session.add(comment83)
    db.session.add(comment84)
    db.session.add(comment85)
    db.session.add(comment86)
    db.session.add(comment87)
    db.session.add(comment88)
    db.session.add(comment89)
    db.session.add(comment90)
    db.session.add(comment91)
    db.session.add(comment92)
    db.session.add(comment93)
    db.session.add(comment94)
    db.session.add(comment95)
    db.session.add(comment96)
    db.session.add(comment97)
    db.session.add(comment98)
    db.session.add(comment99)
    db.session.add(comment100)
    db.session.add(comment101)
    db.session.add(comment102)
    db.session.add(comment103)
    db.session.add(comment104)
    db.session.add(comment105)
    db.session.add(comment106)
    db.session.add(comment107)
    db.session.add(comment108)
    db.session.add(comment109)
    db.session.add(comment110)
    db.session.add(comment111)
    db.session.add(comment112)
    db.session.add(comment113)
    db.session.add(comment114)
    db.session.add(comment115)
    db.session.add(comment116)
    db.session.add(comment117)
    db.session.add(comment118)
    db.session.add(comment119)
    db.session.add(comment120)
    db.session.add(comment121)
    db.session.add(comment122)
    db.session.add(comment123)
    db.session.add(comment124)
    db.session.add(comment125)
    db.session.add(comment126)
    db.session.add(comment127)
    db.session.add(comment128)
    db.session.add(comment129)
    db.session.add(comment130)
    db.session.add(comment131)
    db.session.add(comment132)
    db.session.add(comment133)
    db.session.add(comment134)
    db.session.add(comment135)
    db.session.add(comment136)
    db.session.add(comment137)
    db.session.add(comment138)
    db.session.add(comment139)
    db.session.add(comment140)
    db.session.add(comment141)
    db.session.add(comment142)
    db.session.add(comment143)
    db.session.add(comment144)
    db.session.add(comment145)
    db.session.add(comment146)
    db.session.add(comment147)
    db.session.add(comment148)
    db.session.add(comment149)
    db.session.add(comment150)
    db.session.add(comment151)
    db.session.add(comment152)
    db.session.add(comment153)
    db.session.add(comment154)
    db.session.add(comment155)
    db.session.commit()


def undo_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comments"))

    db.session.commit()
