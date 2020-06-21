label node_26:
    
    $ currentNode = "node_26"

    "…"

    "………"

    "…………………"

    "Another day begins..."

    "You lack both the motivation and courage to get out of bed."

    player "Maybe I’ll just skip university for now…I have no clue what to do anymore…"

    "As you’re contemplating what you should do you pick up your mobile phone to see a message from Alaina that reads…"

    "Hey, [playerName]! I know you’re probably down today. I know this is a tough situation for you, but I’d love if you could try and make it to university today. I’m really looking forward to seeing you today hehe. Hope I get to talk to you lots~~"

    "Reading this message, you’re slightly more motivated and finally work up the courage to go to university today."

    "You’re listening to the news and you’re shocked to find no mention of anything related to the murder on the news…"

    #black flash scene

    "You finally reach the campus."

    #campus outside scene

    player "(sigh) Let's do this"

    "As soon as you enter the campus, you can feel the unrest around you. This place no longer feels like a safe space. As you’re walking by, a few people start giving you weird looks."

    "Ignoring them you move ahead and try to find Alaina and your friends"

    "Trying to search for them you see Ayesha from the corner of your eye. You smile, only for it to fade away the next moment when you notice her crying in front of Aaron."

    "You’re taken aback by this scene. You’ve never seen Ayesha so vulnerable before. She’s pleading for something while Aaron keeps on yelling at her, getting louder and louder until Ayesha drops to the floor, her hands covering her face."

    "Using this as a cue Aaron leaves and comes in your direction. Angry at what you just witnessed, you confront him."

    player "HEY! What’s the matter with you???"

    aaron "Get outta my face. Not in the mood to talk to a killer."

    "Aaron tries to leave but you grab his shoulder."

    "As soon as you do, he flips about and punches your face hard!"

    player "Ooomph"

    aaron "Don’t ever touch me again, dead weight."

    "Aaron says as he storms out of the scene angrily."

    #stress +4

    "Unable to say or do anything to him, you turn to Ayesha on the ground."

    player "Hey are you okay?"

    "Ayesha shakes her head saying no"

    player "Want to tell me what happened?"

    ayesha "I’m sorry [playerName], but I just need some space right now…"

    "She says, as she gets up, still hiding her face and she then leaves too."

    "Unsure of what to do, you wait there, pondering, until you remember you have to get to class!"

    "Throughout your classes that scene of Ayesha crying keeps on playing in your head like a tape recording. As soon as it ends, it just rewinds and starts again."

    "Soon your classes end. As you’re leaving a class, you get a call from Asad."

    #if Asad incestigated
        call node_26_1
    #else
        call node_26_2

    call node_27

    return 

label node_26_1:

    player "Hey, what's up?"

    asad "Hey! So I gave the samples to my friend in the network. And…"

    player "Yeah???"

    asad "It's...It's weird..."

    player "Tell me Asad, what’s wrong?"

    asad "I got the results for the DNA tests. I got it traced back to the sources. We know everyone who was involved…"

    player "Wait…I thought it’d be something else. How did you manage to find out who the DNA belongs to?"

    asad "Didn’t I tell you? I have a friend in the network."

    player "Wait…you don’t mean…"

    asad "Yes."

    player "Unbelievable. So, who does the DNA belong to?"

    asad "That’s the surprising part. The blood and hair samples had yours, Amil’s, Zayn’s, John’s and of course Ahsen’s DNA. My friend told me it could also arise from dead skin cells if you are with the person for a while."

    player "Seeing as me and Amil pulled him out, the suspects are Zayn and John?"

    asad "Probably."

    player "Yikes! Thanks for the information though!"

    asad "No problem! Sorry I couldn’t come to university today, or else I would’ve given them to you face to face."

    player "It’s cool! You rest up okay? Talk to ya later!"

    asad "Yeap! Good bye!!"

    "And you hang up the phone"

    return 

label node_26_2:

    "Not being in the mental condition to talk to anyone, you cut his phone call and move on."

    return 

label node_27:

    $ currentNode = "node_27"

    "As you snap back to reality, the morning scene keeps on playing again in your head, only stewing your already unstable emotions."

    "You decide to rest at the Dhabba area to cool off your head."

    "As you're resting, you fall asleep."

    #show black screen

    #black and white flashes

    "Suddenly you see black and white flashes and you jump awake!"

    #It's dark outside

    player "Ahhhhhhh"

    player "What was that??"

    "As you focus your eyes, you see someone lying in the grass."

    player "Guess I’m not the only one sleepy right now huh."

    "As you pay a closer look you notice it’s Aaron! And that he’s…lying on the ground very weirdly…"

    player "Oh no. Not this again…"

    "You go over to where Aaron is ‘sleeping’ and your suspicions are confirmed. He is… in fact… dead…"

    player "AHHHH. THIS HAS TO STOP, WHO IS DOING THIS?"

    "You scream."

    menu:
        "I should investigate this. This needs to stop. Now. This is enough… (Investigate)":
            call node_27_1
        
        "I can’t handle this anymore… (Do not investigate)":
            call node_27_2

    call node_28

    return

label node_27_1:
    #stress -7

    "You start to investigate, and like the previous two murders, there’s a note left behind. The note reads:"

    "Who’s {i} dead {/i} weight now? :)"

    player "...."

    "At this point you’re starting to question your own sanity."

    player "What do these notes means? What is going on? Why are people suddenly dying??"

    "You investigate further and notice that Aaron’s throat has been pierced with a violin bow."

    player "So the person who did this probably had access to a violin or the music room."

    "You investigate further and see a shirt’s button in Aaron’s hand. You take it out of his hands and inspect it. Not wanting to tamper further with the evidence, you put it back."

    return

label node_27_2:
    #stress +9

    "You start hyperventilating. Every murder, all that tension, everything washes over you like a waterfall and you start to have a panic attack."

    player "I can’t do this anymore. I can’t do this anymore. I can’t do this anymore."

    "You start to mutter to yourself over and over again."

    "You decide to get this over with and get up."

    return 

label node_28:

    $ currentNode = "node_28"

    "As you’re about to go call campus security again, someone has already done so. People have started gathering around and once Campus Security is here, you tell them everything that happened. They cover and close off the area and you finally decide to leave."

    "Everything that happened afterwards is a blur to you. You do not remember what happened or how it happened but when you come back into focus; you’re lying there in your bedroom, with vague memories of how you go there."

    "You decide to just sleep on it, since you cannot do anything anymore…"

    call node_29

    return
        
