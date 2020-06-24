#This is the helper function that uses the node network and data structures
init python:
    def relationKeeper(ds,currentNode, choice): #It takes the current node you're on, the nodenetwork and choice as input
        global relationshipDict     #this helps it change the reltionships and stress counter
        global stress
        for i in ds[currentNode]:      #It cycles throught the node network to match the choice
            if i[0]==choice:            #And adjusts the relations etc accordingly
                stress+=i[1]
                for j in i[2]:
                    relationshipDict[j[0]]+=j[1]
                    if relationshipDict[j[0]]<0:
                        relationshipDict[j[0]]=0
                return i[-1]   #It also returns the node you will go to according to your choice
  


define player = Character("[playerName]")   #This part of the code defines the characters and their names
define aaron = Character("Aaron")
define alaina = Character("Alaina")
define amil = Character("Amil")
define asad = Character("Asad")
define ayesha = Character("Ayesha")
define john = Character("John")
define zayn = Character("Zayn")
define ahsen = Character("Ahsen")
define sean = Character("Sean")
define adam = Character("Adam")
define shanzayy = Character("Shanzayy")
define doctor = Character("Doctor")
define nurse = Character("Nurse")
define cop = Character("Senior Investigative Officer")

#Importing of images from the files
image basement = im.Scale("basement.jpg", 1920, 1080)
image bathroom = im.Scale("Bathroom.jpg", 1920, 1080)
image bedroom = im.Scale("bedroom.jpg", 1920, 1080)
image black = im.Scale("black.png", 1920, 1080)
image carRide = im.Scale("carRide.jpg", 1920, 1080)
image central = im.Scale("centralStreet.png", 1920, 1080)
image central2 = im.Scale("centralTwo.png", 1920, 1080)
image classroom = im.Scale("classroom.png", 1920, 1080)
image courts = im.Scale("courts.png", 1920, 1080)
image courtsNight = im.Scale("courtsNight.png", 1920, 1080)
image dhabba = im.Scale("dhabba.jpg", 1920, 1080)
image dhabbaNight = im.Scale("DhabbaNight.png", 1920, 1080)
image earthCourtyard = im.Scale("earthCourtyard.png", 1920, 1080)
image gardenDhabba = im.Scale("gardenDhabba.png", 1920, 1080)
image gardenMurderArea = im.Scale("gardenMurderArea.png", 1920, 1080)
image gardenMurderAreaNight = im.Scale("gardenMurderAreaNight.png", 1920, 1080)
image gym = im.Scale("gym.png", 1920, 1080)
image habibInside = im.Scale("habibInside.png", 1920, 1080)
image habibOutside = im.Scale("habibOutside.png", 1920, 1080)
image hospital = im.Scale("hospital.jpg", 1920, 1080)
image infoCommons = im.Scale("infoCommons.png", 1920, 1080)
image libraryShelves = im.Scale("libraryShelves.png", 1920, 1080)
image livingRoom = im.Scale("livingRoom.jpg", 1920, 1080)
image murderNote1 = "murderNote1.png"
image murderNote2 = "murderNote2.png"
image murderNote3 = "murderNote3.png"
image musicRoom = im.Scale("musicRoom.png", 1920, 1080)
image securityRoom = im.Scale("securityRoom.jpg", 1920, 1080)
image stairsDownwards = im.Scale("stairsDownwards.png", 1920, 1080)
image tapal = im.Scale("tapal.png", 1920, 1080)
image tapalOutside = im.Scale("tapalOutside.png", 1920, 1080)
image white = im.Scale("white.png", 1920, 1080)
image libraryCourtyard = im.Scale("libraryCourtyard.png", 1920, 1080)
image driving = im.Scale("driving.jpg", 1920, 1080)

#Importing character renders
image Aaron = "aaron.png"
image Adam = "adam.png"
image Ahsen = "ahsen.png"
image Alaina = "alaina.png"
image Amil = "amil.png"
image Asad = "asad.png"
image Ayesha = "ayesha.png"
image Doctor = "doctor.png"
image John = "john.png"
image Nurse = "nurse.png"
image Policeman = "policeman.png"
image Sean = "sean.png"
image ShanzayyAngry = "shanzayyAngry.png"
image ShanzayyHappy = "shanzayyHappy.png"
image Zayn = "zayn.png"










#Labels are like functions and or/nodes, they contain code and you can jump between them
label start:
    #The call function is used to just to another node
    call chapter_0 from _call_chapter_0
    return

label variables:
    $ stress = 80    #Stress levels
    $ asadInvestigate=False   #Variable to be used later


    #This is the node network. It uses a dictionary to store the nodes. 
    #The nodes have tuples of choices and their edge weights
    #Edge weights include the stress and reltionship levels
    #We mimicked the adjacency list form of a Directed Acycic Graph to make it
    $ chapter0_network = {
    'node_1':[
        ('Choice1',-1, [('Asad',1),('Alaina',1)],'node_1_1'),
        ('Choice2',2, [('Asad',-1),('Alaina',-1)],'node_1_2')
        ],
    'node_2':[
        ('Choice1',-2, [('Asad',1),('Alaina',1)],'node_2_1'),
        ('Choice2',2, [('Asad',-1),('Alaina',-1)],'node_2_2'),
        ('Choice3',1, [('Asad',1),('Alaina',1)],'node_2_3')
        ],
    'node_3':[
        ('Choice1',-1, [('Amil',1)],'node_3_1'),
        ('Choice2',-1, [('Amil',1)],'node_3_2'),
        ('Choice3',-1, [('Amil',1)],'node_3_3')
        ],
    'node_3_1':[
        ('Choice1',-1, [('Amil',1)],'node_3_1_1'),
        ('Choice2',-1, [('Amil',1)],'node_3_1_2'),
        ('Choice3',-1, [('Amil',1)],'node_3_1_3')
        ],
    'node_3_2':[
        ('Choice1',-1, [('Amil',1)],'node_3_2_1'),
        ('Choice2',-1, [('Amil',1)],'node_3_2_2'),
        ('Choice3',-1, [('Amil',1)],'node_3_2_3')
        ],
    'node_3_3':[
        ('Choice1',-1, [('Amil',1)],'node_3_3_1'),
        ('Choice2',-1, [('Amil',1)],'node_3_3_2'),
        ('Choice3',-1, [('Amil',1)],'node_3_3_3')
        ],
    'node_4':[
        ('Choice1',1, [('Shanzayy',0)],'node_4_1'),
        ('Choice2',-1, [('Shanzayy',-1)],'node_4_2'),
        ('Choice3',-2, [('Shanzayy',1)],'node_4_3')
        ],
    'node_5':[
        ('Choice1',-3, [('Shanzayy',2)],'node_5_1'),
        ('Choice2',1, [('Shanzayy',-2)],'node_5_2')
        ],
    'node_6':[
        ('Choice1',-2, [('Asad',2),('Alaina',2),('Ayesha',2),('Amil',2)],'node_6_1'),
        ('Choice2',0, [('Asad',0),('Alaina',0),('Ayesha',0),('Amil',0)],'node_6_2'),
        ('Choice3',4, [('Asad',-4),('Alaina',-4),('Ayesha',-4),('Amil',-4)],'node_6_3')
        ],
    'node_6_1':[
        ('Choice1',-1, [('Asad',0),('Alaina',0),('Ayesha',0),('Amil',0)],'node_6_1_1'),
        ('Choice2',-3, [('Asad',2),('Alaina',2),('Ayesha',2),('Amil',2)],'node_6_1_2'),
        ('Choice3',2, [('Asad',-1),('Alaina',-1),('Ayesha',-2),('Amil',-1)],'node_6_1_3')
        ],
    'node_6_2':[
        ('Choice1',-1, [('Asad',1),('Alaina',1),('Ayesha',1),('Amil',1)],'node_6_2_1'),
        ('Choice2',2, [('Asad',-2),('Alaina',-2),('Ayesha',-2),('Amil',-2)],'node_6_2_2'),
        ('Choice3',-3, [('Asad',2),('Alaina',2),('Ayesha',2),('Amil',2)],'node_6_2_3')
        ],
    'node_7':[
        ('Choice1',-2, [('John',2),('Zayn',1)],'node_7_1'), 
        ('Choice2',2, [('John',-2)],'node_7_2') 
        ],
    'node_8':[
        ('Choice1',-2, [('Zayn',2)],'node_8_1'),
        ('Choice2',-1, [('Zayn',1)],'node_8_2'),
        ('Choice3',-1, [('Zayn',1)],'node_8_3'),
        ('Choice4',2, [('Zayn',-2)],'node_8_4')
        ],
    'node_9':[
        ('Choice1',-3, [('John',3)],'node_9_1'),
        ('Choice2',-3, [('Zayn',3)],'node_9_2'),
        ('Choice3',0, [('Zayn',0)],'node_9_3')
        ],
    'node_10':[
        ('Choice1',-3, [('Sean',3)],'node_10_1'),
        ('Choice2',-3, [('Sean',3)],'node_10_2'),
        ('Choice3',0, [('Sean',0)],'node_10_3')
        ],  
    }

    $ chapter1_network = {
    'node_12':[
        ('Choice1',-2, [('Asad',2),('Alaina',2),('Amil',2)],'node_12_1'),
        ('Choice2',2, [('Asad',-2),('Alaina',-2),('Amil',-2)],'node_12_2')
        ],
    'node_13':[
        ('Choice1',-2, [('Adam',-1)],'node_13_1'),
        ('Choice2',2, [('Adam',1)],'node_13_2')
        ],
    'node_14':[
        ('Choice1',3, [('Asad',-1),('Amil',-1)],'node_14_1'),
        ('Choice2',-2, [('Asad',3),('Amil',3)],'node_14_2')
        ],
    'node_15':[
        ('Choice1',5, [('Shanzayy',-4)],'node_15_1'),
        ('Choice2',-5, [('Shanzayy',5)],'node_15_2')
        ],
    'node_16':[
        ('Choice1',4, [('Shanzayy',-1)],'node_16_1'),
        ('Choice2',-4, [('Shanzayy',1)],'node_16_2')
        ],
    'node_17':[ #THIS CHOICE IS AUTOMATIC SO CHECK AND REPLACE VALUES ACCORDINGLY
        ('Choice1',-2, [('John',3)],'node_17_1'),
        ('Choice2',2, [('John',-2)],'node_17_2')
        ],
    'node_18':[
        ('Choice1',-4, [('Asad',3),('Alaina',3),('Amil',3),('Ayesha',3)],'node_18_1'),
        ('Choice2',4, [('Asad',-2),('Alaina',-2),('Amil',-2),('Ayesha',-2)],'node_18_2')
        ]
    }

    $ chapter2_network = {
    'node_20':[
        ('Choice1',-2, [('Zayn',2),('Sean',2)],'node_20_1'),
        ('Choice2',2, [('Zayn',-2),('Sean',-2)],'node_20_2')
        ],
    'node_21':[
        ('Choice1',-2, [('Ahsen',-2)],'node_21_1'),
        ('Choice2',3, [('Ahsen',-2)],'node_21_2')
        ],
    'node_22':[
        ('Choice1',-3, [('Asad',3),('Amil',3)],'node_22_1'),
        ('Choice2',3, [('Asad',-3),('Amil',-3)],'node_22_2')
        ],
    'node_23':[
        ('Choice1',-4, [('Asad',1),('Amil',1)],'node_23_1'),
        ('Choice2',4, [('Asad',-1),('Amil',-1)],'node_23_2')
        ],
    'node_23_1':[
        ('Choice1',-4, [('Asad',3),('Amil',2)],'node_23_1_1'),
        ('Choice2',0, [('Asad',1),('Amil',1)],'node_23_1_2')
        ],
    'node_24':[
        ('Choice1',-4, [('Shanzayy',3)],'node_24_1'),
        ('Choice2',4, [('Shanzayy',-2)],'node_24_2')
        ]
    }

    $ chapter3_network = {
    'node_26':[
        ('Choice1',-2, [('Asad',2)],'node_26_1'),
        ('Choice2',-1, [('Asad',-1)],'node_26_2')
        ],
    'node_27':[
        ('Choice1',-7, [('Amil',0)],'node_27_1'),
        ('Choice2',9, [('Zayn',0)],'node_27_2')
        ]
    }
    #This dictionary stores the relationship levels with each character
    #Relationship levels can be used to unlock bonus scenes when certain levels are met
    $ relationshipDict = {
        "Aaron":25,
        "Alaina":80,
        "Amil":90,
        "Asad":85,
        "Ayesha":70,
        "John":50,
        "Zayn":60,
        "Ahsen":25,
        "Sean":65,
        "Shanzayy":40,
        "Adam":25
    }
    return



