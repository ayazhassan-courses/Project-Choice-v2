label node_15:
    #continued...
    $ currentNode='node_15'
    "Try to track the source of the scream, you see Shanzayy lying on the ground sobbing hardly"
    player "Shanzayy… Shanzayy…SHANZAYY"
    "You scream as you try to shake her out of her crying daze"
    menu:
        "Stop crying dammit. Shut up and tell me what’s wrong":
            $ relationKeeper(chapter1_network, currentNode, "Choice1")
            call node_15_1
        "Shanzayy? Are you alright Shanzayy? What’s wrong? Come on tell me.":
            $ relationKeeper(chapter1_network, currentNode, "Choice2")
            call node_15_2
    call node_16
    return

label node_15_1:
    "Shanzayy looks at you shocked, unable to understand what you just said to her and she starts crying even more"
    return

label node_15_2:
    "You say as you try and shake her out of her shocked state"
    "She looks at you, and hugs you unable to say anything"
    return


label node_16:
    $ currentNode='node_16'
    "You look around to see a strange mound beside your car"
    "As you leave Shanzayy’s side to look into it further, you’re overwhelmed with the sight before you. Your eyes cannot believe themselves. It’s the body of Adam, lying beside your car, seemingly dead."
    "You try to move him, but he is indeed dead."
    "You think of investigating but start to consider its consequences"
    menu:
        "I don’t know whether I can handle this much gore or not. (Don’t investigate)":
            call node_16_1
        "I need to get to the bottom of this. (Investigate)" :
            call node_16_2
    call node_17
    return

label node_16_1:
    $ stress+=4
    "You decide not to investigate and instead back away from the scene of the murder"
    return

label node_16_2:
    $ stress-=3
    "You investigate the body to find…"
    "His collar is bunched up and his throat has been slit” “You also notice his head has been bashed"
    "You also see the door of your car unlocked for some reason, even though you just arrived here"
    "You also find a note beside him…"
    "You open the note to have it read ‘Hope you get good marks on your Calculus homework :)’"
    "Reading this note sends shivers down your spine and you decide to stop investigating further"
    return


label node_17:
    $ currentNode='node_17'
    "You stand up and console Shanzayy enough that she can stand and go with you"
    "You both leave the scene and exit the basement"
    "As soon as you’re exiting the basement you meet Asad and John"
    asad "[player] why are your clothes bloody like that…"
    john "And why is Shanzayy crying…"
    "You explain to them everything you witnessed. Shanzayy’s screams, the murdered body of Adam and everything else"
    asad "Oh my God, we need to report this to campus security immediately"

    $ Johnrelation = relationshipdict['John']
    $ value=15
    if Johnrelation > value: #John (automatic)
        $ relationKeeper(chapter1_network, currentNode, "Choice1")
        call node_17_1
    else:
        $ relationKeeper(chapter1_network, currentNode, "Choice2")
        call node_17_2
    call node_18
    return

label node_17_1:
    john "Yeap, let’s go immediately. We can’t waste any time on this."
    return

label node_17_2:
    john "Nahhh man, I’m out of this murder fiasco, you guys are on your own"
    return

label node_18:
    $ currentNode='node_18'
    "You all head to the campus security office, where you explain everything that happened. They go to the scene of the crime, close it off, issue a gag order and tell you not to tell anyone about this"
    "Both you and Shanzayy are comforted by Asad. Shanzayy’s friend volunteers to drop her off while Asad volunteers to drop you off at your home"
    "You, still shaking, get into Asad’s car and he drops you off at your home"
    "You enter your home, explain everything to your parents and go isolate yourself in your room"
    "While trying to make sense of everything that just happened, you receive a group call from all your friends"
    menu:
        "Pick up the phone and talk to them":
            $ relationKeeper(chapter1_network, currentNode, "Choice1")
            call node_18_1
        "Ignore their call and go to sleep":
            $ relationKeeper(chapter1_network, currentNode, "Choice2")
            call node_18_2
    call node_19
    return

label node_18_1:
    $ stress-=4
    "You talk to your friends and tell them about everything that happened. They console you and try to help you feel better about the weird situation."
    "After talking to them for a while, you feel slightly relaxed. You say your goodbyes and sleep after ending the call"
    return
label node_18_2:
    $ stress+=4
    "The eerie thoughts keep gnawing at your sanity, soon you’re having anxiety attacks thinking about the entire scene of the murder"
    "Tired from all the mental exhaustion, you slowly drift away into a stressful slumber"
    return



label node_19:
    $ currentNode='node_19'
    #scene change black
    #scene change white flash
    #scene change hospital
    #show nurse worried
    nurse "Doctor he’s regaining consciousness, what do we do?"
    doctor "Inject him with 50 micrograms of Fentanyl, 110mg of Propofol, and 30mg of Rocuronium. Wait 15 seconds and then 5 mg of Morphine."
    "The Nurse injects you with weird concoctions until you start to feel you head feel lighter than before…and you slowly…start to drift away again…"
    #scene change black
    #scene change bedroom
    "You suddenly wake back up in your room in cold sweats and scream"
    player "AHHHH"
    "You look around to see that you are in your room, as when you fell asleep"
    player "Weird dream…What was that…"
    "As you start to ponder over what you saw, you fall asleep again…"
    return
