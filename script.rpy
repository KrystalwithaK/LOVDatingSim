# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define player = Character("[player]")
define t = Character("Tomura", color="#b1f2fc")
define tstranger = Character("Strange Guy", color="#b1f2fc")
define tvstranger = Character("Scratchy Voiced Guy", color="#b1f2fc")
define d = Character("Dabi", color = "#8826f7")
define dvstranger = Character("Deep Voiced Guy", color = "#8826f7")
define h = Character("Himiko", color = "#e33d4e")
define hstranger = Character("Strange Girl", color = "#e33d4e")
define s = Character("Spinner", color = "#40a832")
define sh = Character("Shuichi", color = "#40a832")
define sstranger = Character("Scaly Stranger", color = "#40a832")
define tw = Character("Twice", color = "#787878")
define mr = Character("Mister Compress", color = "#ba902f")
define mrstranger = Character("Strange Gentleman", color = "#ba902f")
define atsu = Character("Atsuhiro", color = "#ba902f")
define k = Character("Kurogiri", color = "#2b1e42")
define gi = Character("Giran", color = "#c796f2")


# Secret characters
define ha = Character("Hawks", color = "#ffe23d")
define st = Character("Stain", color = "#bf2626")


default persistent.gallery1=False
default persistent.genend1 = False

##critical question for each character



image bedroom = "background/bedroom.png"
image thrift = "background/thrift.png"
image bookstore = "background/bookstore.png"
image toga = "sprites/toga.png"
image toga blush = "sprites/toga blush.png"
image alleyday = "background/alleyday.png"
image alleyph = "background/placeholder.png"
image shiggycg1 = "gallery/shiggy/shiggycg1.png"

image genend1screen = "gallery/gen/genend1screen.png"
# The game starts here.




layeredimage himiko:
    attribute back:
        "sprites/himiko/behind.png"
    always:
        "sprites/himiko/h.png"
    group expressions:
        attribute blush:
            "sprites/himiko/h_blush.png"
        attribute sad:
            "sprites/himiko/h_sad.png"


layeredimage shiggy:
    always:
        "sprites/tomura/t.png"
    group expressions:
        attribute blush:
            "sprites/tomura/t_blush.png"
        attribute sad:
            "sprites/tomura/t.png"

layeredimage spinner:
    always:
        "sprites/spinner/sp.png"
    group expressions:
        attribute blush:
            "sprites/spinner/sp.png"
        attribute sad:
            "sprites/spinner/sp.png"
layeredimage mister:
    attribute back:
        "sprites/himiko/behind.png"
    always:
        "sprites/compress/mr.png"
    group expressions:
        attribute blush:
            "sprites/himiko/h_blush.png"
        attribute sad:
            "sprites/himiko/h_sad.png"

label splashscreen:

    scene black
    show text "Warning: this game contains themes of rape, murder, gore, toxic behavior, and more. You must be 18 or older to play."
    with fade
    pause
    return

label start:

    $ affectionTomura = 0
    $ affectionDabi = 0
    $ affectionHimiko = 0
    $ affectionSpinner = 0
    $ affectionTwice = 0
    $ affectionMister = 0
    $ affectionKurogiri = 0
    $ affectionGiran = 0

    $ affectionHawks = 0
    $ affectionStain = 0

    default she = "she"
    default her = "her"
    default herself = "herself"


    scene bedroom
    $player = renpy.input("What is your name?", length=22)

    menu:
        "She":
             $she = "she"
             $her = "her"
             $hers = "hers"
             $herself = "herself"
             #$miss = "miss"

             $She = "She"
             $Her = "Her"
             $Hers = "Hers"
             $Herself = "Herself"
             $Miss = "Miss"

        "He":
            $she = "he"
            $her = "him"
            $his = "his"
            $herself = "himself"

            $She = "He"
            $Her = "Him"
            $Hers = "His"
            $Herself = "Himself"
            $Miss = "Sir"

    player "I finally have a day off! Time to get some chores done. What to do first?"
    menu:
        "pick up necessities from the convenience store":
            jump convenience

        "stop by the bookstore":
            jump bookstore

        "grab some clothes from the thrift store":
            jump thrift

label convenience:
    "I don't want to do a full grocery run, so I'll just pick up a few necessities from the convenience store."
    scene convenience
    "Let's see... what do I want to grab first?"
    menu:
        "energy drinks":
            "It's not the healthiest thing ever, but I'll just get a few so it's fine."
            jump energy

        "skincare":
            "I know they don't sell the best quality stuff here, but I'm almost out of face wash and I just need {i}something.{/i}"
            jump skincare

