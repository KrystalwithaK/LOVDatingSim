init python:
    g = Gallery()
    g.locked_button = "gallery/locked.png"
    g.button("gen1")
    g.condition("persistent.genend1")
    g.image("gallery/shiggy/shiggycg1.png")

    g.button("secondimg")
    g.condition("persistent.gallery2")
    g.image("gal2.png")

    g.button("thirdimg")
    g.condition("persistent.gallery3")
    g.image("gal3.png")

    g.button("fourthimg")
    g.condition("persistent.gallery3")
    g.image("gal4.png")

    g.button("fifthimg")
    g.condition("persistent.gallery3")
    g.image("gal1.png")

    g.button("sixthimg")
    g.condition("persistent.gallery3")
    g.image("gal1.png")


screen gallery:
    tag menu
    add "background/brickwall.png"
    grid 3 2:
        xalign 0.5
        yalign 0.5

        add g.make_button("gen1", "gallery/gal1small.png")
        add g.make_button("secondimg", "gal2small.png")
        add g.make_button("thirdimg", "gal3small.png")
        add g.make_button("fourthimg", "gal4small.png")
        add g.make_button("fifthimg", "gal1small.png")
        add g.make_button("sixthimg", "gal1small.png")



    textbutton "return":
        action Return()
        xalign 0.36
        yalign 0.95


    textbutton "next page":
        action Jump("gallery2")
        xalign 0.55
        yalign 0.95
label gallery2:
    call screen gallery2