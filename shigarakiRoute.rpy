label shigarakiRoute:
    t "Wow, I've never felt like this about someone before."
    if affectionTomura == 2:
        t "I really like you."

    $ persistent.ending = "Ending 1"
    jump back
    return