label energy:
    $ affectionTomura += 10

    "I wander through the drink aisle, looking through the colorful cans."
    "I start piling a few cans into my basket, wondering how many miligrams of caffeine will kill me."
    show shiggy with dissolve:
        xpos 1000
        ypos 110

    "The guy next to me puts five more cans into his basket, which is completely full of energy drinks."
    "The bags under his eyes are even worse than mine. I didn't think there was someone out there who got even less sleep than me."
    player "Damn, do you have a night class or something?"
    "Shit, I said that without even thinking!"
    tstranger "Huh?"
    "He's looking at me. Damnit, I have to say something! I'm too tired for this shit and totally forgot how to social."
    player "Um... uhh..."
    menu:
        "say he's cute":
            jump tcute
        "compliment his shirt":
            jump compshirt
        "say bye and leave":
            jump sorry


label tcute:
    $ affectionTomura += 50
    "Sorry! You're just really cute and my brain just kinda shut down."
    tstranger "..."

    show shiggy blush with dissolve:
        xpos 1000
        ypos 110
    "Really givin' me nothing here, huh?"
    tstranger "..."
    player "Um, sorry. Didn't mean to be weird. I'm gonna go now."
    "Oh god, that was awful. I'm never coming back to this store."
    jump alley


label compshirt:
    "Oh, that's a cool shirt."
    tstranger "..."

    show shiggy blush with dissolve:
        xpos 1000
        ypos 110
    player "Sorry. Was that weird?"
    jump alley



label sorry:
    "Ah, sorry for being weird! Good bye!"
    tstranger "Uh. Ok."
    hide shiggy with dissolve
    "Fuck, that was awkward. I hope it didn't seem rude that I just left."
    jump alley



label skincare:
    "Forgive me, skin, but this will have to do for now."
    "I wander through the skincare aisles, looking for something that isn't {i}too{/i} cheap."
    show spinner
    "I start looking at the brands I like, having to peek around a guy right in front of the section I want to look at."
    "Well, this is awkward."
    "As I consider just reaching around him to grab a product, I hear him muttering to himself."
    sstranger "Damnit, what does any of this shit mean?!"
    player "You okay there?"
    "Part of me wants to help, and part of me wants him to get out of my way."
    sstranger "Uh, do you work here? Yeah I could really use some help."
    "When he turns around, I can see his scaly skin. There's some dried bits hanging off, and most of it looks really rough and dry."
    player "Oh, are you molting?"
    "He looks at me in horror, and tugs his hood over his face."
    player "Sorry! I didn't mean to be rude."
    sstranger "I-it's okay. I know it looks gross."
    "It kinda does."
    player "No, it doesn't! Besides, it's a natural process, right?"
    sstranger "Yeah. I guess."
    player "Let me look up some stuff real quick, I feel like moisturizing
    and gentle exfoliation is probably the way to go, but I don't wanna give you a bad recommendation."
    sstranger "Thanks."
    "I whip out my phone and start looking stuff up. I've helped friends with their skincare in the past, so I feel like I should be able to figure this out."
    sstranger "Um, what's your name? I think you forgot to put on your name tag."
    player "Oh, uh..."
    "I look around sheepishly."
    player "I don't actually work here. But skincare is kind of my thing."
    sstranger "Shit, I'm sorry. I didn't mean to rope you into--"
    player "--No, it's okay! Maybe it's hard to believe, but stuff like this is actually fun to me. I'm [player], by the way."
    sh "Shu-Shuichi."
    jump alley

label bookstore:
    "I haven't been to the book store in a while."
    scene bookstore
    "Let's see... What section should I look at?"
    menu:
        "Manga":
            jump manga

        "Cook Books":
            jump cookbooks

label manga:
    "I head over to the manga section, trying not to let my eyes hover over the more salacious titles for too long. A bunch of school girls are chatting around the more romantic titles, while the school boys are looking at more action centered titles. Many colorful titles line the shelves. I just browse absentmindedly."
    $affectionHimiko += 10
    "My finger traces the spines of different books, hues of pinks and purples blending together as I search for that title."
    player "Aha!"
    "I pull out a pink book, with blood splatter accents all over the cover."
    player "They have the new volume. Sweet!"
    show himiko:
        xpos 1000
        ypos 110

    h "I love that series! It's my favorite!"
    player "sdf"

    show himiko blush with dissolve:
        xpos 1000
        ypos 110
    h "you're cute!"

    jump alley


label cookbooks:
    "I head over to look at the cook books, browsing for something that is the right combination of tasty, healthy, and cheap."
    $affectionMister += 10
    "Browsing through budget cooking recipes gets a bit old after a while, so I browse over some of the more extravagant titles. There's no way I have time to try out a fancy French recipe, but the curiosity is killing me."
    player "What the heck is soos vaid?"
    mrstranger "It's actually pronounced 'soo veed.'"
    "I jump, startled by the voice suddenly so close to me."
    show mister with dissolve:
        xpos 1000
        ypos 110
    mrstranger "Ah, pardon me, [Miss]. I didn't mean to frighten you."
    player "Oh, it's okay. You know what this is?"
    mrstranger "I do! In fact, I believe it is the best way to cook steak."

    jump alley



