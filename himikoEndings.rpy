init python:
    g=Gallery()
    g.button("questionmark")
    g.image("questionmark")




screen himikoEndings:
    add "black"
    add "questionmark"
    add "questionmark"
    text "this is the page for himiko's endings"


    textbutton "return":
        action Jump("endings")
        xalign 0.5
        yalign 0.95