screen stress_counter:
    hbox:
        textbutton "Stress: [stress]" 

label chapter_0:
    call variables from _call_variables
    call node_1 from _call_node_1
    
    return

#CHAPTER ZERO STARTS HERE--------------------------------------------------------------------------------------------------------------------------------------------------------
label node_1:
    $ currentNode='node_1'  #This is used for the helper function to know the current node
    scene bedroom
    play music "chp01music.mp3" loop
    show screen stress_counter
    "You wake up to another day at university."
    
    "You’re lost in the sight of your bedroom. Barely awake you try to make sense of who you are and what you’re doing here"
    $ playerName = renpy.input("Enter your name:").strip()
    menu:
        'Female':
            $ gender='Female'
        'Male':
            $ gender='Male'
    
    scene bathroom
    with dissolve
    "You get ready and prepare to head out"
    scene livingRoom
    player "Can’t wait to meet everyone"
    
    player "It feels like it’s been years since I’ve met everyone"
    
    scene habibOutside with fade
    "You go through the gates and bask in the glorious structure in front of you…"
    scene habibInside
    "And are attacked on the back by…"
    show Alaina at right
    show Asad at left
    alaina "Heyyyyyy [player], what’re you so zoned out for?~~"
    asad "Probably day-dreaming about what he’s going to study next"
    alaina "Hehehe, yeah I guess he is a big nerd after all~~"
    menu:
        "Hey guys what’s up!?":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")  #The menu option allows us to have different choices
            call node_1_1 from _call_node_1_1
        "Ughh, why are you guys so annoying so early in the morning":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_1_2 from _call_node_1_2
    call node_2 from _call_node_2
    return

label node_1_1:
    
    return

label node_1_2:
    
    return

label node_2:
    $ currentNode='node_2'
    alaina "Happy to see you is all~~"
    asad "I finally won that gaming tournament right now, so I’m as happy as a lark"
    player "Great to hear that! But…"
    player "Come on guys, let’s keep walking or we’ll be late for class"
    "You and the others head to Central Street"
    scene central
    "This is Central Street. It is the first place you see when you come into Habib. It connects all the different areas of Habib together. You can head to any of the other locations from here!"
    "You’re standing with your friends when you see Adam"
    "Adam 'accidentally' bumps into you"
    show Adam at center
    adam "Are you blind or something?"
    player "You’re the blind one, you bumped into me…?"
    adam "Hahaha, my bad, all I saw was dead air, didn’t think it was actually you"
    menu:
        "*smirks* Maybe you should get glasses, though I don’t know whether they make them for eggheads or not":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_2_1 from _call_node_2_1
        "*angry* How about I punch your face in?":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_2_2 from _call_node_2_2
        "…":
            $ relationKeeper(chapter0_network, currentNode, "Choice3")
            call node_2_3 from _call_node_2_3
    call node_3 from _call_node_3
    return

label node_2_1:
    
    "Alaina and Asad laugh"
    adam "…"
    return

label node_2_2:
    
    "You try to punch him, but Alaina and Asad stop you. Adam then leaves."
    return

label node_2_3:
    
    adam "Yeah thought so"
    "When Adam leaves, Alaina and Asad console you."
    return


label node_3:
    $ currentNode='node_3'
    hide Adam
    player "Okay guys, guess I’ll go to my classes now that this drama’s over"
    show Alaina 
    alaina "Byeeee!~~"
    hide Alaina
    show Asad
    asad "See ya later dude!"
    hide Asad
    "Tired from the early morning drama, you reluctantly head to your classes"
    scene classroom with fade
    "And like that, before you even know it, your classes ended"
    scene libraryCourtyard
    "You decide to go to the library and study up a little before you head out for lunch"
    scene infoCommons
    "This is Habib University’s library! It’s a great place to study both by yourself and in groups! You can get a lot of work done here if you focus and work hard on your academics!"
    "You decide to go to your favorite spot, that is, the Info Commons!"
    "As you head there you see a familiar face"
    show Amil
    amil "Hey [player], finally done with classes?"
    player "Yeap! I’m so exhausted but I have so much work left ughhh…"
    amil "Now now, you mustn’t fret when I’m here. I’m mostly done with my work so let’s see yours"
    
    player "Thank youuuuuu!! I really need help with…"
    menu:
        "Writing my modernity essay":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_3_1 from _call_node_3_1
        "Understanding Dijkstra's algorithm":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_3_2 from _call_node_3_2
        "Understanding these Calculus problems":
            $ relationKeeper(chapter0_network, currentNode, "Choice3")
            call node_3_3 from _call_node_3_3
    call node_4 from _call_node_4
    return

label node_3_1:
    $ currentNode='node_3_1'
    "You show him your essay"
    menu:
        "I don’t know how to start this essay":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_3_1_1 from _call_node_3_1_1
        "How do I transition between these paragraphs":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_3_1_2 from _call_node_3_1_2
        "Can you please proof read this for me?":
            $ relationKeeper(chapter0_network, currentNode, "Choice3")
            call node_3_1_3 from _call_node_3_1_3
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
            call node_3_2_1 from _call_node_3_2_1
        "Which searching algorithm do we use and why?":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_3_2_2 from _call_node_3_2_2
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
    scene libraryShelves
    "After arriving at the shelves, you suddenly see…"
    show Ayesha
    ayesha "Hey!!! [player]"
    "Ayesha!"
    ayesha "What’cha guys up to?"
    hide Ayesha
    show Amil at left
    amil "Hey Ayesha! Just here to find book so I can explain this one thing to [player]"
    player "What Amil said"
    show Ayesha at right
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
    hide Amil
    hide Ayesha

    "Amil and Ayesha go to Tapal Cafeteria while you go to Info Commons to grab your bag from there"
    scene infoCommons
    "You leave Info Commons and go through Central Street to Tapal Cafeteria"
    scene central
    show ShanzayyAngry
    shanzayy "Oh Em Gee wow, lunch with friends. Must be fun when no one else likes you right?"
    "This is Shanzayy, she is extremely popular but has a very narcissistic personality because of her fame. She has a weird rivalry with the player, where she’s not openly hostile but isn’t really friendly with the player either as of yet"
    menu:
        "Ugh what do you want?":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_4_1 from _call_node_4_1
        "Describing your life sweetie?":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_4_2 from _call_node_4_2
        "Come on, you don’t have to be mean. Can’t we play nice?":
            $ relationKeeper(chapter0_network, currentNode, "Choice3")
            call node_4_3 from _call_node_4_3
    call node_5 from _call_node_5
    return

label node_4_1:
    
    shanzayy "Why would I want anything to do with you? Ha!"
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
            call node_5_1 from _call_node_5_1
        "Well maybe you should get your head out of the gutter then, for a better view":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_5_2 from _call_node_5_2
    call node_6 from _call_node_6
    return


label node_5_1:
    
    shanzayy "Uhh wait…umm…nevermind"
    
    "You leave while Shanzayy stands there staring at you"
    return

label node_5_2:
    
    shanzayy "Oomph, prick"
    "Shanzayy leaves"
    "You finally head towards Tapal"
    return

