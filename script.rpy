

define player = Character("[playerName]")
define alaina = Character("Alaina")
define asad = Character("Asad")
define adam = Character("Adam")
define ayesha = Character("Ayesha")
define amil = Character("Amil")
define shanzayy = Character("Shanzayy")


label start:
    $ stress=0
    call chapter_0
    return

screen stress_counter:
    hbox:
        textbutton "Stress: [stress]" action Show("pop_up")


label chapter_0:
    call variables
    call node_1
    return

label node_1:
    $ currentNode='node_1'
    #scene bedroom
    show screen stress_counter
    "You wake up to another day at university."
    #scene change bathroom
    "You’re lost in the sight of your bedroom. Barely awake you try to make sense of who you are and what you’re doing here"
    $ playerName = renpy.input("Enter your name:").strip()
    menu:
        'Female':
            $ gender='Female'
        'Male':
            $ gender='Male'
    #show player
    "You get ready and prepare to head out"
    player "Can’t wait to meet everyone"
    #show player happy
    player "It feels like it’s been years since I’ve met everyone"
    #scene change car_ride
    #scene change habib_entrance
    "You go through the gates and bask in the glorious structure in front of you…"
    #scene change habib_building
    "And are attacked on the back by…"
    #show alaina at left
    #show asad at right
    alaina "Heyyyyyy [player], what’re you so zoned out for?~~"
    asad "Probably day-dreaming about what he’s going to study next"
    alaina "Hehehe, yeah I guess he is a big nerd after all~~"
    menu:
        "Hey guys what’s up!?":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_1_1
        "Ughh, why are you guys so annoying so early in the morning":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_1_2
    call node_2
    return

label node_1_1:
    return

label node_1_2:
    return

label node_2:
    $ currentNode='node_2'
    alaina "Happy to see is all~~"
    asad "I finally won that gaming tournament right now, so I’m as happy as a lark"
    player "Great to hear that! But…"
    player "Come on guys, let’s keep walking or we’ll be late for class"
    "You and the others head to Central Street"
    #scene change central_street
    "This is Central Street. It is the first place you see when you come into Habib. It connects all the different areas of Habib together. You can head to any of the other locations from here!"
    "You’re standing with your friends when you see Adam"
    "Adam 'accidentally' bumps into you"
    adam "Are you blind or something?"
    player "You’re the blind one, you bumped into me…?"
    adam "Hahaha, my bad, all I saw was dead air, didn’t think it was actually you"
    menu:
        "Maybe you should get glasses, though I don’t know whether they make them for eggheads or not":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_2_1
        "How about I punch your face in?":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_2_2
        "…":
            $ relationKeeper(chapter0_network, currentNode, "Choice3")
            call node_2_3
    call node_3
    return

label node_2_1:
    #show alaina laugh
    #show asad laugh
    #show bully angry
    "…"
    return

label node_2_2:
    return

label node_2_3:
    adam "Yeah thought so"
    return


label node_3:
    $ currentNode='node_3'
    player "Okay guys, guess I’ll go to my classes now that this drama’s over"
    #show alaina happy
    alaina "Byeeee!~~"
    #asad smiles
    asad "See ya later dude!"
    "Tired from the early morning drama, you reluctantly head to your classes"
    "And like that, before you even know it, your classes ended"
    "You decide to go to the library and study up a little before you head out for lunch"
    #scene change library
    "This is Habib University’s library! It’s a great place to study both by yourself and in groups! You can get a lot of work done here if you focus and work hard on your academics!"
    "You decide to go to your favorite spot, that is, the Info Commons!"
    "As you head there you see a familiar face"
    amil "Hey [player], finally done with classes?"
    player "Yeap! I’m so exhausted but I have so much work left ughhh…"
    amil "Now now, you mustn’t fret when I’m here. I’m mostly done with my work so let’s see yours"
    #show amil happy
    player "Thank youuuuuu!! I really need help with…"
    menu:
        "Writing my modernity essay":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_3_1
        "Understanding Dijkstra's algorithm":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_3_2
        "Understanding these Calculus problems":
            $ relationKeeper(chapter0_network, currentNode, "Choice3")
            call node_3_3
    call node_4
    return

