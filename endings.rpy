screen endings:
    tag menu
    add "black"

    textbutton "Tomura":
        action Jump("shigEndings")
        xalign 0.1
        yalign 0.1

    textbutton "Dabi":
        action Jump("dabiEndings")
        xalign 0.1
        yalign 0.2

    textbutton "Himiko":
        action Jump("himikoEndings")
        xalign 0.1
        yalign 0.3

    textbutton "Kurogiri":
        action Jump("kurogiriEndings")
        xalign 0.1
        yalign 0.4

    textbutton "Spinner":
        action Jump("spinnerEndings")
        xalign 0.1
        yalign 0.5

    textbutton "Twice":
        action Jump("twiceEndings")
        xalign 0.1
        yalign 0.6

    textbutton "Mister Compress":
        action Jump("mrEndings")
        xalign 0.1
        yalign 0.7

    textbutton "return":
        action Return()
        xalign 0.5
        yalign 0.95




label shigEndings:
    call screen shigarakiEndings
label dabiEndings:
    call screen dabiEndings
label himikoEndings:
    call screen himikoEndings
label kurogiriEndings:
    call screen kurogiriEndings
label spinnerEndings:
    call screen spinnerEndings
label twiceEndings:
    call screen twiceEndings
label mrEndings:
    call screen mrEndings
