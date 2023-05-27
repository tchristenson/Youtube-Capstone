from app.models import db, Video, environment, SCHEMA
from sqlalchemy.sql import text

def seed_videos():
    video1 = Video(
        user_id = 1,
        name = "Graceful Bull Finch: Nature's Seed Connoisseur",
        description = "Observe the elegance of a Bull Finch as it delicately perches on a tree, savoring a delightful meal of seeds.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/9500b3ed03a440b89e3a758fac4e6828.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/2c0917bba5ce48cb8e01476f28ddb195.png'
    )
    video2 = Video(
        user_id = 2,
        name = "Mixology Masterclass: Crafted Cocktails by the Bartender Extraordinaire",
        description = "Step into the world of mixology as our skilled bartender takes you on a tantalizing journey of cocktail creation. Learn the art of mixing, shaking, and garnishing as expert hands transform premium spirits and fresh ingredients into exquisite concoctions. Get ready to elevate your taste buds with these handcrafted libations and become a cocktail connoisseur.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/28412f3e38bd4a24bb8ca160a186acbe.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/c39231205f044f4fba0a66c452bc1720.png'
    )
    video3 = Video(
        user_id = 3,
        name = "DJ Beats that Ignite the Dancefloor",
        description = "Immerse yourself in the electrifying ambiance of a bustling nightclub as the DJ spins a symphony of pulsating beats. Feel the energy surge through your veins as the crowd moves in sync to the rhythm. Let the music transport you to a euphoric state, where the only thing that matters is the dancefloor. Get ready for an unforgettable night of infectious melodies and non-stop party vibes.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/b0f010c70b514240acd7f873e16bd49e.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/d63f2ff9f0be44b6a19ebfd55851decc.png'
    )
    video4 = Video(
        user_id = 4,
        name = "A Playful Adventure with a Retriever",
        description = "Experience the pure delight as a golden retriever dashes through shallow waters, embracing the freedom and joy of the moment.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/054b3d83692c4935876714179a0d38c1.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/37946ea902ce4bf3ac54a677d90e330c.png'
    )
    video5 = Video(
        user_id = 5,
        name = "Coastal Golf Course Aerial Tour: Breathtaking Views from Above",
        description = "Take flight on a mesmerizing drone journey as it soars above a stunning coastal golf course. Behold the panoramic vistas of rolling greens, pristine fairways, and majestic ocean waves crashing against the shoreline. Immerse yourself in the beauty of this serene oasis where nature blends seamlessly with the art of golf. Join us for an unforgettable aerial adventure that captures the essence of leisure and natural splendor in perfect harmony.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/a405cfdcfb5c4335b9390e729d36ca25.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/29f563c3f2fe4073863b46e02995b93c.png'
    )
    video6 = Video(
        user_id = 6,
        name = "A Wolf's Elegant Stride in Slow Motion",
        description = "Enter the world of untamed wilderness as a magnificent wolf moves with mesmerizing elegance in slow motion. Witness the strength, poise, and raw beauty of this apex predator as every step exudes a quiet confidence. Get lost in the captivating gaze of its piercing eyes and the grace of its fluid movements. Join us on this enchanting journey to appreciate the untamed spirit and timeless allure of the wolf.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/33a560a768f04a92a2b171cbd0210c20.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/31a33932604e416ea3038a8b78b9cec4.png'
    )
    video7 = Video(
        user_id = 7,
        name = 'My buddy Charvat plays in the sand',
        description = 'If you want to be a good bunker player, do everything the opposite of what you see in this video',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/5c64b4cd73394362af2ddef7d32486d7.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/6996374e466340eba289f5c11c3a6730.png'
    )
    video8 = Video(
        user_id = 8,
        name = "Yankee Stadium: First Base Line View",
        description = "Experience the thrill of America's favorite pastime from an unparalleled vantage point on the first base line at Yankee Stadium. Get a front-row seat to the action as you soak in the electrifying atmosphere and witness the crack of the bat, the speed of the players, and the roar of the crowd. Immerse yourself in the rich history and tradition of this iconic ballpark as you enjoy an unforgettable perspective on the game. Join us for an extraordinary baseball experience that will leave you in awe.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/7346ae4ac5de4c4cb0894ca7097d3916.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/60998de4dd584228bf0163519d091486.png'
    )
    video9 = Video(
        user_id = 9,
        name = "Dustin Johnson's Swing in a Golf Tournament",
        description = "Witness golfing greatness as Dustin Johnson unleashes a powerful drive in the heat of a prestigious tournament. Marvel at the flawless mechanics and raw athleticism as his club connects with the ball, sending it soaring through the air with precision and finesse. Experience the intensity of the moment and the admiration of the crowd as this golfing maestro showcases his skill and dominance on the course.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/8e4d9386612948a88a1951543d342462.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/5637215d6c284053b13d1f8930ba6485.png'
    )
    video10 = Video(
        user_id = 10,
        name = "Leisurely Walk with Beloved Older Dogs",
        description = "Join us for a delightful stroll in the company of two cherished senior dogs. Despite their gentle pace, their love and devotion shine brightly, making them the best companions anyone could ask for.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/da34416910db42bd88dfdc12acc63cbf.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/765f05015e9045f09dd48c9e3c322201.png'
    )
    video11 = Video(
        user_id = 1,
        name = "Blue Angels Soar in Air Show",
        description = "Look up in awe as four magnificent jets take to the skies, dazzling the audience with their breathtaking maneuvers in an exhilarating air show. Feel the rush as these powerful aircraft roar past, leaving trails of excitement and wonder in their wake. Experience the adrenaline-pumping precision and skill of the pilots as they showcase the artistry of flight. Join us for an unforgettable spectacle that will leave you captivated and inspired by the wonders of aviation.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/9f3108c19ce34ceb81bb20a2380882e6.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/ea80630938324ac2976be130e0f6f6d1.png'
    )
    video12 = Video(
        user_id = 2,
        name = "Aerial Symphony: Mesmerizing Jets in High-Flying Air Show",
        description = "Prepare to be mesmerized as four impressive jets paint the sky with their awe-inspiring performance in a thrilling air show. Marvel at the synchronized precision and graceful maneuvers as these powerful aircraft soar through the heavens. Feel the exhilaration of the roaring engines and witness the skillful artistry of the pilots. Join us for a captivating symphony of flight that will leave you breathless and in awe of the magnificent capabilities of these flying marvels.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/ffd1115447cc4d2d9d6857785753e2cc.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/e8bd6caf6c5a41d3ab8cd9848554a170.png'
    )
    video13 = Video(
        user_id = 3,
        name = 'Matteo Berrettini Serving on Match Point',
        description = "Witness an unforgettable moment as a player secures victory in a thrilling tennis match at the prestigious US Open. Feel the intensity of the competition as they showcase their skill, strategy, and unwavering determination. Experience the elation of the crowd and the sheer joy radiating from the triumphant athlete. Join us in celebrating this historic achievement and the indomitable spirit of tennis excellence at the grandest stage of them all.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/1c8a00096c5e431cb5b83b4380e0255a.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/7729d5819ed24220a193eb1bddb6b20a.png'
    )
    video14 = Video(
        user_id = 4,
        name = '18-year Old Sensation Carlos Alcaraz at the 2021 US Open',
        description = 'This video is from the Grandstand court at the Arthur Ashe Tennis Center in Flushing Meadows, NY. This was before Carlos Alcaraz became the number one player in the world - good luck seeing him this close in the future!',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/c3ead175f8dd4924bebbc96ce3c09892.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/f77e5f897e5e4fc38d5d85fece92759b.png'
    )
    video15 = Video(
        user_id = 5,
        name = "Crowd Delight at Sacre Coeur, Paris",
        description = "Immerse yourself in the captivating performance of a talented man as he mesmerizes the crowd at the renowned Sacre Coeur in Paris. Feel the magic in the air as his artistic expression takes center stage, leaving spectators in awe of his skills and presence. Join the enthusiastic audience as they revel in the delightful ambiance, surrounded by the timeless beauty of this iconic landmark. Experience the joy and wonder of this unforgettable moment of entertainment that adds an extra touch of charm to the City of Lights.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/dae57164b11f444f8c47a8ecb63bea78.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/2c8f6d6faa5d4c3284fcf7c8a3401b59.png'
    )
    video16 = Video(
        user_id = 6,
        name = 'Eisbachwelle: Surfing in the center of Munich',
        description = 'The waves on the Eisbach river at the entrance to the Englischer Garten (park) attract surfers and onlookers from around the world. The spot is famous throughout the world for being the largest, best and most consistent city centre location for river surfing. People have been surfing here for 40 years.',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/ea61933f141a45e082fa80212a439d05.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/f3166c91980c46a8b495454ecfcf574a.png'
    )
    video17 = Video(
        user_id = 7,
        name = 'Nick Kyrgios Ace Against JJ Wolf',
        description = 'Taken inside the Louis Armstrong stadium at the 2022 US Open. Kyrgios went on to win the match 6-4, 6-2, 6-3.',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/b2c2c145d70b42a38159a0a745be745d.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/b68d9b14862649c9aaed49abe8fd397c.png'
    )
    video18 = Video(
        user_id = 8,
        name = "Ocean Waves Caressing Cabo's Shores",
        description = "Immerse yourself in the soothing embrace of nature as gentle ocean waves grace the sun-kissed beaches of Cabo. Experience the rhythmic dance of water meeting land, creating a harmonious symphony that echoes tranquility. Feel the warm sand between your toes and the cool breeze brushing against your skin as you indulge in a moment of pure bliss. Join us in this coastal paradise, where the mesmerizing beauty of the ocean becomes a source of rejuvenation and inner peace.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/d8fabd980f1c4af2826012a5d38184b5.mov',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/4da12444e8aa4f018abcacd8f6b779d3.png'
    )
    video19 = Video(
        user_id = 9,
        name = "Cute Kitten",
        description = "Embark on a heartwarming journey as a playful kitten explores the joy of playtime with its favorite toy. Witness the infectious energy and curiosity as it pounces, chases, and swats, completely engrossed in the captivating world of its imagination. Delight in the adorable antics, soft purrs, and adorable expressions that will melt your heart. Join us in this endearing moment that reminds us of the simple pleasures and boundless happiness found in the companionship of a furry friend.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/c3ab279f96e842bd9892db8e53db3a58.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/35154e019bd4400fbb579c3ed3d98f63.png	'
    )
    video20 = Video(
        user_id = 10,
        name = "Helicopter Touches Down with Precision",
        description = "Experience the awe-inspiring sight as a helicopter gracefully lands, showcasing the skill and precision of the pilot. Witness the powerful rotors slow down, creating a mesmerizing display of motion. Feel the excitement in the air as the aircraft gently touches the ground, its landing gear absorbing the impact with ease. Join us in this thrilling moment of aviation as we witness the seamless combination of technology and human expertise, resulting in a safe and controlled descent.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/b5546034bba64ce7ab87ec0380260a9b.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/ac2ba8ff2f264aea875ca037a162f3ee.png'
    )
    video21 = Video(
        user_id = 1,
        name = "Flavors on Fire: Culinary Delights on the Flat Top Grill",
        description = "Indulge in the sizzling artistry as a skilled chef takes command of a flat top grill, transforming ingredients into mouthwatering creations. Watch in awe as the flames dance beneath the sizzling surface, infusing tantalizing flavors into every dish. Experience the tantalizing aromas and the sizzling symphony of ingredients as they come to life under the expert hands of the culinary maestro. Join us for a culinary journey that will ignite your taste buds and leave you craving for more.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/360f5f3a2a23488fabffed22d5d76597.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/b5e0fdc442d84e2f8e3d29384d439794.png'
    )
    video22 = Video(
        user_id = 4,
        name = "Masterful Pizza Tossing Demonstration",
        description = "Step into the world of pizza perfection as a skilled individual showcases their artistry by tossing the dough effortlessly into the air. Witness the seamless rhythm and precision as the dough gracefully spins and twirls, transforming into the foundation of a delicious pizza. Feel the anticipation build as each toss adds a touch of flair and expertise to the culinary spectacle. Join us in this mesmerizing display of pizza-making prowess that will leave you craving a slice of the delectable creation.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/f5ec5b471f4e40d59aee98df4767bb31.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/310babb09d2d475a8112647bf49616d2.png'
    )
    video23 = Video(
        user_id = 8,
        name = "Golden Crisp: French Fries Sizzling in Hot Oil",
        description = "Indulge in the mouthwatering aroma as freshly cut French fries are submerged into a bubbling bath of hot oil. Observe as the humble potato slices undergo a magical transformation, turning into golden delights. Hear the gentle sizzle and witness the gradual browning, as the fries develop a tantalizing crispy texture. Join us in this delectable culinary experience as we celebrate the irresistible allure of perfectly cooked French fries, offering a delightful balance of crispy exterior and fluffy interior.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/893a81fc2d2f48caa6de9777766a386a.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/d0609e1a130a417b97cfc0f550218a6f.png'
    )
    video24 = Video(
        user_id = 9,
        name = "Cars Navigate Mountain Roads",
        description = "Embark on a scenic journey as cars gracefully navigate a snow-covered mountain road, carving their way through a winter wonderland. Witness the breathtaking vistas and pristine white landscapes as these vehicles conquer the challenging terrain. Feel the tranquility of the snowy mountains as the tires grip the road and the engines hum in harmony with nature. Join us in this captivating spectacle of winter driving, where adventure and serenity blend in perfect harmony.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/d97d3c5d6b514c51974621bb7b522dc6.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/6e5a9ceb54344364aad13c6f8555024f.png'
    )
    video25 = Video(
        user_id = 9,
        name = "Illuminating Fireworks Show",
        description = "Prepare to be mesmerized as a dazzling fireworks display lights up the night sky, painting it with vibrant colors and patterns. Witness the explosive beauty as each firework bursts into a shower of shimmering lights, creating a symphony of awe-inspiring visual splendor. Feel the anticipation build with each crackling sound and be captivated by the breathtaking choreography of the sparkling spectacle above. Join us in this magical celebration that ignites the sky and fills hearts with wonder and joy.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/d40c5abad1d144128da627bb4f7aee47.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/4e4bf994bdc34a57a11884db6e74aeb0.png'
    )
    video26 = Video(
        user_id = 2,
        name = "Street Food Stand's Flavorful Meat Skewers",
        description = "Delight in the aromatic symphony as succulent pieces of meat are skewered and expertly grilled at a vibrant street food stand. Witness the sizzle and the tantalizing scents that fill the air, drawing you closer to this delectable display of culinary expertise. Feel your taste buds awaken as the meats cook to perfection, creating a symphony of flavors. Join us in this savory experience as we indulge in the mouthwatering delights served hot off the grill, a true street food sensation.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/dfaf88bcaa864954a3e55c274bd24f25.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/34d5f78c7ee74535b886ae6869e097ed.png'
    )
    video27 = Video(
        user_id = 3,
        name = 'Man Dances and Cheers Happily After Graduating From App Academy',
        description = "He must've just debugged his last modal",
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/3dbf7419fd264a129e4c652f28f527f6.png'
    )
    video28 = Video(
        user_id = 4,
        name = "Productivity Hub: Dynamic Open Office Space",
        description = "Step into a buzzing hive of activity as you enter a bustling open office space. Witness the seamless collaboration and energy as colleagues interact, brainstorm, and bring ideas to life. Feel the vibrant atmosphere that fosters creativity and productivity, where innovation flourishes amidst the shared workspace. Join us in this dynamic environment where work and inspiration intertwine, creating a hub of growth and professional excellence.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/ca461cc293784dea85badf2b2e22b9f3.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/68bd83eb2bf2462fa4d88a9c5b70a718.png'
    )
    video29 = Video(
        user_id = 4,
        name = "Captivating Sunset from an Airplane",
        description = "Gaze out the window of an airplane and behold a mesmerizing sunset painting the sky with a kaleidoscope of vibrant hues. Witness the sun's warm embrace as it sinks below the horizon, casting a golden glow that dances on the clouds. Feel a sense of awe and serenity as you soar through the air, surrounded by the ethereal beauty of nature's masterpiece. Join us in this enchanting moment where the boundary between earth and sky fades, leaving you in pure admiration of the captivating sunset spectacle.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/1a8f7e61732e4d0292f4c8f596d6e74e.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/71bcf8ca052248af8a6dc98437f81860.png'
    )
    video30 = Video(
        user_id = 7,
        name = "Dusk's Urban Symphony: Bustling City Street Alive",
        description = "Immerse yourself in the vibrant energy of a bustling city street as dusk descends. Witness the captivating transformation as the city comes alive with flickering lights and the hum of activity. Feel the rhythm of the urban symphony as pedestrians rush by, cars navigate the streets, and the city's pulse beats in harmony. Join us in this enchanting scene where the dynamic cityscape at dusk casts a spell, inviting you to explore its hidden corners and embrace the excitement that lingers in the air.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/2b596da4e9f8439ebf5cb618004ee93e.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/438e939346634848b64eb58eb56e12d1.png'
    )
    video31 = Video(
        user_id = 9,
        name = "Times Square's Enchanting Night Shower",
        description = "Step into the enchanting realm of Times Square at night, where the city's vibrant energy meets the gentle touch of raindrops. Witness the mesmerizing dance of rain as it cascades down, creating a shimmering spectacle against the backdrop of dazzling lights. Feel the electric atmosphere intensify as umbrellas emerge, and the cityscape reflects on the glistening pavement. Join us in this unique moment where the allure of Times Square meets the whimsy of rainfall, offering a captivating blend of urban charm and nature's own symphony.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/2a03182a723b44c398d0cec00e9579bd.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/c43aae32c3004032a3218f07d4520d3c.png'
    )
    video32 = Video(
        user_id = 10,
        name = "Submerged Swimmer Shows Form",
        description = "Dive into the serene depths as an underwater camera captures the elegant movements of a man swimming. Witness the grace and fluidity as he glides through the water, surrounded by the tranquil blue hues. Feel the weightlessness and the soothing embrace of the underwater world as he explores this ethereal domain. Join us in this immersive experience where the boundaries between land and sea fade away, offering a glimpse into the captivating beauty and freedom found beneath the surface.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/7df2dd09f02d46c78adaa19942dd4f57.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/267175c98e584f178da3b03e3c38c69d.png'
    )
    video33 = Video(
        user_id = 8,
        name = "Foot Traffic Along the Beachfront",
        description = "Take a leisurely walk along the beachfront and immerse yourself in the lively foot traffic that paints a vibrant scene. Witness the ebb and flow of people as they stroll, jog, and engage in beachside activities. Feel the warmth of the sun on your skin and the refreshing breeze from the ocean as you join this vibrant tapestry of beachgoers. Join us in this captivating coastal experience, where the carefree ambiance and the rhythmic sound of crashing waves create a delightful symphony of seaside joy.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/77e6d16460ec4725a56ef7a5c13488b6.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/c63cd0f851b4445794316cd5d3154a05.png'
    )
    video34 = Video(
        user_id = 1,
        name = "Artful Presentation at a Restaurant",
        description = "Indulge in a culinary masterpiece as a succulent chicken dish is meticulously plated at a renowned restaurant. Witness the chef's artistry unfold as every element is carefully arranged with precision and creativity. Admire the vibrant colors, enticing aromas, and the perfect harmony of flavors that grace the plate. Join us in this gastronomic journey where the combination of culinary expertise and impeccable presentation elevates the humble chicken into a gourmet delight, enticing both the eyes and the taste buds.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/976f345fe40d4c43ae40bf611db8fd36.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/3bbc5bc7cd854ca284a68bb15b3e1654.png'
    )
    video35 = Video(
        user_id = 3,
        name = "Omelette Flipping Mastery",
        description = "Enter the world of culinary finesse as a skilled chef effortlessly flips an omelette with mastery. Witness the swift motion and impeccable timing as the delicate omelette soars through the air and lands back in the pan with grace. Feel the anticipation build as the omelette transforms into a fluffy creation, filled with delectable ingredients. Join us in this mesmerizing display of culinary skill, where the art of omelette flipping takes center stage, showcasing the harmonious blend of technique and creativity in the world of cooking.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/7893acd551b24bb3b781a242a106bc34.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/b601d4e7534640e89e51284f03cfbdbf.png'
    )
    video36 = Video(
        user_id = 4,
        name = "Aerial Thrills: Hang Gliders Soaring over the Landscapes",
        description = "Experience the exhilarating adventure as hang gliders take flight, gracefully soaring through the skies above breathtaking lakes and majestic mountains. Witness their daring maneuvers and the freedom they embrace as they navigate the air currents with precision. Feel the rush of adrenaline as they glide effortlessly, offering a bird's-eye view of the stunning landscapes below. Join us in this awe-inspiring spectacle where human courage and the beauty of nature converge, creating a thrilling display that will leave you in awe of the wonders that lie both above and below.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/7c2ffbe17a084aa5a20a7271c1f0e422.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/3309a9d45a97402690cc62e9b38cc41c.png'
    )
    video37 = Video(
        user_id = 6,
        name = "Serene Family of Deer in the Snow",
        description = "Enter a tranquil winter scene as a family of deer gracefully moves through a snowy landscape. Witness the elegance and beauty of these majestic creatures as they navigate the pristine white surroundings with gentle steps. Feel the hushed silence and the crisp air that envelops this serene winter wonderland. Join us in this heartwarming moment where the bond of family and the harmony of nature unfold, leaving an indelible impression of peace and tranquility in the midst of the snowy wilderness.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/b1bd516bc8994401920a34666a71f39f.mp4',
        content = 'http://capstone-video-bucket.s3.amazonaws.com/529366187cea43799c8dea39c78f16d0.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/fd1836bb5beb4145b8896c3a54bca2cf.png'
    )
    video38 = Video(
        user_id = 4,
        name = 'Middle Earth, But If The Year Was 2023',
        description = "Embark on a breathtaking aerial expedition over a landscape reminiscent of Middle Earth, yet firmly rooted in the year 2023. Marvel at the rolling hills, winding rivers, and majestic mountains that seem straight out of a fantastical realm. Experience the fusion of nature's beauty with contemporary civilization as modern structures coexist harmoniously with the picturesque scenery. Join us in this awe-inspiring journey where imagination and reality intertwine, offering a glimpse into a world that captures the spirit of Middle Earth while firmly anchored in the present day.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/b1bd516bc8994401920a34666a71f39f.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/b732d4cac9d84ef5b9ad088c48925366.png'
    )
    video39 = Video(
        user_id = 9,
        name = "Nature's Symphony: Majestic Waterfall in the Rainforest",
        description = "Immerse yourself in the enchanting allure of a rainforest waterfall, where nature's symphony plays out in harmonious beauty. Witness the cascading waters as they plunge into a crystal-clear pool, surrounded by lush greenery and vibrant flora. Feel the refreshing mist on your skin and the gentle roar of the waterfall that resonates through the dense foliage. Join us in this mesmerizing spectacle of nature's power and serenity, where the rainforest's captivating waterfall invites you to experience the sublime connection between earth, water, and life itself.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/5bc95f8e55d4475f8b3f653acf9bf1f2.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/414706e913fb4210952e49f6078ac46a.png'
    )
    video40 = Video(
        user_id = 6,
        name = "Thrills of the Wild: First-Person Motorcycle Adventure through Forest Trails",
        description = "Experience the exhilarating rush of riding a motorcycle through winding forest trails in a thrilling first-person perspective. Immerse yourself in the immersive journey as you navigate the dense foliage, feeling the wind on your face and the rumble of the engine beneath you. Witness the beauty of nature up close as you weave through towering trees and conquer challenging terrain. Join us in this adrenaline-fueled adventure through the untamed wilderness, where the thrill of the ride and the splendor of the forest combine for an unforgettable experience of speed, freedom, and natural beauty.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/4e38fe8160524fe7a5c19d482d36701f.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/6544443bea544a98b0c27473eabbdf10.png'
    )
    video41 = Video(
        user_id = 2,
        name = "Vibrant Yellow Fish in the Ocean's Depths",
        description = "Dive into the mesmerizing depths of the ocean and encounter a captivating sight—a vibrant yellow fish gracefully gliding through the azure waters. Witness its vibrant hues that shimmer and reflect the sunlight, adding a touch of brilliance to the underwater realm. Feel the tranquility and awe as you observe this elegant creature in its natural habitat, surrounded by the mesmerizing beauty of the ocean. Join us in this enchanting encounter where nature's palette comes alive, showcasing the diversity and vibrant charm that exists beneath the waves.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/5c90dacdfb2f4e6f999dd259c962e861.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/b96daebb389f49a49a4ffc12e5f9fdd0.png'
    )
    video42 = Video(
        user_id = 3,
        name = "Rhythm Revolution",
        description = "Join the ultimate dance party that ignites the night with pulsating beats and infectious energy. Step into a world where the music takes control and bodies move in perfect harmony. Feel the exhilaration as the DJ spins electrifying tracks, setting the dance floor ablaze with vibrant lights and an atmosphere of pure euphoria. Join us in this unforgettable celebration of music and movement, where strangers become friends and the dance floor becomes a stage for freedom and self-expression. Let the rhythm guide you and unleash your inner dancer in this unforgettable dance party experience.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/4862034f6d804454b3fe6538018bdb64.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/f480677d63fe4eb4a084e413d771aa92.png'
    )
    video43 = Video(
        user_id = 5,
        name = "Tranquil Beauty of a Beach at Dusk",
        description = "Witness the enchanting spectacle of a sunset on a serene beach, as the golden orb dips below the horizon, painting the sky with hues of orange, pink, and purple. Feel the gentle breeze caress your skin and the soft sand beneath your feet as you bask in the tranquil beauty of this idyllic moment. Join us in this breathtaking experience where time slows down, and the symphony of crashing waves provides the soundtrack to a peaceful evening on the shore. Let the mesmerizing colors and soothing ambiance of the sunset embrace your senses and create lasting memories.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/c3bd5c6821d640d6a587c83c19205edf.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/7dd0b59853e84168a1bfba97bca0dd56.png'
    )
    video44 = Video(
        user_id = 6,
        name = "Winter Escape: Aerial Journey through a Snowy Forest Drive",
        description = "Embark on a mesmerizing aerial adventure as you soar above a snow-covered forest, capturing the enchanting sight of a car gracefully navigating its way through the wintry wonderland. Witness the pristine white landscape adorned with glistening snow-laden trees, creating a picturesque scene straight out of a winter fairy tale. Feel the sense of tranquility and adventure as the car leaves tracks behind, forging a path through the untouched beauty of the snowy forest. Join us in this captivating experience where nature's splendor and the thrill of the open road converge, offering a breathtaking perspective of winter's magic.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/37900192df784e08831e0ef724e68a3c.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/ff585e7cc02041d98f47a993691da2b9.png'
    )
    video45 = Video(
        user_id = 7,
        name = "Sandy Paws",
        description = "Join us on a delightful journey to the beach, where a playful puppy discovers the joys of sand and surf. Watch as the adorable furry friend frolics along the shore, chasing waves and digging in the soft sand. Feel the warmth of the sun and the salty breeze as you witness the pure bliss and infectious energy of the puppy's beachside escapades. Join us in this heartwarming experience where the carefree spirit of a puppy and the beauty of the beach combine, creating an unforgettable moment of pure joy and happiness.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/bfb2b03c9f99432aa79166d6a47da303.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/1b9353d76d504a8cb8c564bbd5fc73e1.png'
    )
    video46 = Video(
        user_id = 8,
        name = "Sushi Symphony",
        description = "Indulge your senses in a tantalizing display of sushi artistry at a renowned restaurant. Feast your eyes on an exquisite assortment of colorful and meticulously crafted sushi rolls, nigiri, and sashimi. Admire the vibrant presentation, the precision of knife work, and the intricate details that showcase the culinary mastery behind each piece. Join us in this culinary journey where the fusion of flavors, textures, and aesthetics elevate sushi to an art form. Immerse yourself in the captivating beauty and mouthwatering allure of this visual feast that celebrates the rich traditions of Japanese cuisine.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/ac222daaf9444481a39999e03504fbdb.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/09c97398a3f74f938ceabd282074c2aa.png'
    )
    video47 = Video(
        user_id = 9,
        name = "Underwater Snorkelers",
        description = "Dive into an enchanting underwater world as you witness a captivating sight—an underneath view of two snorkelers exploring the mesmerizing depths of the ocean. Observe their graceful movements and the vibrant hues of their snorkeling gear against the backdrop of the azure waters. Feel the sense of wonder and serenity as you immerse yourself in this tranquil underwater realm, where marine life thrives and secrets unfold. Join us in this mesmerizing encounter where the beauty of the ocean unveils itself from a unique perspective, offering a glimpse into the captivating world that lies beneath the surface.",
        content = 'http://capstone-video-bucket.s3.amazonaws.com/7c185cd2c7074c28b8033c4e6600ec2a.mp4',
        thumbnail = 'http://capstone-image-bucket2.s3.amazonaws.com/ad86831e6a6549939ae154d66054ea86.png'
    )
    video48 = Video(
        user_id = 2,
        name = "Aerial View of Skier Behind a Boat",
        description = "Experience the exhilaration of water skiing from a bird's-eye perspective as an aerial shot captures the thrilling moment of a skier being pulled behind a boat. Witness the skier gliding effortlessly across the shimmering surface of the water, leaving trails of excitement in their wake. Feel the rush of adrenaline as they navigate the waves and perform impressive maneuvers. Join us in this adrenaline-fueled adventure where the synergy between human skill, water, and speed creates an electrifying spectacle. Get ready to be captivated by the thrill and beauty of water skiing from an awe-inspiring aerial viewpoint.",
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
