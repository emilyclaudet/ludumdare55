define e = Character("Eileen")


label start:
    $ player = renpy.input("What is your name?", default = "Traynor")
    $ player = player.strip()
    if player == "":
        $ player = "Traynor"
    jump story

label story:
    call intro

    return