label node_3_1:
    $ currentNode='node_3_1'
    "You show him your essay"
    menu:
        "I don’t know how to start this essay":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_3_1_1
        "How do I transition between these paragraphs":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_3_1_2
        "Can you please proof read this for me?":
            $ relationKeeper(chapter0_network, currentNode, "Choice3")
            call node_3_1_3
    return

label node_3_1_1:
    amil "Okay so you take the topic and…"
    "Amil explains how to write topic sentences and start essays"
    return

label node_3_1_2:
    "Amil shows you a list of transition words and explains how to use them"
    return

label node_3_1_3:
    "Amil proof reads it and points out your mistakes and shows you how to correct them"
    return

label node_3_2:
    $ currentNode='node_3_2'
    "Amil starts typing out code on Visual Studio Code"
    menu:
        "How does the algorithm know which path is the shortest?":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_3_2_1
        "Which searching algorithm do we use and why?":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_3_2_2
    return

label node_3_2_1:
    amil "So basically you look at the edge weights…"
    "Amil continues and fully explains the algorithm"
    return

label node_3_2_2:
    amil "It’s kind of neither, but slightly close to BFS. Let me explain…"
    "Amil continues and fully explains the algorithm"
    return

label node_3_3:
    $ currentNode='node_3_3'
    "Amil opens his notes and starts to guide you through them"
    player "I’m having trouble with these problems, can you help me?"
    amil "Yeah sure, so in this question what you do is… "
    "Amil explains all your queries."
    return

label node_4:
    $ currentNode='node_4'
    amil "Oh, regarding this let’s go to the first floor, there’s a great book there to explain this concept!"
    "You and Amil go to the Library first floor to find the book!"
    #scene change library_shelves
    "After arriving at the shelves, you suddenly see…"
    #show ayesha happy
    ayesha "Hey!!! [player]"
    "Ayesha!"
    ayesha "What’cha guys up to?"
    amil "Hey Ayesha! Just here to find book so I can explain this one thing to [player]"
    player "What Amil said"
    ayesha "Ahhh youth. I remember the time I actually studied hehe"
    amil "You still do… you’re in the dean’s list…"
    ayesha "Shhhh that’s a secret hehe"
    player "Ohhh why don’t we just ask her to explain this problem?"
    amil "Great idea!"
    "You all start talking and discussing in between the shelves"
    ayesha "Why don’t we continue this in Tapal? I’m really hungry"
    amil "Sure, good with me!"
    player "Sure, you guys go ahead, I’ll grab my bag and meet you there"
    amil "Seems good, see you there!"
    "Amil and Ayesha go to Tapal Cafeteria while you go to Info Commons to grab your bag from there"
    "You leave Info Commons and go through Central Street to Tapal Cafeteria"
    #scene change central_street
    shanzayy "Oh Em Gee wow, lunch with friends. Must be fun when no one else likes you right?"
    "This is Shanzayy, she is extremely popular but has a very narcissistic personality because of her fame. She has a weird rivalry with the player, where she’s not openly hostile but isn’t really friendly with the player either as of yet"
    menu:
        "Ugh what do you want?":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_4_1
        "Describing your life sweetie?":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_4_2
        "Come on, you don’t have to be mean. Can’t we play nice?":
            $ relationKeeper(chapter0_network, currentNode, "Choice3")
            call node_4_3
    call node_5
    return

label node_4_1:
    shanzayy "Why would I want anything to do with you> Ha!"
    return

label node_4_2:
    shanzayy "More yours than mine prick"
    return

label node_4_3:
    shanzayy "Well…Um…Whateverrr"
    return


label node_5:
    $ currentNode='node_5'
    player "So what did you want?"
    shanzayy "Oh nothing, just here to get rid of the poor people for ruining my view of the clean Central Street"
    menu:
        "Well guess I’ll leave then. Have a good day Shanzayy":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_5_1
        "Well maybe you should get your head out of the gutter then, for a better view":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_5_2
    call node_6
    return


label node_5_1:
    shanzayy "Uhh wait…umm…nevermind"
    #show shanzayy sad
    "You leave while Shanzayy stands there staring at you"
    return

label node_5_2:
    #show shanzayy angry
    shanzayy "Oomph, prick"
    "Shanzayy leaves"
    "You finally head towards Tapal"
    return
