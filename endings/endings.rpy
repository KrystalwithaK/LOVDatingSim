label endings:
    call screen endings
screen endings:
    tag menu
    image "wall.png"

    hbox:
        yalign 0.1
        xalign 0.5
        imagebutton:
            idle "chibi toga.png"
            hover "chibi toga hover.png"
            action Jump("himikoEndings")
        imagebutton:
            idle "chibi shiggy.png"
            hover "chibi shiggy hover.png"
            action Jump("shigEndings")

        imagebutton:
            idle "chibi dabi.png"
            hover "chibi dabi hover.png"
            action Jump("dabiEndings")

        imagebutton:
            idle "chibi spinner.png"
            hover "chibi spinner hover.png"
            action Jump("spinnerEndings")


    hbox:
        xalign 0.5
        yalign 0.8
        imagebutton:
            idle "chibi twice.png"
            hover "chibi twice hover.png"
            action Jump("twiceEndings")
        imagebutton:
            idle "chibi kurogiri.png"
            hover "chibi kurogiri hover.png"
            action Jump("kurogiriEndings")
        imagebutton:
            idle "chibi compress.png"
            hover "chibi compress hover.png"
            action Jump("mrEndings")

        imagebutton:
            idle "gen ending.png"
            hover "gen ending hover.png"
            action Jump("genEndings")

    textbutton "return":
        action Return()
        xalign 0.36
        yalign 0.95


    textbutton "next page":
        action Jump("endings2")
        xalign 0.55
        yalign 0.95


label shigEndings:
    call screen shigarakiEndings
label dabiEndings:
    call screen dabiEndings
label himikoEndings:
    call screen himikoEndings
label mrEndings:
    call screen mrEndings
label spinnerEndings:
    call screen spinnerEndings
label twiceEndings:
    call screen twiceEndings
label kurogiriEndings:
    call screen kurogiriEndings
label genEndings:
    call screen genEndings
label endings2:
    call screen endings2
