init python:
    g=Gallery()
    g.button("dabi")
    g.image("dabi")


screen gallery:
    tag menu

    add "dabi"

    textbutton "return":
        action Return()
        xalign 0.5
        yalign 0.95
