label intro:
    scene black
    n "The year is 2200. The world is run by AI Agents and Cyborgs."
    n "Humans without microchip implants have no use in society."
    n "Cyborgs who mastered summoning AI agents are the new lords."
    pause 1.5
    n "You are a cyborg who's microchip malfunctioned in a tragic accident."
    n "But you didn't despair. You found a new purpose."
    n "You decided your job is to help cyborgs get in touch with their human side."
    n "Time to go to your coffee meetup for cyborgs who want to disconnect."

label prologue:
    scene cafe with dissolve
    n "It's a quiet day. Fewer attendees have shown up than expected."
    n "You see a well-dressed young lady cyborg catch your eye. She smiles and walks over to you."
    show seren with dissolve
    u "Hi! You must be [player]. I'm Seren. I've read so much about you."
    menu:
        "Why thank you very much.":
            s "It really is an honor to meet you!"
            s "I loved your post about the research in how real life eye-contact can really elevate the human senses."
        "You've heard of me?":
            s "Of course I have! You're a legend!"
            s "I loved your post about the research in how real life eye-contact can really elevate the human senses."
            s "I think you're right - it totally makes me feel more inspired."
        "Incredible! Which blog?":
            s "The one on face to face connection."
            s "I loved your post about the research in how real life eye-contact can really elevate the human senses."
            s "I think you're right - it totally makes me feel more inspired."
    menu:
        "Are you suffering from digital overdose?":
            s "Actually, I've made a lot of progress from reading your blog."
            s "I've been going out more often, meeting people IRL."
            s "I even started a near-distance relationship."
            s "It's actually my friend I'm worried about."
        "How can I help you?":
            s "Well... I'm actually doing great."
            s "Your blogs really helped and I honestly think I'm more in touch with myself than ever before."
            s "I even started a near-distance relationship."
            s "It's actually my friend I'm worried about."

    menu serenquestions2:
        "I'm delighted to hear that my writing helped.":
            s "You really are an inspiration."
            s "I would've thought my life was over if I could no longer use my microchip."
            s "You taught me that being more human isn't anything to be ashamed of."
            jump serenquestions2
        "Congrats on the relationship!":
            s "Thank you. It's really really lovely."
            s "I can't believe I deprived myself from skin contact for so long..."
            jump serenquestions2
        "What's up with your friend?":
            s "Her name is Cyra. I met her in Summoning class at college." 
            s "She's a genius, even for a cyborg. Her biological brain has merged with her microchip, I swear."
            s "She had her implant put in when she was just a baby. Her parents didn't wait till school age like most people do."
            s "She's so deep in the digital world it's like she's become an AI Agent herself."
    
    menu serenquestions3:
        "Wow wait, so you're a summoner?":
            s "Kind of. I mean I'm no where near as talented as Cyra."
            s "But I can summon agents who specialize in data manipulation and I'm a decent prompter."
            s "It's how I built my successful crypto trading firm actually."
            jump serenquestions3
        "Tell me more about summoning.":
            $ serenquestion_summoner = True
            s "Right, yeah I know not many cyborgs know how to summon. Cyborgs are just humans connected to the internet all the time via their microchips."
            s "Summoners have learned how to become one with their microchips. They can manipulate data and summon AI agents to do as they please."
            s "They can summon physical bots or drones to do manual labor, summon holograms of experts to give advice, and summon new data structures to hack into systems."
            jump serenquestions3
        "Couldn't summoners take over the world then?" if serenquestion_summoner == True:
            s "Well, there are limits to their abilities depending on talent."
            s "And of course some bots and data sources have high level security so they can't be controlled."
            s "But it's true that in society summoners are the top, then it's cyborgs, then AI agents, and then it's humans."
            jump serenquestions3
        "So Cyra needs a digital-detox?":
            s "Eh... well... I don't want to change who she is. I accept her quirks."
            s "It's just that I'm turning 30 and I really want her to come to my birthday party in person."
            s "But she's insisting that there's no point and she can just dial in."
    
    menu serenquestions4:
        "You're turning 30?":
            s "Yeah... don't remind me."
            s "Although I know it's still relatively very young, I still can't help but face that milestone and say goodbye to my twenties."
            jump serenquestions4
        "You want me to persuade Cyra to go to a birthday party?":
            s "Yes, in real life."
            s "I know it sounds mundane, but it would mean so much to me. I miss her and I'd like her to meet my new partner."
            s "Will you help me out?"

    menu:
        "Of course happy to help.":
            s "THANK YOU SO MUCH."
            s "Here's her address."
            s "She'll know you're coming, but don't worry."
            s "Just use your skills to persuade her!"
            jump chapter1
        "She seems like a lost cause, but I'll try.":
            s "Haha thanks. I know there's a human in there somewhere."
            s "Here's her address."
            s "She'll know you're coming, but don't worry."
            s "Just use your skills to persuade her!"
            jump chapter1