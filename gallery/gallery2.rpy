init python:
    gal = Gallery()
    gal.locked_button = "gallery/locked.png"
    gal.button("firstimg")
    gal.condition("persistent.gallery1")
    gal.image("bar.jpg")

    gal.button("secondimg")
    gal.condition("persistent.gallery2")
    gal.image("bar.jpg")

    gal.button("thirdimg")
    gal.condition("persistent.gallery3")
    gal.image("bar.jpg")

    gal.button("fourthimg")
    gal.condition("persistent.gallery4")
    gal.image("bar.jpg")

    gal.button("fifthimg")
    gal.condition("persistent.gallery5")
    gal.image("bar.jpg")

    gal.button("sixthimg")
    gal.condition("persistent.gallery6")
    gal.image("bar.jpg")


screen gallery2:
    tag menu
    add "background/brickwall.png"

    grid 4 2:

        xalign 0.5
        yalign 0.5
        #xpadding 10
        #xfill True
        #yfill True

        add gal.make_button("firstimg", "locked.png")
        add gal.make_button("secondimg", "locked.png")
        add gal.make_button("thirdimg", "locked.png")
        add gal.make_button("fourthimg", "locked.png")
        add gal.make_button("fifthimg", "locked.png")
        add gal.make_button("sixthimg", "locked.png")
        add gal.make_button("fifthimg", "locked.png")
        add gal.make_button("sixthimg", "locked.png")
        

         #,xpos =20, ypos=0)



    textbutton "return":
        action Return()
        xalign 0.36
        yalign 0.95


    textbutton "previous page":
        action Jump("gallery")
        xalign 0.55
        yalign 0.95
label gallery:
    call screen gallery