label node_6:
    scene stairsDownwards
    

    $ currentNode = "node_6"
    "You walk towards Tapal Cafeteria, trying to clear your head of all the people who are mean to you on a daily basis and before you know it, you’re standing at the door of Tapal Café"
    scene tapalOutside
    "You’re about to open the door, when  it suddenly opens itself, revealing…"
    show Aaron
    "Aaron..."
    "Sigh, this day just HAD to get worse, you think to yourself"
    aaron "(scoffs) Oh look what the cat dragged in"
    player "I don’t even have the energy to deal with you right now..."
    aaron "Worry not, I’m off to the airport to pick up Papa from his flight from Germany. I’m feeling proud today you see; he made a multi-million dollar deal with Aces industries, so now he’ll probably buy me that new car hahaha"
    player "I don’t remember asking"
    aaron "True, I in fact do not have time to waste on…on…people like you…"
    "Aaron is implying how he has a higher standard than you"
    "And after saying that Aaron leaves"
    "Sighing again you enter Tapal Cafeteria"
    scene tapal with fade

    "You spot your friends Alaina, Amil, Asad, Ayesha all at the same table and go sit with them!"
    #show All
    player "Did Mitosis occur here? I could’ve sworn I was supposed to meet two of you here"
    show Alaina
    alaina "Hardy Har har, we just happened to bump into each other and thought we’d all enjoy lunch together hehe~~"
    hide Alaina
    player "Well it’s great to see all my favorite people on one table so I’m not complaining"
    "You all start to eat and talk when you suddenly sigh after a few minutes"
    show Asad
    asad "You good [playerName]?"
    hide Asad
    
    menu:
        "Yeah, just tired of the annoying people I have to tolerate everyday":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_6_1 from _call_node_6_1

        "It’s nothing, let’s just eat":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_6_2 from _call_node_6_2

        "Just mind your own business and leave me alone for a while okay?":
            $ relationKeeper(chapter0_network, currentNode, "Choice3")
            call node_6_3 from _call_node_6_3

    call node_7 from _call_node_7

    return

label node_6_1:
    #relation all + 2
    show Asad
    asad "Ohhh, you wanna talk about it?"
    hide Asad
    menu:
        "I’d rather not…":
            call node_6_1_1 from _call_node_6_1_1
        "It’s just these few people bullying me and I’m started to grow tired of it":
            call node_6_1_2 from _call_node_6_1_2
        "There’s a few people I’m considering murdering, I might actually do it":
            call node_6_1_3 from _call_node_6_1_3
    return

label node_6_1_1:
    #relation all + 0
    
    show Alaina
    alaina "Whatever makes you comfortable, but know that we’re all here for you any time you need to rant or anything okay?~~"
    hide Alaina
    player "Yeap, thanks guys…love you all so much"
    "You all continue eating your food but the mood is sour at the table"
    return

label node_6_1_2:
    #relation all + 2
    
    "You continue to talk about the people bullying you in university that you can’t do anything to"
    "Your friends listen to you and after you’re done ranting, everyone consoles you and reassures you that they’ll help you fight off these bullies"
    "Reassured and seeing everyone so concerned for your well-being, you spring back to life and make a joke to lighten the mood"
    "Everyone laughs and you all continue enjoying your lunch"
    #show images of everyone laughing
    return

label node_6_1_3:
    #relation all -2
    
    show Alaina
    alaina "Hehe, [playerName], you’re joking…right?"
    hide Alaina
    player "I really hope I was"
    show Ayesha
    ayesha "Listen [playerName] if something is bothering you please tell us but please don’t make bad jokes like these, lives are not something we can throw away so easily even if they inconvenience us"
    hide Ayesha
    player "..."
    player "Okay fine, my bad, sorry."
    show Ayesha
    ayesha "Nice to see that you understand"
    hide Ayesha
    "The mood at the table is awkward as you all try to finish your lunch after the scene that happened"
    return

label node_6_2:
    #relation all +0
    show Ayesha
    ayesha "You sure? You can always talk to us you know, we’ll always be here for you…"
    hide Ayesha
    menu: 
        "No it’s cool. I know I can trust you guys. I’ll be sure to let y’all know if something is up":
            call node_6_2_1 from _call_node_6_2_1
        "Please, just leave me alone for a while to manage my stuff okay? No need to be so nosy where y’all don’t belong":
            call node_6_2_2 from _call_node_6_2_2
        "I guess I could tell you guys…":
            call node_6_2_3 from _call_node_6_2_3
    return


label node_6_2_1:
    #relation all +1
    
    show Alaina
    alaina "Whatever makes you comfortable, but know that we’re all here for you okay? If anything’s bothering you or you need help be sure to reach out m’kay?~~"
    hide Alaina
    player "Yeap, thanks guys…means a lot!"
    "You all continue eating your food but you feel uneasy"
    return 

label node_6_2_2:
    #relation all -2
    
    show Amil
    amil "Amil: “No need to lash out [playerName], she was just worried is all"
    hide Amil
    player "Yeah… sorry. Just… not in the right state of mind right now…"
    return

label node_6_2_3:
    #relation all +2
    
    "You tell everyone about the people bullying you in university and that you’re frustrated because of it"
    "Your friends listen to you and after you’re done ranting, everyone consoles you and reassures you that they’ll help you fight off these bullies"
    "Reassured and seeing everyone so concerned for your well-being, you spring back to life and Asad makes a joke which lightens the mood of the table."
    "Everyone laughs and you all continue enjoying your lunch"
    #show images of everyone laughing
    return

label node_6_3:
    #player image changes to angry
    #relation all -4
    
    show Alaina
    alaina "[playerName]…"
    hide Alaina
    show Amil
    amil "Wasn’t a nice thing to say but we’ll leave you to it"
    hide Amil
    player "Thanks, appreciate it."
    "The mood at the table became incredibly hostile and sad, everyone seems down and Asad feels sad because to hm it feels like he triggered you or something"
    return 


label node_7:
    $ currentNode = "node_7"
    "You all finish your lunch and everybody prepares to head for class. You still have time till your next class starts so you go to the Dhabba area to chill after you say goodbye to everyone"
    scene tapalOutside
    "As you’re going to the Dhabba Area, you bump into Bakhtawar and Zain"
    scene dhabba
    show John at left
    show Zayn at right

    player "Yo Bakhtawar and Zayn, what’s up!"
    john "Dude, for the hundredth time, it’s John, not Bakhtawar, I don’t use that name anymore."
    player "Fine fine, {i}John{/i}"
    john "Why do I smell sarcasm in there…"
    player "(smirks) Hmmm, I wonder"
    zayn "Dude, he’s obvio making fun of you"
    john "Huh. Not cool dude. Don’t you know I’ve been hitting the gym again lately? I’d lift you up and throw you into the Naala if I wasn’t so nice"
    zayn "AGAIN. Dude we get it, you gym hard, but please for the love of God stop telling us that"
    menu:
        "It’s cool, I’m interested in his gym routine":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_7_1 from _call_node_7_1
        "Yeah lmao stop using the gym as a personality trait":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_7_2 from _call_node_7_2
    call node_8 from _call_node_8
    return

label node_7_1:
    #relation John +2
    
    zayn "That’s a first I’ve heard someone say that"
    return

label node_7_2:
    #relation John -2
    
    john "Dude shut up or I’ll seriously throw you off a ledge or something"
    return

label node_8:
    $ currentNode = "node_8"
    zayn "Oh my God, I completely forgot about my singing lessons today at 8. I’m too tired to go today *sigh*"
    #show Zayn sad
    player "So Zayn, what kind of music do you like to listen to?"
    zayn "Honestly man anything pop gets me going, the only thing I despise is death metal music. What kind do you like?"
    menu:
        "Same as you, a pop fan":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_8_1 from _call_node_8_1
        "Eastern music mostly":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_8_2 from _call_node_8_2
        "EDM stuff is what I jam to":
            $ relationKeeper(chapter0_network, currentNode, "Choice3")
            call node_8_3 from _call_node_8_3
        "Death Metal!!":
            $ relationKeeper(chapter0_network, currentNode, "Choice4")
            call node_8_4 from _call_node_8_4
    call node_9 from _call_node_9
    return

label node_8_1:
    #relation Zayn +2
    
    zayn "Ayyy man, gang gang"
    return 

label node_8_2:
    #relation Zayn +1
    
    zayn "Ahhh sitars and tablas, nice, the classics"
    return 

label node_8_3:
    #relation Zayn +1
    
    zayn "Ayyy party music, love it!"
    return

label node_8_4:
    #relation Zayn -2
    
    zayn "Ouch…sorry for your loss"
    return

label node_9:
    $ currentNode = "node_9"
    player "So what’re you guys up to?"
    john "Gonna hit the gym, wanna join me?"
    zayn "Gotta go practice the violin, how about you come with and I teach you too?"
    menu:
        "Go to the gym with John":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_9_1 from _call_node_9_1

        "Go to the music room with Zayn":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_9_2 from _call_node_9_2

        "Stay here by yourself":
            $ relationKeeper(chapter0_network, currentNode, "Choice3")
            call node_9_3 from _call_node_9_3
    call node_10 from _call_node_10
    return

label node_9_1:
    #relation John +3
    
    player "Guess I’ll hit the weights"
    scene gym
    "You gym for a while then freshen up and go to your classes"
    return

label node_9_2:
    #relation Zayn +3
    
    player "Guess I’m learning the violin today"
    scene musicRoom
    "You go to the music room, play the violin horribly for a while then go to your classes when time comes"
    return 

label node_9_3:
    #relation both +0
    
    "John and Zayn both leave. You stay there, bask in the sun and wait till it’s time for your classes. Once it is, you go to your classes"
    return 

