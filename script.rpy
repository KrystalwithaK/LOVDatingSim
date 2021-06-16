# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Tomura", color="#b1f2fc")
define d = Character("Dabi", color = "#8826f7")
define h = Character("Himiko", color = "#e33d4e")
define s = Character("Spinner", color = "#40a832")
define tw = Character("Twice", color = "#787878")
define mr = Character("Mister Compress", color = "#ba902f")
define k = Character("Kurogiri", color = "#2b1e42")
define g = Character("Giran", color = "#c796f2")


# Secret characters
define ha = Character("Hawks", color = "#ffe23d")
define st = Character("Stain", color = "#bf2626")



image shigaraki1 = im.FactorScale("shigaraki1.png", 0.85)
image dabi = im.FactorScale("dabi.png", 1.25)

# The game starts here.
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


    scene bar

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

#if high enough affection you can get their quirk with a copying quirk?

    #"You wander into a dilapidated bar"
    "The plain, wooden door squeaks loudly as Giran casually swings it open.
    Thing probably hasn’t been oiled in years. The room he leads you into is a bar. It looks far cleaner than you expected."
    "It smells kind of bad..."

    show shigaraki1:
        xalign 0.8


    t "Do you have a quirk?"
    "another man enters the bar." with vpunch
    show dabi:
        xalign 0.4
        linear 0.5 xalign 0.1


    menu:
        "Asking right off the bat, huh? Guess he doesn't waste time."

        "Yes":
            jump quirk


        "No":
            jump noQuirk


label quirk:

    t "Good. You will be useful to us."
    $ affectionTomura += 1
    jump secondQuestion

label noQuirk:

    t"Unfortunate. We can give you a quirk if you prove yourself."

    jump secondQuestion


label secondQuestion:
    t "Why do you want to join the league?"
    menu:


        "I want to continue Stain's work":
            jump stain

        "I hate hero society":
            jump hateHero

label stain:
    t"Fuck off."
    jump dabiRoute
    return


label hateHero:
    t"Good."
    $ affectionTomura += 1
    if persistent.ending == "Ending 1":
        t"Damn, you're cute."
    jump shigarakiRoute

    return

label back:
    t "....kith?"

    return
