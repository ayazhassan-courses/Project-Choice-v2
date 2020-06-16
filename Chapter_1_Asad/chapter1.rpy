define adam = Character("Adam")
define shanzayy = Character("Shanzayy")

label node_12:
    
    $ currentNode = "node_12"

    "The next day starts and you wake up to an extremely tiring morning."

    "You feel as though you’ve lost all the energy you previously had because of how stressful your previous days have been."

    "Reluctantly you get out of bed and get ready to head out for university"

    "You take out your car and drive to university."
    
    "Upon reaching there you see familiar faces waiting for you."

    alaina "Hey [playerName]!! How’re you doing today?~~"

    asad "Looks the same to me, not gonna lie"

    menu:
        "Hey guys! It’s been a really bad morning, but thanks for being here, just seeing you all again is so soothing for me right now":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_12_1
        
        "Ughhh, I don’t have the energy to talk right now, sorry.":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_12_2

    call node_13

    return 

label node_12_1:
    #relation +2 all

    alaina "(smiles) Well what are friends for?~~"

    "You smile in return"

    return 

label node_12_2:
    #relation -2 all

    "You walk away while your friends sadly look at you in awe, unable to understand why you’re so distant today"

    return

label node_13:

    $ currentNode = "node_13"

    #scene changes to central

    "As you talk to your friends, you all walk towards your classes. You all stop at Central Street, say your goodbyes and all go your ways"

    #scene changes to classroom

    "You take your classes as usual and after they are over, you prepare to go to Tapal Cafeteria to meet your friends for lunch"

    #scene changes to central

    "As you’re preparing to go there, you meet Adam…"

    adam "(smirks) Hey small-fry"

    player "Ugh…What do you want?"

    adam "Show some respect or I’ll beat it into ya"

    player "(smiles sarcastically) Yesss sweety? Do you want something? :)"

    adam "As a matter of fact I do. Have you done the Calculus homework?"

    player "Of course, I was just about to submit it."

    adam "Show it to me"

    menu:
        "Why would I do that?":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_13_1

        "Sure thing!":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_13_2

    call node_14

    return 

label node_13_1:
    #relation -1 Adam
    #stress -2

    "Adam grabs your shirt’s collar and threatens you to show it to him"

    return

label node_13_2:
    #relation +1 Adam
    #stress +2

    "Adam grabs your shirt’s collar, smirks and says…"

    adam "Thanks :)"

    return

label node_14:

    $ currentNode = "node_14"

    "As you show him the homework, he takes it from you and keeps it"

    player "Hey, give it back. I have to submit it right now in an hour"

    adam "That’s your problem now. I’ve got my homework submission right here"

    "As you try to take it back from him, he pushes you hard and you fall to the ground"

    adam "Don’t forget your place, trash"

    "As soon as he says this he leaves, as you’re left hurt lying on the floor"

    "You get up and dust yourself"

    "Panicking about the work due in an hour you consider your options"

    menu:
        "Go to the library and try to get done with your work":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_14_1

        "Call Amil and ask for help":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_14_2

    call node_15

    return

label node_14_1:
    #relation -1 all

    "You call your friends and tell them that there’s been an emergency and that you won’t be able to make it today"

    "They are sad to hear this but they understand something important might’ve come up"

    "You hurry to the library and start working there"

    #scene change to library

    "You keep on working for almost 50 minutes and barely reach the faculty pod in order submit your homework submission"

    "After you’ve submitted it, you breathe a sigh of relief"

    return 

label node_14_2:
    #relation +3 all

    player "Hey Amil, so a scene happened and now I have to redo my entire Calculus homework in less than an hour. Can you help me out?"

    amil "Of course mate, come on over to Tapal and we’ll sort it out"

    "You go to Tapal…"

    #scene changes to Tapal

    "…and see Amil and Asad there"

    player "Guys I’m in a real pinch, Adam took my homework and now I have to do it right now"

    amil "Don’t worry mate, I’ve done it a ton of times, it’s very easy!"

    "Amil helps you solve the assignment very quickly! Asad explains concepts which he knows in order to improve your understanding. You all collectively work on it for 30 minutes and once it’s finished, you go and submit it."

    "You thank Amil and Asad for helping you throughout the process and you all hug!"

    return 

label node_15:
    
    $ currentNode = "node_15"

    "As you breathe a sigh of relief, you remember you used up your entire break time to re-solve the Calculus homework. Angrily you head back to your classes after saying goodbye to everyone"

    #scene change to Central Street

    "As you’re going to your next class, you see Shanzayy staring angrily at you and then at Adam who’s standing on the other side of Central street"

    #show Shanzayy angry

    shanzayy "...."

    "You try to ignore her and go away from there"

    "After your classes end, you tiredly go towards the basement area so that you can finally drive yourself back home"

    "As you’re heading to the basement, you hear…"

    #insert scream sound

    "SOMEONE SCREAM!"

    #insert tense music
