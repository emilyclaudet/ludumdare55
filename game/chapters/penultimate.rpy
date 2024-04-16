label penulitmate:
    scene livingroom with dissolve
    show cyra with dissolve
    n "You think it's better to connect more directly with Cyra."
    n "From learning more about her, perhaps there is context that could help her appreciate the real world."
    menu cyradeepquestions:
        "Can you tell me about your hobbies?":
            c "My main goal is to scrape all the data and optimize it for money and trade."
            c "I occasionally start cyber wars on small-time ecommerce bidding sites to see how much it can change the prices."
            c "Although this is not the most productive for making money, it is interesting to see how customers react."
            jump cyradeepquestions
        "Tell me about your family?":
            c "This is more personal data, but I suppose it's in your interest to know."
            c "My parents are regular cyborgs who work in science. We keep in touch, but it's always async."
            c "I have no siblings, and not in touch with any cousins."
            c "My last grandparent passed away 1 year ago."
            $ cyradeepquestion1 = True
            jump cyradeepquestions
        "Sorry to hear about your grandmother. How do you feel?" if cyradeepquestion1 == True:
            c "It is sad but it is also inevitable."
            c "Human bodies die. We can preserve the data from their microchips if they are cyborgs though."
            c "Despite centries of research, humanity still has not found the way to stop death."
    n "You sense something is weighing down on Cyra's mind."
    menu:
        "Can't a genius like you solve death?":
            c "It should be a solvable problem."
            c "I have scraped all information and tried to run various simulations of solutions."
            c "I haven't found anything that works yet."
        "Death is natural, that's why it's not a solved problem":
            c "It should be possible to solve."
            c "I have scraped all information and tried to run various simulations of solutions."
            c "I haven't found anything that works yet."
    menu cyrasummoningquestion: 
        "What about using summoning?":
            c "That does not raise biotic life from the dead."
            c "But it's true that I can create the very form of someone from the past if I have the data on them."
        "Didn't you say data is the same as reality for you?.":
            c "That does not raise biotic life from the dead."
            c "But it's true that I can create the very form of someone from the past if I have the data on them."

    n "Cyra pauses. She glances to the side, looking even deeper in thought."
    n "Then her eyes grow soft and she returns to being present with you."
    c "It's possible for me to summon my grandmother. I have all her files."
    c "I thought about it a few times, but I did not think it was a productive thing to do."
    
    menu:
        "I think it's worth seeing what she would say.":
            c "I see your point. Even if not alive, it's very real."
            c "Summoning her could demonstrate how life-like my holograms are."
            c "And my grandmother was a nice person to talk to..."
        "I'd be interested to see how your grandmother was.":
            c "I see your point. Even if not alive, it's very real."
            c "Summoning her could demonstrate how life-like my holograms are."
            c "And my grandmother was a nice person to talk to..."

label grandmother:
    n "A hologram is fading into presence..."
    n "You see a silouette of what looks like an elderly lady with wings..."
    n "Cyra's gaze turns and there is a twinkle of emotion in her eyes."
    scene black with dissolve
    n "To be continued...."

    #TO DO
    # Add asset for the art agent
    # Add asset for Cyra from Marian
    # Add sounds
    # Add animation for the bots, just bobbing up and down maybe?
    # Add asset for Seren?