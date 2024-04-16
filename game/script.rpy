label start:
    $ player = renpy.input("What is your name?", default = "Traynor")
    $ player = player.strip()
    if player == "":
        $ player = "Traynor"
    jump intro

label story:
    call intro from _call_intro

    return
