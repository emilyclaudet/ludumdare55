﻿label start:
    $ player = renpy.input("What is your name?", default = "Traynor")
    $ player = player.strip()
    if player == "":
        $ player = "Traynor"
    jump chapter1

label story:
    call intro

    return
