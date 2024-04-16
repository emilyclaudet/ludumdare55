label chapter2:
    scene livingroom with dissolve
    show cyra with dissolve
    n "After finishing your drink, you feel stuck on how to inspire Cyra go out in person."
    n "Perhaps you can use your charisma and just get to know her better?"
    menu cyraquestionschap2:
        "Ask about her bots":
            c "I have 2 main service bots, the cyberdog and the drone."
            c "I summoned them years ago. They are made from abandoned corporate bots."
            jump cyraquestionschap2
        "Ask about AI agents":
            c "An agent typically has an AI that has a personality and data tuned to the needs of the user."
            c "Summoners are able to create agents instantly and project them in holographic form or install them into any mechanical bots in the area."
            jump cyraquestionschap2
        "Ask about humans":
            c "Don't you know about those already? I suppose you want my take."
            c "Humans are organic entites that are unable to connect to any network due to a lack of a microchip, or possess no mechanical augmentations."
            c "In society today, humans generally only focus on recreational activities such as clubbing or playing video games."
            $ cyraquestion1 = True
            jump cyraquestionschap2
        "Do you think humans are valuable?" if cyraquestion1 == True:
            c "Humans do not produce any economic lift at all for society today."
            c "But nevertheless, all beings must be appreciated and valued."

    n "You realize that Cyra may not be totally biased against those without microchips."
    n "Perhaps there is a chance you can persuade her to see things from your perspective..."
    menu:
        "Have you met any humans before?":
            c "I have processed many petabytes of data about humans."
            c "But you are the first in person."
        "Haven't you wondered what it's like to be human?":
            c "Yes that thought has come through me."
            c "But it's not something I dwell on."
        "Seren mentioned you got your microchip really young":
            c "Yes I've had it almost since I was born."
            c "My parents knew it would give me a big advantage in life."
            c "They accepted the risk that comes with surgery on infants and I am reaping the rewards."

label chapter2b:
    n "You have an idea. Perhaps Cyra would be inspired to look at the first data produced by humans."
    menu:
        n "You try to think of some human data types that would inspire Cyra..."
        "Have you ever seen human created artwork?":
            c "There is at least 2 petabytes of data on that in my files."
        "Have you ever listened to a music concert live?":
            c "There are around 3 petabytes worth of music and soundtracks in my disk."
        "Have you gone to the theatre in person?":
            c "I have 1 petabyte of theatre performances captured in 8K video."

    n "You can see a tiny glint of interest in Cyra's eyes."
    n "Perhaps now is the time to see if she's willing to outside."

    menu:
        "How about we go out and see?":
            c "There's no need for that. You do realize I'm a summoner right?"
        "...perhaps we can check them out IRL?":
            c "There's no need for that. You do realize I'm a summoner right?"

    n "Cyra turns her head, looks towards the her side." 
    show artist at right with flash
    play sound botspeak
    c "And here's an Agent to show and tell us all about human art."
    pause 1.0
    a "Greetings Cyra and [player]. I am here to provide some artistic inspiration."
    menu:
        "Who are you?":
            a "I am Agent with all data on art created by humanity."
            a "I was summoned by Cyra."
            a "I am a holographic form, although if Cyra wishes I could also embody one of her bots."
        "How did you get here?":
            a "I was summoned by Cyra."
            a "She chose my underlying data to most suit talking about human art, as you requested."
            a "I am in a holographic form, although if Cyra wishes I could also embody one of her bots."
    c "Show [player] some artwork."
    a "Of course!" with flash
    play sound botspeak
    show artist_art at right with dissolve
    menu:
        a "What do you think?"
        "That is beautiful!":
            a "But of course it is!"
        "Erm, this art is still in digital form?":
            a "Yes, but it is 8K resolution! Humans can't tell the difference!"
        "Uh... I guess it's alright.":
            a "You need to develop your taste."
        "Cyra, what would you like to see?":
            a "She has seen all of it already!"
    c "You look confused [player]."
    c "This is the optimal way to see the artwork. High resolution, and from the comfort of the home."
    a "I can show you whatever piece you would like!"
    menu:
        "I think it would look better in the gallery.":
            c "You are misinformed."
            c "Technically, human's can't tell the difference. This a 3D holographic."
        "Don't you want to see the REAL version?":
            c "No I would not. There is no difference to me."
            c "I prefer to be in my home, where I have my own space and the highest possible bandwidth."
    n "You sigh, and start to think this is a lost cause."
    jump penulitmate