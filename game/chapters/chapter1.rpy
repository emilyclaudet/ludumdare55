label chapter1:
    scene black with dissolve
    n "You head over to Cyra's address a few days later."
    n "You hope that Cyra will be willing to see things from a human perspective."
    scene door with dissolve
    n "You approach the door only to find it's being guarded."
    show bot with dissolve
    play sound botspeak
    b "Good morning [player]."
    b "Welcome to the AI Agents Realm. Cyra's expecting you."
    menu botdog1:
        "Wow you're a dog?":
            b "I am a bot in the form of man's best friend, yes."
            b "Cyra customised me as so."

            jump botdog1
        "She knew I was coming?":
            b "Of course. Your digital footprint couldn't be more hackable."
            b "And well, Seren did give her a heads up."
    b "Before entering, we need do a verification of your identity."
    b "Nothing much, just standard stuff."
    show bot at right with moveinleft
    show drone at top with dissolve
    d "Welcome [player]!"
    d "Please look into the camera and tap your finger on the pad."
    n "You feel uneasy, but you know there's no going around this procedure."
    d "Come now, don't be shy."
    pause 1.0
    play sound confirm
    d "And that's it." with flash
    b "OK, you may enter now."

label chapter1a:
    scene livingroom with dissolve
    show bot with dissolve
    play sound botspeak
    b "Please make yourself at home."
    n "You are tempted to sit on the very comfy looking couch, but first you look for Cyra."
    n "You realize she's sitting on the floor on a plush carpet, looking deep in thought."
    hide bot with dissolve
    show cyra with dissolve
    n "You feel the intensity of signals and data processors as you stare at Cyra."
    menu:
        "Hi Cyra, nice to meet you!":
            jump chapter1b
        "Hey, why are you meditating?":
            jump chapter1b
        "Erm, is that really her?":
            jump chapter1b

label chapter1b:
    show bot at left with dissolve
    play sound botspeak
    b "There is no need to disturb her directly."
    b "She will reply to your queries through us, her agents."
    menu:
        "So you talk for her?":
            b "Yes Cyra sends her thoughts to her agents through the network."
            b "I can communicate on her behalf, as can any other bot that she links to."
        "Can you tell Cyra to talk to me directly?":
            b "She does not wish to engage. Her mind is focused on other things."

    n "You feel frustrated, and you realize why Seren was willing to pay you to get her to go out."
    menu chapter1bmenu:
        "Can you ask Cyra if she'll come to Seren's birthday party?":
            b "Cyra has already replied to the invitation."
        "Hey Cyra, don't you want to attend the birthday party?":
            b "Cyra has already replied to the invitation."
        "Try tapping Cyra on the shoulder":
            b "HALT! You cannot approach her." with vpunch
            jump chapter1bmenu
    b "Cyra will attend the party remotely."
    show drone at topright with dissolve
    play sound botspeak
    d "That's right! She can dial in and view it in VR."
    d "Seren has great camera and good streaming, we know it will be high quality enough for Cyra."
    d "What's the point in going?"

    menu:
        "Seren wants to see her":
            d "Cyra knows this. She appreciates the invitation to celebrate the birthday."
            b "We will broadcast the highest quality footage of Cyra to the event."
            d "Humans cannot tell the difference between reality and VR. It truly is the same thing."
        "It's not the same!":
            d "There have been various studies dating back to the 2150s."
            d "Humans cannot tell the difference between reality and VR."
            b "And remember, Cyra is a cyborg who is very in tune with the digital world."
    c "[player]..."
    n "The bots freeze and fall into deep silence, giving space for Cyra's voice to faintly echo through the room."
    n "You immediately turn to look deeply into Cyra's sparkling eyes."
    hide bot with dissolve
    hide drone with dissolve
    show cyra with dissolve 
    c "I know it's hard for you to understand why I don't feel the need to be there in person."
    c "It seems your microchip really has malfunctioned and you are fully human now. Is that correct?"
    menu:
        "Yes.":
            c "You are a unique person."
            jump cyraquestions
        "That's right, I'm basically a human now.":
            c "There are not many like you."
            jump cyraquestions
    menu cyraquestions:
        "Great you're finally talking to me directly.":
            c "I know it's bad social etiquette to not use my human voice."
            c "I can handle my other tasks in parallel, but it does lower my efficiency slightly."
            c "But it is unique that you were a cyborg and are now surviving with purely human skills."
            c "I can see why Seren wanted you to visit me."
        "How do you feel talking to a mere human?":
            c "It made me think about all the inputs you can't process because you lack a working microchip."
            c "But otherwise it is fine. I'm only using a fraction of my resources to maintain this conversation."
            c "It is unique that you were a cyborg and are now surviving with purely human skills."
            c "I can see why Seren wanted you to visit me."
        "Do you think humans are stupid?":
            c "Well objectively, they do have less capabilities than cyborgs."
            c "But no matter what, you can't deny that the first training data originated from humans 2 centries ago."
            c "That's what all technology experts are taught, and even my grandmother knew and talked about this."
            c "I can see why Seren wanted you to visit me."
    c "There's no need to keep telling me about Seren's party."
    n "You know you can't give up. There must be something that could suggest her to leave the house."
    menu cyraquestions2:
        n "You brainstorm ideas to inspire Cyra to go out..."
        "Offer to take her out for a coffee.":
            c "There's no need for that. We can get some delivered."
            c "Do you want a coffee? I prefer matcha."
            show drone at topright with dissolve
            play sound botspeak
            n "The drone appears suddenely, and the window slides open."
            show drone at offscreenright with moveinright
        "Suggest to go for a walk in the park.":
            c "I already did my exercise this morning."
            n "Cyra nods her head in the direction of a running machine set up in another room."
            n "You sense there's no persuading her this way."
            jump cyraquestions2
        "Talk about Seren's party":
            c "I already told you, I am fully committed to dialling in live."
            c "I will be present for Seren's party."
            jump cyraquestions2

    c "We ordered you a cappuchino with oat milk. It looks like that's your preference from the data on file."
    n "2 minutes later..."
    show drone at topright with dissolve
    d "Here are your drinks. Please let me know anything else I can do to assist you."
    n "You sit in silence, realizing even more how easy it must be for Cyra to justify never leaving the house."
    jump chapter2