label node_10:
    $ currentNode = "node_10"
    scene classroom
    "Your leftover classes resume"
    "Before you even know it, all of your classes have ended and it's evening already"
    scene gardenDhabba
    "You go out to the garden area to grab some of Rahim Bhai's fries before leaving"
    "You notice that it's the time of the year when evenings are really dark"
    "You quickly grab your fries and go to the Courts Area to watch some sports"
    scene courts
    "The Courts Area is an area with Basket Ball and Tennis Courts and across that a place to sit so people can come and enjoy the sports with their friends"
    "As you're passing by the nets, your eyes cross that of someone who'd be the last person you'd want to see at the end of such a tiring day"
    "Your eyes meet Ahsen's..."
    show Ahsen
    ahsen "(Comes over by the net) Here to tell the teacher that I’m playing basketball, [playerName]?"
    player "Look, I only did that because you were being manipulative of the club as president and the members were not happy. I was forced to involve the teachers"
    ahsen "Save the excuses for someone else, I know you were just jealous of my leadership and couldn’t bear to see the spotlight on someone else than yourself."
    player "But I was just a freshie then, why would I feel jealous of anything. I didn’t even know who was who until the whole incident happened"
    ahsen "Listen, if you so even try to come near me or try to ruin my reputation again, I will do something so bizarre even…"
    "Just as Ahsen is about to go wild, Sean shows up"
    hide Ahsen
    show Sean
    show Ahsen at right
    sean "Hey Ahsen, you gonna play or just threaten people? Come on, it’s your turn on the field"
    "Ahsen angrily leaves, cursing at you under his breath"
    hide Ahsen
    sean "Seems like he was about to have a meltdown"
    player "Yeah, he has those whenever he sees me. He was abusing his power as club president a while back and I got SL and the professors involved which made him look really bad so he despises me for it. Anyway thanks for helping me!"
    sean "Any time man! It’s been a while since we’ve talked, what’s up nowadays"
    menu:
        "Uhhh nothing. I should leave.":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_10_1 from _call_node_10_1

        "You know the same old same old; trying to just pass the semester and failing miserably":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_10_2 from _call_node_10_2
    "You wave to Sean and leave"
    hide Sean
    scene habibInside with fade
    "You get into your car and drive back home"
    scene bedroom with fade
    "You finally reach home and drop dead on the bed. You ponder over all that happened today and as you’re dreaming, you fall asleep"
    stop music
    scene black with fade
    call node_11 from _call_node_11
    return

label node_10_1:
    #relation Sean -2
    
    sean "Uhhh okay, if you say so. Bye!"
    return 

label node_10_2:
    #relation Sean +2
    
    sean "Hahaha I know what you mean. Playing sports is the only thing that keeps me sane in this stressful time. You should give it a try too"
    player "Not really much of a sports player anymore after I discovered how bad I was"
    sean "That’s sad to hear"
    "You both keep talking till someone calls Sean back into the game"
    sean "Guess that’s my cue, see ya later. It was fun talking to you again, we should hangout again sometime like we used to"
    player "Totally, see you later!"
    return 

label node_11:

    call node_12 from _call_node_12
    return

#CHAPTER ZERO END------------------------------------------------------------------------------------------------------------------------------------------------------------



















#CHAPTER ONE START-----------------------------------------------------------------------------------------------------------------------------------

label node_12:
    $ currentNode = "node_12"
    
    scene black
    "The next day starts and you wake up to an extremely tiring morning."
    scene bedroom with fade
    play music "chp01music.mp3" loop
    "You feel as though you’ve lost all the energy you previously had because of how stressful your previous days have been."
    "Reluctantly you get out of bed and get ready to head out for university"
    scene driving
    "You take out your car and drive to university."
    scene basement
    "You get out and head upwards."
    scene habibInside
    "Upon reaching there you see familiar faces waiting for you."
    show Alaina at right
    show Asad at left
    alaina "Hey [playerName]!! How’re you doing today?~~"
    asad "Looks the same to me, not gonna lie"
    menu:
        "Hey guys! It’s been a really bad morning, but thanks for being here, just seeing you all again is so soothing for me right now":
            $ relationKeeper(chapter1_network, currentNode, "Choice1")
            call node_12_1 from _call_node_12_1
        "Ughhh, I don’t have the energy to talk right now, sorry.":
            $ relationKeeper(chapter1_network, currentNode, "Choice2")
            call node_12_2 from _call_node_12_2
    call node_13 from _call_node_13
    return 

label node_12_1:
    #relation +2 all
    alaina "*smiles* Well what are friends for?~~"
    "You smile in return"
    return 

label node_12_2:
    #relation -2 all
    "You walk away while your friends sadly look at you in awe, unable to understand why you’re so distant today."
    "They catch up to you and walk beside you. Slowly you start talking."
    return

label node_13:
    $ currentNode = "node_13"
    scene central
    "As you talk to your friends, you all walk towards your classes. You all stop at Central Street, say your goodbyes and all go your ways"
    hide Alaina
    hide Asad
    scene classroom
    "You take your classes as usual and after they are over, you prepare to go to Tapal Cafeteria to meet your friends for lunch"
    scene central
    "As you’re preparing to go there, you meet Adam…"
    show Adam
    adam "(smirks) Hey small-fry"
    player "Ugh…What do you want?"
    adam "Show some respect or I’ll beat it into ya"
    player "(smiles sarcastically) Yesss sweety? Do you want something? :)"
    adam "As a matter of fact I do. Have you done the Calculus homework?"
    player "Of course, I was just about to submit it."
    adam "Show it to me"
    menu:
        "Why would I do that?":
            $ relationKeeper(chapter1_network, currentNode, "Choice1")
            call node_13_1 from _call_node_13_1
        "Sure thing!":
            $ relationKeeper(chapter1_network, currentNode, "Choice2")
            call node_13_2 from _call_node_13_2
    call node_14 from _call_node_14
    return 

label node_13_1:
    
    "Adam grabs your shirt’s collar and threatens you to show it to him"
    return

label node_13_2:
    
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
    hide Adam
    "You get up and dust yourself"
    "Panicking about the work due in an hour you consider your options"
    menu:
        "Go to the library and try to get done with your work":
            $ relationKeeper(chapter1_network, currentNode, "Choice1")
            call node_14_1 from _call_node_14_1
        "Call Amil and ask for help!":
            $ relationKeeper(chapter1_network, currentNode, "Choice2")
            call node_14_2 from _call_node_14_2
    call node_15 from _call_node_15
    return

label node_14_1:
    #relation -1 all
    "You call your friends and tell them that there’s been an emergency and that you won’t be able to make it today"
    "They are sad to hear this but they understand something important might’ve come up"
    "You hurry to the library and start working there"
    scene infoCommons with fade
    "You keep on working for almost 50 minutes and barely reach the faculty pod in order submit your homework submission"
    scene stairsDownwards
    "After you’ve submitted it, you breathe a sigh of relief"
    return 

label node_14_2:
    #relation +3 all
    player "Hey Amil, so a scene happened and now I have to redo my entire Calculus homework in less than an hour. Can you help me out?"
    amil "Of course mate, come on over to Tapal and we’ll sort it out"
    "You go to Tapal…"
    scene tapal with fade
    show Amil at right
    show Asad at left
    "…and see Amil and Asad there"
    player "Guys I’m in a real pinch, Adam took my homework and now I have to do it right now"
    amil "Don’t worry mate, I’ve done it a ton of times, it’s very easy!"
    "Amil helps you solve the assignment very quickly! Asad explains concepts which he knows in order to improve your understanding. You all collectively work on it for 30 minutes and once it’s finished, you go and submit it."
    scene stairsDownwards
    "You thank Amil and Asad for helping you throughout the process and you all hug!"
    return 

label node_15:
    $ currentNode = "node_15"
    "As you breathe a sigh of relief, you remember you used up your entire break time to re-solve the Calculus homework. Angrily you head back to your classes after saying goodbye to everyone"
    scene classroom with fade
    "The class ends"
    scene central with fade
    "As you’re going to your next class, you see Shanzayy staring angrily at you and then at Adam who’s standing on the other side of Central street"
    show ShanzayyAngry
    shanzayy "..."
    "You try to ignore her and go away from there"
    scene classroom
    "After your classes end, you tiredly go towards the basement area so that you can finally drive yourself back home"
    scene basement
    "As you’re heading to the basement, you hear…"
    play sound "scream.mp3"
    stop music
    "SOMEONE SCREAM!"
    play music "chp3music.mp3" loop
    "Trying to track the source of the scream, you see Shanzayy lying on the ground sobbing hardly"
    stop sound
    show ShanzayyHappy
    player "Shanzayy… Shanzayy…SHANZAYY"
    "You scream as you try to shake her out of her crying daze"
    menu:
        "Stop crying dammit. Shut up and tell me what’s wrong":
            $ relationKeeper(chapter1_network, currentNode, "Choice1")
            call node_15_1 from _call_node_15_1
        "Shanzayy? Are you alright Shanzayy? What’s wrong? Come on tell me.":
            $ relationKeeper(chapter1_network, currentNode, "Choice2")
            call node_15_2 from _call_node_15_2
    call node_16 from _call_node_16
    return

label node_15_1:
    "Shanzayy looks at you shocked, unable to understand what you just said to her and she starts crying even more"
    return

label node_15_2:
    "You say as you try and shake her out of her shocked state"
    "She looks at you, and embraces you unable to say anything"
    return


label node_16:
    $ currentNode='node_16'
    "You look around to see a strange mound beside your car"
    hide ShanzayyHappy
    stop music
    play music "deathscenemusic.mp3" loop
    "As you leave Shanzayy’s side to look into it further, you’re overwhelmed with the sight before you. Your eyes cannot believe themselves. It’s the body of Adam, lying beside your car, seemingly dead."
    #murder scene 1
    "You try to move him, but he is indeed dead."
    "You think of investigating but start to consider its consequences"
    menu:
        "I don’t know whether I can handle this much gore or not. (Don’t investigate)":
            $ relationKeeper(chapter1_network, currentNode, "Choice1")
            call node_16_1 from _call_node_16_1
        "I need to get to the bottom of this. (Investigate)" :
            $ relationKeeper(chapter1_network, currentNode, "Choice2")
            call node_16_2 from _call_node_16_2
    call node_17 from _call_node_17
    return

label node_16_1:
    "You decide not to investigate and instead back away from the scene of the murder"
    return

label node_16_2:
    "You investigate the body to find…"
    "His collar is bunched up and his throat has been slit” “You also notice his head has been bashed"
    "You also see the door of your car unlocked for some reason, even though you just arrived here"
    "You also find a note beside him…"
    show murderNote1 at truecenter
    "You open the note to have it read ‘Hope you get good marks on your Calculus homework :)’"
    "Reading this note sends shivers down your spine and you decide to stop investigating further"
    hide murderNote1
    return


