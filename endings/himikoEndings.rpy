init python:
    g=Gallery()
    g.button("questionmark")
    g.image("questionmark")




screen himikoEndings:
    add "togaendingsbg"
    #add "questionmark"
    #add "questionmark"


    textbutton "return":
        action Jump("endings")
        xalign 0.5
        yalign 0.95
