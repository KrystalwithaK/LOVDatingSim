init python:
    g=Gallery()
    g.button("questionmark")
    g.image("questionmark")




screen genEndings:
    add "background/brickwall.png"
    if (persistent.genend1):
        add "gallery/gen/gen ending1.png"


    textbutton "return":
        action Jump("endings")
        xalign 0.5
        yalign 0.95