label node_17:
    $ currentNode='node_17'
    show ShanzayyHappy
    "You stand up and console Shanzayy enough that she can stand and go with you"
    "You both leave the scene and exit the basement"
    "As soon as you’re exiting the basement you meet Asad and John"
    hide ShanzayyHappy

    show Asad at left
    show John at right
    asad "[player] why are your clothes bloody like that…"
    john "And why is Shanzayy crying…"
    "You explain to them everything you witnessed. Shanzayy’s screams, the murdered body of Adam and everything else"
    asad "Oh my God, we need to report this to campus security immediately"

    $ Johnrelation = relationshipDict['John']
    $ value=50
    if Johnrelation > value: #John (automatic)
        $ relationKeeper(chapter1_network, currentNode, "Choice1")
        call node_17_1 from _call_node_17_1
    else:
        $ relationKeeper(chapter1_network, currentNode, "Choice2")
        call node_17_2 from _call_node_17_2
    call node_18 from _call_node_18
    return

label node_17_1:
    john "Yeap, let’s go immediately. We can’t waste any time on this."
    return

label node_17_2:
    john "Nahhh man, I’m out of this murder fiasco, you guys are on your own"
    hide John
    return

label node_18:
    $ currentNode='node_18'
    stop music
    play music "chp3music.mp3" loop
    "You all head to the campus security office, where you explain everything that happened. They go to the scene of the crime, close it off, issue a gag order and tell you not to tell anyone about this"
    scene securityRoom with fade
    "Both you and Shanzayy are comforted by Asad. Shanzayy’s friend volunteers to drop her off while Asad volunteers to drop you off at your home"
    "You, still shaking, get into Asad’s car and he drops you off at your home"
    scene livingRoom with fade
    "You enter your home, explain everything to your parents and go isolate yourself in your room"
    scene bedroom with dissolve
    "While trying to make sense of everything that just happened, you receive a group call from all your friends"
    menu:
        "Pick up the phone and talk to them":
            $ relationKeeper(chapter1_network, currentNode, "Choice1")
            call node_18_1 from _call_node_18_1
        "Ignore their call and go to sleep":
            $ relationKeeper(chapter1_network, currentNode, "Choice2")
            call node_18_2 from _call_node_18_2
    call node_19 from _call_node_19
    return

label node_18_1:
    # $ stress-=4
    "You talk to your friends and tell them about everything that happened. They console you and try to help you feel better about the weird situation."
    "After talking to them for a while, you feel slightly relaxed. You say your goodbyes and sleep after ending the call"
    scene black with dissolve
    return
label node_18_2:
    # $ stress+=4
    "The eerie thoughts keep gnawing at your sanity, soon you’re having anxiety attacks thinking about the entire scene of the murder"
    "Tired from all the mental exhaustion, you slowly drift away into a stressful slumber"
    scene black with dissolve
    return


label node_19:
    $ currentNode='node_19'
    stop music
    
    #scene change black
    "..."
    scene white with dissolve
    scene black with dissolve
    scene white with dissolve
    scene black with dissolve
    scene white with dissolve
    play music "hospitalbg.mp3"
    scene hospital
    show Nurse
    nurse "Doctor he’s regaining consciousness, what do we do?"
    hide Nurse
    show Doctor
    doctor "Inject him with 50 micrograms of Fentanyl, 110mg of Propofol, and 30mg of Rocuronium. Wait 15 seconds and then 5 mg of Morphine."
    hide Doctor
    "The Nurse injects you with weird concoctions until you start to feel you head feel lighter than before…and you slowly…start to drift away again…"
    stop music
    scene black with dissolve
    scene bedroom with fade
    "You suddenly wake back up in your room in cold sweats and scream"
    player "AHHHH"
    "You look around to see that you are in your room, as when you fell asleep"
    player "Weird dream…What was that…"
    "As you start to ponder over what you saw, you fall asleep again…"
    
    scene black with dissolve
    call node_20 from _call_node_20
    return


#CHAPTER ONE END-------------------------------------------------------------------------------------------------------------------------------

























#CHAPTER 2 START-------------------------------------------------------------------------------------------------------------------
label node_20:
    $ currentNode = "node_20"
    scene bedroom with fade
    play music "chp2music.mp3" loop
    "You wake up with blurry eyes, unable to recognize what’s happening around you."
    "Your eyes focus to your empty bedroom. It takes a while before you’ve regained your consciousness properly. As soon as you do, you’re reminded of the unnerving scene which you witnessed yesterday."
    player "(sighs) Guess I should get ready..."
    "You sigh again"
    "And before you know it, you're at Habib again."
    scene habibInside with fade
    scene central with fade
    player "Why is it so quiet?"
    "You ponder to yourself as you enter campus expecting drama and screaming people."
    #scene changes to central street
    player "Why isn't there more....more...."
    
    aaron "Drama, action, media and publicity?"
    "You turn around to see Aaron behind you"
    show Aaron
    player "Yeah…I mean, someone did die, I thought there’d be more people concerned about it."
    aaron "Ahhhh naïve young little boy."
    player "What...?"
    aaron "Didn’t you know? Adam was always the family disgrace. Mediocre grades, mediocre extra-curricular activities, thuggish behavior and always made a laughing stock of the entire Zaidi family. He caused them more trouble than he was worth."
    player "Yeah so?"
    aaron "Sooo, my young stupid child, his father wanted him gone anyway. In fact, if he wasn’t the gentle man he is, he would’ve kicked him out of the family. Him dying was like a sigh of relief for Adam’s father. The child not wanted, finally gone." 
    aaron "And he didn’t even have to lift a finger to do it. It just happened for him. So he cut a deal with Habib. Habib doesn’t go public with this murder, Habib saves face, his dad gets off a dead weight, Habib issues a hush order to stop the flow of information, everyone wins, and no one loses."
    player "Dude…that is seriously messed up…"
    aaron "Not as messed up as Adam’s manners might I add though, hahahaha"
    player "Are you seriously laughing at someone dying? You have no morals, do you?"
    aaron "Please, you’re the last person I want to hear this from, mister ‘I was just visiting by as my college bully was found dead beside my car"
    player "Look, I had nothing to do with it okay? Shanzayy was there before me, and she mentioned seeing no one before her."
    aaron "True, doing something like this would require guts which you don’t have. Maybe it was John after all."
    player "Wait, wait, WHAT? What do you mean by ‘Maybe it was John after all’?"
    aaron "(sigh) John had issues with Adam. Adam was jealous of John’s new car. Apparently in angst and spite of it, he scratched it. John became super pissed, gave him death threats and everything. Told Adam that he’d actually murder him if he ever messed with his car again."
    player "Ohhhh. Which car does he have by the way?"
    aaron "A red Toyota Supra from what I’ve heard. Apparently it belonged to some racer and he got it imported from there."
    player "..."
    aaron "What’s wrong? Car too expensive for you to understand?"
    player "Ye-Yesterday…beside my car…John’s car…was parked beside my car…"
    aaron "Well there you have it. Guess he followed through."
    player "I can’t believe it…"
    aaron "Well take your time shortcake. I’m off to soccer practice. Ciao."
    hide Aaron
    player "Y-Yeah..."
    "You’re trying to process everything when suddenly Sean yells…"
    show Sean
    sean "Oh my God [playerName]"
    hide Sean
    show Sean at right
    show Zayn at left
    "You see Sean and Zayn walking by together"
    sean "Are you okay? I heard you got involved with something unpleasant. Maybe you should’ve taken the day off today."
    zayn "Heck yeah mannn, no one should have to come to uni after an incident like that oooh."
    menu:
        "I’m fine, I’d rather be here than alone with my thoughts at home after what I saw":
            $ relationKeeper(chapter2_network, currentNode, "Choice1")
            call node_20_1 from _call_node_20_1
        "It’s my choice whatever I do with my life, do y’all both have to butt in??":
            $ relationKeeper(chapter2_network, currentNode, "Choice2")
            call node_20_2 from _call_node_20_2
    call node_21 from _call_node_21
    return

label node_20_1:
    #relation +2 zayn, sean
    zayn "Yeah mannn, totes get you bruh. It’d hard to process seeing a dead body."
    sean "ZAYN, you’re not supposed to say it out like that geez!"
    zayn "Ahhh damn, my bad man, sorry."
    return

label node_20_2:
    #relation -2 zayn, sean
    zayn "Yikesss, sorry man, didn’t mean to be mean"
    sean "Yeah man, sorry if we hurt you or something, we’re just concerned."
    return 

label node_21:
    $ currentNode = "node_21"
    player "…it’s cool"
    sean "So man, what’re you gonna do now? I mean it’s probably hard to move on right?"
    zayn "Wow, who’s asking the intrusive questions now?"
    sean "(laughing) Shut up dude."
    "Seeing them banter like that, you start to giggle too"
    player "don’t know man. Most probably will try to get my sanity back, however much I can."
    zayn "Yeah man, baby steps. Hit me up if you ever wanna talk or something."
    sean "Same man."
    player "Thanks guys"
    "You three talk some more, before Zayn and Sean realize they had to go to their classes. You finish up the conversation quickly and they leave."
    zayn "Bye man!!"
    sean "Bye [playerName]!"
    hide Sean
    hide Zayn

    player "Bye guys!"
    "You decide to go to the area outside Tapal cafeteria to study"
    scene stairsDownwards with dissolve
    "As you’re on the way, you come across Ahsen."
    show Ahsen
    ahsen "My oh my, why if isn’t the murderer of Warren Street."
    player "I’m not the fascist here Ahsen, you are."
    ahsen "At least I’m no murderer you blood sucker."
    menu:
        "Calling me a vampire, when you’re the pale-dead looking one? Hahaha":
            $ relationKeeper(chapter2_network, currentNode, "Choice1")
            call node_21_1 from _call_node_21_1
        "Look dude, I’m not the murder! WHY IS EVERYONE ACCUSING ME?":
            $ relationKeeper(chapter2_network, currentNode, "Choice2")
            call node_21_2 from _call_node_21_2
    call node_22 from _call_node_22
    return

label node_21_1:
    #stress -2
    #relation -2 Ahsen
    ahsen "Ahhh is my fancy white color why you despise me so much you filthy muggle?"
    player "Racist much Ahsen?"
    ahsen "Not in the least [playerName]"
    return

