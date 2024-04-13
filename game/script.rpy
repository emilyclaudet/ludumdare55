define e = Character("Eileen")


label start:
    $ playername = renpy.input("What is your name?", default = "Jennifer")
    $ playername = playername.strip()
    if playername == "":
        $ playername = "Jennifer"
    "The story starts in a cozy student shared house..."
    "Where our hero [playername] must learn to survive."
    jump story

label story:
    call intro

    scene bg room
    show eileen happy

    e "You've created a new Ren'Py game."
    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