label thrift:
    scene thrift
    "I really need some new clothes. Most of mine are falling apart. Better head to the thrift store."
    "Let's see... Where to start?"
    menu:
        "Look for hoodies":
            jump hoodies

        "Browse tote bags":
            jump bags

label hoodies:
    "This is where the player will meet Dabi"
    $ affectionDabi += 10
    return

label bags:
    "This is where the player will meet Twice"
    $ affectionTwice += 10
    return

label alley:
    scene alleyday
    "I've only gotten one chore done today, but that's kind of all I have energy for. I think I'm gonna head home and take a nap."
    "As I walk, my eyes begin to droop and my head starts to feel heavy. I hardly did anything today but I'm still absolutely pooped."
    "Should I take a shortcut?"
    menu:
        "Yes":
            jump shortcut

        "No":
            jump home


label shortcut:
    "It should be fine to cut through the alleyways real quick. It's daylight out, so it's not a big deal."
    "I wander through the alley, being sure to pay attention to my surroundings."
    "Aside from a rat scurrying around and the occasional employee on a smoke break, it's just me."
    "The bags hanging from my arms start to dig into my elbows, and I speed up to get home quicker."
    tvstranger "--Toga's the best one to do it. She'll need some new blood, though."
    dvstranger "Can we really trust that psycho on a mission like that?"
    "Wow, that's rude. Whoever he's talking about, I bet they're not a psycho."
    "I probably shouldn't be eavesdropping, but those people are having a conversation right around the corner."
    hstranger "Don't say that, Dabi! I'll behave, promise!"
    "...Dabi? That name sounds familiar, but I don't remember where I heard it."
    dvstranger "We need someone calm and stealthy for this mission. You can't be running around and freaking out as soon as someone starts bleeding."
    "Mission? Are these heroes planning out something?"
    hstranger "Aww, but it smells so good~ I can't help myself sometimes."
    "The girl talking giggles. It sounds lighthearted, but given the subject matter it just feels... off."
    tvstranger "Doesn't matter. She's the best fit. God knows you couldn't do it. We need a fresh face, someone the heroes won't recognize."
    "Their voices get closer and closer as I pass the alley they're talking in. Just keep your head down, don't make eye contact as you walk by."
    "Wait... heroes?"
    dvstranger "Shit, keep your voice down!"
    "It's too late to turn around. I'm passing by the alley as the thougth occurs to me."

    scene placeholder
    "They're villains."
    tvstranger "Fuck!"
    "Before I can even blink, there's a man standing in front of me and a hand wrapped around my throat."

    if affectionTomura>=10:
        jump tomurasave

    elif affectionDabi>=10:
        jump dabisave

    elif affectionHimiko>=10:
        jump himikosave

    elif affectionMister>=10:
        jump mistersave

    elif affectionSpinner>=10:
        jump spinnersave

    elif affectionTwice>=10:
        jump twicesave


label tomurasave:
    "I close my eyes, waiting for him to start choking me. I should probably try to fight back, but I'm frozen in place."
    return

label dabisave:
    "dabi saves"
    return

label himikosave:
    "himiko saves"
    return

label mistersave:
    "Just a moment!"
    return

label spinnersave:
    "WAIT!"
    return

label twicesave:
    "twice saves"
    return


label home:
    "Probably better to just stick to the main roads."
    scene bedroom

    if affectionTomura>=10:
        jump shiggystalk

    elif affectionHimiko >=10:
        jump togastalk
    else:
        #if unlocked ending, you come home to someone curled up in  your bed? or shiggy stealing your panties?
        "Ah, home sweet home! Now I can finally take a nap."
        $ persistent.genend1 = True
        scene genend1screen with fade
        pause

        return

label togastalk:
    "Opening the door while juggling all my bags is difficult, but I finally manage to get the damn door open."
    "Once I get through the doorway, I drop my bags haphazardly in the entry way. My arms instantly feel 50 pounds lighter."
    "As soon as I close the door and kick the bags into the kitchen, incessant knocking begins ringing out from my door."
    player "Seriously?"
    "I {i}just{/i} got home. I really don't want to deal with this right now."
    "..."
    "The knocking won't freaking stop!"
    "Do I open the door?"
    menu:
        "Open the door":
            jump opendoor

        "Ignore it":
            jump ignore

        "Look through peephole":
            jump peep




label opendoor:
    "open"
    return

label ignore:
    "Sorry, buddy. I'm tired as hell. Knock till your knuckles bleed, for all I care."
    "{i}BANG{/i}"
    return

label peep:
    "peep"
    return

label shiggystalk:
    "The door handle rattles as I unlock my apartment door, even more than it usually does."
    player "I'm gonna have to call the land lord about this dang thing sometime."
    "I'm too busy setting down my keys and putting away the things I bought to notice my bedroom door is open."
    "There's a soft, rhythmic sound coming from my room as I approach the door."
    scene shiggycg1 with dissolve
    pause
    "What the fuck"
    return