label node_21_2:
    #stress +3
    #relation -2 Ahsen
    ahsen "The dude had an obvious connection to you, who else would kill him? Bigfoot?"
    player "Like I’ve been explaining to people since morning, I just got to the scene of the crime, I did not kill him!"
    ahsen "Keep telling yourself that!"
    return

label node_22:
    $ currentNode = "node_22"
    player "*sighs* Could you please be nice for once? I’m going through a lot right now?"
    "Ahsen just takes advantage of you being down, and used it to push down harder on you."
    "Ahsen starts screaming."
    ahsen "GOING THROUGH A LOT? A LOT? WHAT ABOUT WHEN YOU MADE MY LIFE MISERY FOR 6 WHOLE MONTHS? WHEN THE PROFESSORS REFUSED TO EVEN ACKNOWLEDGE MY EXISTENCE?"
    player "Nothing of the sort happened. Stop screaming about it."
    ahsen "AHHH YES. YOU DO WHATEVER YOU WANT AND WHEN SOMEONE TRIES TO SPEAK UO YOU GASLIGHT THEM. REALLY NICE, REALLY NICE [Player]. NEXT THING YOU KNOW YOU’RE GONNA ASK ADAM’S PARENTS NOT TO SCREAM BECAUSE IT MAKES YOU FEEL BAD?? WELL BOOHOO"
    "You’re about to start sobbing from all the screaming."
    ahsen "WHO’RE YOU GONNA MURDER NEXT HUH? THAT DUDE FROM YOUR CALCULUS CLASS? OR THAT TEACHER'S ASSISTANT YOU DON’T LIKE. COME TELL ME HUH! {b}WHO? WHO?{/b}"
    "You try extremely hard to stop yourself from dropping just there and crying."
    player "..."

    hide Ahsen
    show Amil at right
    show Asad at left
    amil "Tormenting an already down man? How Draco Malfoy of you, Ahsen."
    asad "You’d think Draco would get a life after the whole fiasco he had. Guess it’s true when they say ‘You can never straighten a dog’s tail'."
    amil "Exactly!"
    player "Guys...."
    hide Amil
    hide Asad
    show Ahsen
    ahsen "Well if it isn’t Shaggy and Scooby, here to save the day!"
    hide Ahsen
    show Amil
    amil "Indeed! I just hope there’s no office involved in saving the day this time, if you know what I mean."
    "Amil winks"
    hide Amil
    show Ahsen
    ahsen "Pfffft, I’m outta here. Have a good day you gorillas."
    hide Ahsen
    "Noticing that since other people are here now, and that he won’t be able to manipulate you, Ahsen leaves the scene"
    player "T-Thanks guys…"
    show Asad at left
    show Amil at right
    asad "(smiles) What're friends for?"
    amil "Exactly!"
    "You all talk to each other for a few minutes and then decide to go to the Dhabba to get some fries."
    asad "Let's goooo!"
    scene dhabba
    "You guys order fries and as they’re being prepared, you excuse yourself for a few minutes."
    player "Guys I’ll be back, just gonna go to the washroom real quick."
    show Amil
    amil "Sure, we’re gonna be waiting here."
    hide Amil
    player "Cool!"
    "You go to the washroom…"
    scene tapalOutside
    #scene change to washroom
    scene black with dissolve
    scene black with dissolve
    scene black with dissolve
    scene black with dissolve
    scene black with dissolve
    scene black with dissolve
    scene black with dissolve
    scene black with dissolve
    # scene black with dissolve
    # scene black with dissolve
    #black screen for 5 seconds
    #scene change back to washroom
    scene tapalOutside
    "You finally go back to the Dhabba."
    scene dhabba
    player "Hey, I’m back!"
    show Asad at left
    show Amil at right
    asad "Took you long enough, you were gone for fifteen-ish minutes."
    player "Whattttt? Nooo?"
    asad "Yeah lol, you were...."
    menu:
        "Wow, I didn’t notice. Oops, sorry.":
            $ relationKeeper(chapter2_network, currentNode, "Choice1")
            call node_22_1 from _call_node_22_1
        "Mind your own business okay, I can stay however long I want":
            $ relationKeeper(chapter2_network, currentNode, "Choice2")
            call node_22_2 from _call_node_22_2
    call node_23 from _call_node_23
    return

label node_22_1:
    #relation +3 Asad, Amil
    asad "Hahaha it’s cool, we were just worried is all"
    amil "Yeap..."
    player "Thanks for caring guys! But I'm cool. Love you! "
    asad "Love ya too!"
    amil "Likewise!"
    return

label node_22_2:
    #relation -3 Asad, Amil
    amil "Of course friend, we were just worried is all."
    asad "Yeah man, that’s all"
    player "Yeah sure, thanks…"
    return 

label node_23:
    $ currentNode = "node_23"
    "You all start chatting again."
    "As you’re chatting, Asad finishes his fries and utters that he wants to eat some Makai next"
    asad "Guys let’s go to Learn courtyard!, I really wanna have some Makai right now!"
    player "Sure!"
    amil "Let’s make a dash through Earth Courtyard; it’ll be closer to go from there."
    player "Sure, that’s fine by me."
    "You all start walking towards Learn Courtyard."
    scene central2
    "You finally reach Earth Courtyard."
    scene earthCourtyard
    #Scene change Earth courtyard
    "…and see Ahsen with his face submerged in the Earth Courtyard fountain’s water."
    "Asad decides to tease Ahsen."
    show Asad at left
    asad "Hey man! This is no place to wash your face!"
    "Amil decides to chime in!"
    show Amil at right
    amil "Yeah man, there’s better ways to get that permanent grime off your face, hahaha."
    "…while you stand there awkwardly thinking about the scene that happened earlier…"
    "They both tease him for a few minutes, but he doesn’t reply."
    player "Uhhhh guys…how long has he been submerged in that water?"
    amil "We’ve been taunting him for 5 minutes straight."
    asad "Oh My God get him out!!!"
    stop music fadeout 0.5
    "You run and pull his face out of the water…only to see…"
    "HIS FACE HAS BEEN BADLY BASHED AND IS BLEEDING."
    play music "deathscenemusic.mp3" loop
    player "GUYS!"
    "Amil checks for a pulse but Ahsen’s long gone"
    amil "Dead…"
    player "WHAT IS HAPPENING"
    "You suddenly scream. Amil and Asad start looking concerned too."
    player "Guys we should…"

    menu:
        "See if there are any clues nearby (Investigate)":
            $ relationKeeper(chapter2_network, currentNode, "Choice1")
            call node_23_1 from _call_node_23_1
        "Forget everything and call campus security (Don’t investigate)":
            $ relationKeeper(chapter2_network, currentNode, "Choice2")
            call node_23_2 from _call_node_23_2
    call node_24 from _call_node_24
    return

label node_23_1:
    $ currentNode = "node_23_1"
    "As you eye around, you see a note which gives off a very familiar feeling."
    show murderNote2 at truecenter
    "You open it and the note reads: ‘No, you’re next :)’"
    "Reading this sends shivers down your spine."
    "It’s just like the note from before… what is happening… why is this happening…"
    "You investigate further and notice that Ahsen’s head was bashed with a rock. You find a bloodied rock nearby!"
    player "Guys look! That’s probably what was used to break Ahsen’s face in!"

    #This is an example of a bonus scene, made automatically if you have enough relations
    $ Asadrelation = relationshipDict['Asad']    
    $ value=72
    if Asadrelation > value: #Asad (automatic)
        $ relationKeeper(chapter2_network, currentNode, "Choice1")
        $ asadInvestigate=True
        call node_23_1_1 from _call_node_23_1_1
    else:
        $ relationKeeper(chapter2_network, currentNode, "Choice2")
        $ asadInvestigate=False
        call node_23_1_2 from _call_node_23_1_2

    return

label node_23_1_1:
    asad "Wait! Don’t touch it!"
    "Asad pulls into his bag and pulls out a weird kit-box. From inside it, he pulls out a scraping knife and a collection disk."
    amil "Uhhh Asad, why do you have that…?"
    asad "I was supposed to go collect insect and soil samples later for my biology course project, but I guess we’ll use it for this now"
    "Asad scrapes the blood and hair samples from the rock and Ahsen’s bloodied face and clothes, and stores them in a closed petri dish"
    asad "I have a guy, in the hacker network; I’ll try giving these to him to see what’s possible but I can’t promise anything for now."
    player "Y-Yeah…thanks…"
    "Amil holds your shoulder to console you."
    amil "Don’t you worry; we’ll get together this…somehow."
    player "Thanks man…"
    "You both nervously smile at each other."
    "Amil further analyses the situation."
    amil "From the look of the place where he was hit by the rock, it seems that the height of the murder was close to Zayn’s, mine and yours [player]"
    amil "Furthermore there must be prints on the rock right?"
    asad "Sorry, I couldn’t find any."
    amil "Ahhh. Oh well, there goes that trail..."
    "You all try to find more clues but when you’ve exhausted every option, you all decide to go to campus security."
    player "Let’s call the security guys; this is out of our hands now"
    "Asad quickly hides all the DNA samples he collected and you all go to the campus security office."
    return


label node_23_1_2:
    "You pick up the rock, but unsure of what to do with it, you put it back…"
    "Amil further analyses the situation."
    amil "From the look of the place where he was hit by the rock, it seems that the height of the murder was close to Zayn’s, mine and yours [player]"
    amil "Furthermore there must be prints on the rock right?"
    asad "We have no way of knowing right now"
    amil "Ahhh. Oh well, there goes that trail…"
    "You all try to find more clues but when you’ve exhausted every option, you all decide to go to campus security."
    player "Let’s call the security guys; this is out of our hands now"

    return

label node_23_2:
    player "Let’s call the security guys; this is out of our hands. Not one but two murders? This is getting crazy and I am not in a mental condition to deal with it right now."
    amil "Yeah, let’s get out of here quick. I can’t bear looking at that body anymore"
    "You all leave the scene and go to the campus security office in order for them to take care of the matter."
    return


