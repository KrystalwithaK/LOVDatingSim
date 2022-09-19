label credits:
    call screen credits
screen credits:
    tag menu
    add "black"

    text "Coders":
        xalign 0.5
        yalign 0.1

    text "Writers":
        xalign 0.5
        yalign 0.3

    text "Artists":
        xalign 0.5
        yalign 0.5

    textbutton "return":
        action Return()
        xalign 0.5
        yalign 0.95