label node_24:
    $ currentNode = "node_24"
    scene securityRoom with fade
    "You reach the security office and explain everything to them in detail. How you saw Ahsen’s body submerged in water, how you pulled him out and everything afterwards."
    "Campus security follows you to the scene at Earth Courtyard where a bunch of students have already gathered."
    scene earthCourtyard with fade
    "There you show them the body and how you discovered it."
    "Listening to this, everyone suddenly starts giving you weird looks as they already suspected you to be involved in the basement murder."
    "Seeing all this commotion and the uneasiness of people around you, you run and flee from the scene which makes everyone suspect you even more."
    "Within a few minutes, everyone has started giving you weird looks. Your bloodied shirt gives everyone the wrong impression so you try to get away from everyone as soon as possible and dash for the courts area to be alone."
    scene courtsNight
    stop music fadeout 0.5
    play music "chp2music.mp3" loop
    "When you reach there, you see Shanzayy on her phone. She looks up from her phone and sees you."
    show ShanzayyAngry

    $ Shanzayyrelation = relationshipDict['Shanzayy']
    $ value=42
    if Shanzayyrelation > value: #Shanzayy (automatic)
        $ relationKeeper(chapter2_network, currentNode, "Choice1")
        call node_24_1 from _call_node_24_1
    else:
        $ relationKeeper(chapter2_network, currentNode, "Choice2")
        call node_24_2 from _call_node_24_2

    call node_25 from _call_node_25
    return

label node_24_1:
    hide ShanzayyAngry
    show ShanzayyHappy
    shanzayy "H-Hey…"
    player "Hey…"
    shanzayy "So I heard…"
    
    player "And you think I’m a cold-blooded killer too?"
    shanzayy "Contrary to popular belief right now, I know how great of a guy you are."
    "You’re shocked to hear these words, especially at a time like this that too from Shanzayy."
    player "W-W-Wha-…"
    shanzayy "I mean it. Even though I was always mean to you, you were kind to me. If that’s not the definition of a nice person I don’t know what is."
    "Hearing these kind words from Shanzayy, you start to get teary eyes."
    shanzayy "You have great friends [player], I know you’ll get past this. I’m sure of it!"
    "Hearing all these sweet words, you’re extremely taken aback and left speechless."
    shanzayy "Stay in there [player]! I know you can!"
    player "Mhm…thanks…"
    shanzayy "I have to leave for home now, but I’m here for you okay? If you every wanna talk just call me or text me or whatever is easy for you okay?"
    
    player "Mhm, thanks…Shanzayy…"
    "Shanzayy smiles sweetly, probably the first time she’s smiled at you and afterwards, she leaves…"
    hide ShanzayyHappy
    return

label node_24_2:
    shanzayy "Oh My God, murderer…"
    player "Let me explain, it wasn’t m-"
    "You’re cut off by Shanzayy."
    shanzayy "NO! Everyone’s saying you’re the guy who killed them both and I will not stand here and be the third!"
    hide ShanzayyAngry
    "After saying this, she makes a dash for it and you’re left there alone sobbing, unsure of what to do or whether to even live or not."
    return



label node_25:
    "You stay there for a while, thinking back on everything that happened today, scared of what’s to come."
    "After a while, you decide to finally go home."
    "Avoiding any eye contact, you leave for home."
    scene livingRoom with fade
    #Scene change home
    "When you reach home you make a dash for your bedroom."
    scene bedroom
    "…and you collapse on the bed, unable to think of what to do next…"
    stop music fadeout 0.5
    scene black with dissolve
    call node_26 from _call_node_26
    return

#CHAPTER TWO END-----------------------------------------------------------------------------------------------------------------------------



















#CHAPTER THREE START----------------------------------------------------------------------------------------------------------------

label node_26:
    $ currentNode = "node_26"
    scene black with fade
    scene bedroom with fade
    "…"
    "………"
    "…………………"
    "Another day begins..."
    play music "chp3music.mp3" loop
    "You lack both the motivation and courage to get out of bed."
    player "Maybe I’ll just skip university for now…I have no clue what to do anymore…"
    "As you’re contemplating what you should do you pick up your mobile phone to see a message from Alaina that reads…"
    "Hey, [playerName]! I know you’re probably down today. I know this is a tough situation for you, but I’d love if you could try and make it to university today. I’m really looking forward to seeing you today hehe. Hope I get to talk to you lots~~"
    "Reading this message, you’re slightly more motivated and finally work up the courage to go to university today."
    scene livingRoom with dissolve
    "You’re listening to the news and you’re shocked to find no mention of anything related to the murder on the news…"
    scene black with fade
    "You finally reach the campus."
    scene habibOutside with fade
    #campus outside scene
    player "(sigh) Let's do this"
    scene habibInside with fade
    "As soon as you enter the campus, you can feel the unrest around you. This place no longer feels like a safe space. As you’re walking by, a few people start giving you weird looks."
    "Ignoring them you move ahead and try to find Alaina and your friends"
    "Trying to search for them you see Ayesha from the corner of your eye. You smile, only for it to fade away the next moment when you notice her crying in front of Aaron."
    scene central2
    
    "You’re taken aback by this scene. You’ve never seen Ayesha so vulnerable before. She’s pleading for something while Aaron keeps on yelling at her, getting louder and louder until Ayesha drops to the floor, her hands covering her face."
    "Using this as a cue Aaron leaves and comes in your direction. Angry at what you just witnessed, you confront him."
    show Aaron
    player "HEY! What’s the matter with you???"
    aaron "Get outta my face. Not in the mood to talk to a killer."
    "Aaron tries to leave but you grab his shoulder."
    "As soon as you do, he flips about and punches your face hard!"
    player "Ooomph"
    aaron "Don’t ever touch me again, dead weight."
    "Aaron says as he storms out of the scene angrily."
    hide Aaron
    $ stress += 4
    "Unable to say or do anything to him, you turn to Ayesha on the ground."
    player "Hey are you okay?"
    show Ayesha
    "Ayesha shakes her head saying no"
    player "Want to tell me what happened?"
    ayesha "I’m sorry [playerName], but I just need some space right now…"
    "She says, as she gets up, still hiding her face and she then leaves too."
    hide Ayesha
    "Unsure of what to do, you wait there, pondering, until you remember you have to get to class!"
    scene classroom with fade
    "Throughout your classes that scene of Ayesha crying keeps on playing in your head like a tape recording. As soon as it ends, it just rewinds and starts again."
    "Soon your classes end. As you’re leaving a class, you get a call from Asad."
    scene stairsDownwards with fade
    if asadInvestigate==True:
        $ relationKeeper(chapter3_network, currentNode, "Choice1")
        call node_26_1 from _call_node_26_1
    else:
        $ relationKeeper(chapter3_network, currentNode, "Choice2")
        call node_26_2 from _call_node_26_2
    call node_27 from _call_node_27
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
    scene dhabba with fade
    "As you're resting, you fall asleep."
    #show black screen
    scene black with dissolve
    scene white with dissolve
    scene black with dissolve
    scene white with dissolve
    scene black with dissolve
    scene white with dissolve
    scene dhabbaNight with dissolve
    #black and white flashes
    "Suddenly you see black and white flashes and you jump awake!"
    "It's dark outside"

    player "Ahhhhhhh"
    player "What was that??"
    "As you focus your eyes, you see someone lying in the grass."
    player "Guess I’m not the only one sleepy right now huh."
    "As you pay a closer look you notice it’s Aaron! And that he’s…lying on the ground very weirdly…"
    player "Oh no. Not this again…"
    stop music
    play music "deathscenemusic.mp3" loop
    "You go over to where Aaron is ‘sleeping’ and your suspicions are confirmed. He is… in fact… dead…"
    scene gardenMurderAreaNight
    player "AHHHH. THIS HAS TO STOP, WHO IS DOING THIS?"
    "You scream."
    menu:
        "I should investigate this. This needs to stop. Now. This is enough… (Investigate)":
            $ relationKeeper(chapter3_network, currentNode, "Choice1")
            call node_27_1 from _call_node_27_1
        "I can’t handle this anymore… (Do not investigate)":
            $ relationKeeper(chapter3_network, currentNode, "Choice2")
            call node_27_2 from _call_node_27_2
    call node_28 from _call_node_28
    return

label node_27_1:
    #stress -7
    "You start to investigate, and like the previous two murders, there’s a note left behind. The note reads:"
    show murderNote3 at truecenter
    "Who’s {i} dead {/i} weight now? :)"
    hide murderNote3
    player "..."
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
    scene bedroom with dissolve
    "You decide to just sleep on it, since you cannot do anything anymore…"
    stop music
    scene black with fade
    call node_29 from _call_node_29

    return

#CHAPTER THREE END---------------------------------------------------------------------------------------------------------------------

















#CHAPTER FOUR START-------------------------------------------------------------------------------------------------------------------
label node_29:
    scene bedroom with fade
    play music "chp3music.mp3" loop
    "As you wake up to a dreadful morning, you’re taken aback by the overwhelming mental trauma you’ve received over the past few days"

    "You reluctantly get out of bed and get ready to go to university since you have no other options. As you throw the shirt you wore yesterday to the side, you notice something"

    player "Why is this shirt missing a button?"

    "Not caring too much, you throw it to the side and get ready."
    scene habibOutside with fade
    "When you reach university, you witness a bizarre show of police, journalists, media personnel, parents and other workers as well"
    scene habibInside with fade
    scene central with fade
    "Concerned, you ask Asad, who’s been standing there for a while now on what is happening?"

    "Asad explains that the police and media arrived this morning and that the police have started investigating the scenes of the murders"
    show Asad
    asad "Apparently, they’ve locked down all the scenes of the murders. No students, faculty or staff goes in or out."

    asad "Media’s here too. They wanted to scoop up some dirt on us, now sadly they have plenty of it."

    "You see Zayn pacing around really anxious with what’s going on."

    player "What’s his problem?"

    asad "He’s been like this since morning. Telling people to get the police out and stuff; pacing like that and being suspicious overall."

    player "You don’t think…he-?"

    asad "I honestly don’t know man. What amazes me is that the murder was very intelligent on where he did it and how he did it. None of it has been caught on camera so even the police are confused on how to investigate this case further."
    asad "Aaron’s dad and Ahsen’s family have their hands on the admin’s throat. I cannot even imagine how this all will play out."
    hide Asad
    show Amil
    amil "It’s been a real series of tragedies honestly."
    hide Amil
    show Asad at right
    show Amil at left
    player "Indeed it has been…"

    "After a pause, Asad speaks again."

    asad "And that is the officer in chief"

    "Asad points to the officer in charge of the investigation"
    hide Amil
    hide Asad

    show Policeman
    "..."
    hide Policeman


    "You decide that enough is enough and that you’ll reveal all your findings to the chief police officer"
    
    player "Hello sir, are you the chief investigating officer over here?"


    show Policeman
    cop "Yes, yes I am. Now, unless you have something important to say, I’d recommend moving back and not approaching this area for a while till our work is finished over here."

    player "Yes, it is in fact something related to the murders…"

    cop "Yeah? I’m listening."

    "You start speaking. At first it is just incoherent rambling as you try to find the words to explain everything you saw. Slowly it all starts to make sense; the murders, what you found out during your investigations, the details and the lack thereof, everything…"

    cop "Wow. So you were present at all the scenes of the crime and in fact were a key witness? And you played round with the bodies thinking you’re what? Sherlock Holmes?"

    player" “I never intended to involve myself, it just happened. I’d rather not be a part of all this if it were up to me to be honest."

    "The officer breathes a heavy sigh"

    cop "So…Who do you think is the murderer?"

    player "If I had to guess…"
    stop music

    menu:

        "It's me":
            call Node_GoodvsNeutral from _call_Node_GoodvsNeutral

        "Alaina":
            call Node_Bad_Ending from _call_Node_Bad_Ending
        "Amil":
            call Node_Bad_Ending from _call_Node_Bad_Ending_1
        "Sean":
            call Node_Bad_Ending from _call_Node_Bad_Ending_2
        "John":
            call Node_Bad_Ending from _call_Node_Bad_Ending_3
        "Ayesha":
            call Node_Bad_Ending from _call_Node_Bad_Ending_4
        "Asad":
            call Node_Bad_Ending from _call_Node_Bad_Ending_5
        "Zayn":
            call Node_Bad_Ending from _call_Node_Bad_Ending_6
        "Shanzayy":
            call Node_Bad_Ending from _call_Node_Bad_Ending_7
    return

label Node_Bad_Ending:
    show black with dissolve
    show white with dissolve
    show black with dissolve
    show white with dissolve

    scene hospital
    with fade
    play music "hospitalbg.mp3" loop
    "You wake up to the scene of a hospital, unable to make sense of anything."

    "You try to get up but you’re strapped to the bed and can’t move."
    show Doctor at left
    show Nurse at right
    doctor "So what are the results?"

    if stress > 60:
        $ dialogue = "which were unacceptably high, showing lack of mental therapeutic effects."
    else:
        $ dialogue = "which shows improvement compared to the previous levels when the patient was admitted."

    nurse "Patient shows a lack of empathy quotient. Even though the murdered victims and the notes placed on their bodies clearly indicated the patient’s involvement, the patient still chose not to believe their involvement."
    nurse "Stress levels were [stress] [dialogue]. Overall, patient has shown little to no improvement."

    doctor "So the experiment failed…"

    doctor "Administer 35 mgs of the Chlordiazepoxide, Clonazepam and Midazolam concoction to wipe the patient’s memories and put them into an induced comma again. We will execute the experiment again after the wait period of 3 days."

    nurse "Understood."
    hide Doctor
    hide Nurse
    "Before you can say anything, the nurse injects you with something, and you…slowly…fall…to…sleep…again…"

    scene black with fade
    stop music
    "The Game has ended."
    return

label Node_GoodvsNeutral:
    $value=60
    if stress>value:
        call Node_Neutral_Ending from _call_Node_Neutral_Ending
    else:
        call Node_Good_Ending from _call_Node_Good_Ending
    return


label Node_Neutral_Ending:
    show black with dissolve
    show white with dissolve
    show black with dissolve
    show white with dissolve
    scene hospital with fade
    play music "hospitalbg.mp3" loop
    "You wake up to the scene of a hospital, unable to make sense of anything."

    "You try to get up but you’re strapped to the bed and can’t move."

    show Nurse

    "The Nurse comes and unstraps you"
    hide Nurse
    show Doctor at left
    doctor "So what are the results?"
    show Nurse at right
    nurse "The Patient shows a positive empathy quotient. When faced with the consequences of their previous choices, the patient somehow realized what was going on and was ready to accept themselves as the culprit."
    nurse "However, their stress levels were [stress], which were unacceptably high, showing lack of mental therapeutic effects."

    doctor "So the experiment was a partial success?"

    nurse "Quantitatively so."

    doctor "At least it’s progress."

    "You seem confused so the doctor explains."
    hide Nurse
    hide Doctor
    show Doctor
    doctor "You must be confused. Let me explain. When you were admitted here, you were caught by the police, while committing a murder. Those three murders; you committed them."
    doctor "You suffered from Dissociative identity disorder caused by your elevated levels of stress because of your environment."
    doctor "It was because of that stress, that when you experienced bullying or harassment which you could not tolerate, another personality would take over, so that your mind could cope with the pressure you were feeling."
    doctor "However, this second personality had no moral compass, so it saw fit to remove the hurdles which were affecting your mental state. And by remove the hurdles, I of course mean murder them."

    player "Wait so I murdered those people? How? Wasn’t I here?"

    doctor "No, these murders have happened beforehand, but because of your mental disorder those memories were repressed. You did not remember doing anything. Furthermore, your other personality was quite cunning. It was able to commit all those murders till it was finally caught and you were brought here."

    player "So how was I seeing those memories? And why was I reliving them?"

    doctor "We tried to help you but all other forms of therapy failed. This therapy was one which we have just invented. We put you into a coma using specific medication and hypnosis."
    doctor "Using the hypnosis we were able to tap into those suppressed memories and send you into them, to experience the loss of life as any other bystander would."
    doctor "This forced you to confront your guilt and actions and to make a choice, to either accept your guilt, accept your actions, even though you had very little clues on whether it was your or not, or to neglect everything and act as though you had no hand in it."
    doctor "You chose the former, and accepted that what happened was wrong, and that you probably had some part to play in it."

    player "So am I better now?"

    doctor "You have almost the same stress levels as you had when you were admitted here. However, you accepted that murder is wrong, which your former self didn’t. You tried to live a slightly more healthier and friendlier life in your mental simulation."
    doctor "So I wouldn’t call it a complete failure, but we do need to decrease your stress levels somehow for it to be called a complete success."

    player "Ahhh I see…"

    doctor "Since we weren’t able to help you completely, we will keep you here for slightly longer. We might try other therapies and medicine as well. Since you’ve shown improvement, it’s possible you might finally be cured of your illness."

    player "Thank you doctor, I’ll try my best to get better as soon as I can."

    doctor "And we’ll be here to help you throughout that process."
    hide Doctor
    "The doctor instructs the nurse to escort you out of the hospital room, and she takes you to another room where you can rest before your next therapy session starts…"
    screen black 
    with fade
    stop music
    "The Game has ended."

    return



label Node_Good_Ending:
    show black with dissolve
    show white with dissolve
    show black with dissolve
    show white with dissolve
    
    scene hospital with fade
    play music "hospitalbg.mp3" loop
    "You wake up to the scene of a hospital, unable to make sense of anything."

    "You try to get up but you’re strapped to the bed and can’t move."

    show Nurse

    "The Nurse comes and unstraps you"
    hide Nurse
    show Doctor at left
    show Nurse at right
    doctor "So what are the results?"

    nurse "The Patient shows a positive empathy quotient. When faced with the consequences of their previous choices, the patient somehow realized what was going on and was ready to accept themselves as the culprit."
    nurse "Their stress levels were [stress], which shows a massive decrease in stress levels than when the patient was first admitted here."

    doctor "So the experiment was a success!"

    nurse "Quantitatively so."

    "You seem confused so the doctor explains."
    hide Nurse
    hide Doctor
    show Doctor
    doctor "You must be confused. Let me explain. When you were admitted here, you were caught by the police, while committing a murder. Those three murders; you committed them."
    doctor "You suffered from Dissociative identity disorder caused by your elevated levels of stress because of your environment."
    doctor "It was because of that stress, that when you experienced bullying or harassment which you could not tolerate, another personality would take over, so that your mind could cope with the pressure you were feeling."
    doctor "However, this second personality had no moral compass, so it saw fit to remove the hurdles which were affecting your mental state. And by remove the hurdles, I of course mean murder them."

    player "Wait so I murdered those people? How? Wasn’t I here?"

    doctor "No, these murders have happened beforehand, but because of your mental disorder those memories were repressed. You did not remember doing anything. Furthermore, your other personality was quite cunning. It was able to commit all those murders till it was finally caught and you were brought here."

    player "So how was I seeing those memories? And why was I reliving them?"

    doctor "We tried to help you but all other forms of therapy failed. This therapy was one which we have just invented. We put you into a coma using specific medication and hypnosis."
    doctor "Using the hypnosis we were able to tap into those suppressed memories and send you into them, to experience the loss of life as any other bystander would."
    doctor "This forced you to confront your guilt and actions and to make a choice, to either accept your guilt, accept your actions, even though you had very little clues on whether it was your or not, or to neglect everything and act as though you had no hand in it."
    doctor "You chose the former, and accepted that what happened was wrong, and that you probably had some part to play in it."

    player "So am I better now?"

    doctor "You have half the stress levels as when you were admitted here. You accepted that murder is wrong, which your former self didn’t. You tried to live a healthier and friendlier life in your mental simulation. I wouldn’t call that any less than massive improvement."

    player "Ahhh I see…"

    doctor "Be happy, the experiment was a success. Your mental state improved immensely. It is now no more in shatters. In fact you might be able to leave this place soon too."

    player "Thank you doctor, thank you so much."

    doctor "Thank yourself; it was what got you out of this mess."
    hide Doctor
    "The doctor instructs the nurse to escort you out of the hospital room, and for once in the apparent past few days, you feel optimistic of what’s to come..."

    screen black
    with fade
    stop music
    "The Game has ended."
    return



