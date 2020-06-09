init python:
    def relationKeeper(ds,currentNode, choice):
        global relationshipDict
        global stress
        for i in ds[currentNode]:
            if i[0]==choice:
                stress+=i[1]
                for j in i[2]:
                    relationshipDict[j[0]]+=j[1]
                    if relationshipDict[j[0]]<0:
                        relationshipDict[j[0]]=0
                return i[-1]
  
image mountain = im.Scale("Screenshot (866).png", 1920, 1080)

define player = Character("[playerName]")
define aaron = Character("Aaron")
define alaina = Character("Alaina")
define amil = Character("Amil")
define asad = Character("Asad")
define ayesha = Character("Ayesha")
define john = Character("John")
define zayn = Character("Zayn")
define ahsen = Character("Ahsen")
define sean = Character("Sean")

label start:
    scene mountain
    $ stress = 0
    $ playerName = renpy.input("Please enter your name")
    $ playerName = playerName.strip()
    call chapter_0
    return

label variables:
    $ chapter0_network = {
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
        ]  
}


    $ relationshipDict = {
        "Aaron":0,
        "Alaina":0,
        "Amil":0,
        "Asad":0,
        "Ayesha":0,
        "John":0,
        "Zayn":0,
        "Ahsen":0,
        "Sean":0
    }
    return

screen stress_counter:
    hbox:
        textbutton "Stress: [stress]" action Show("pop_up")

label chapter_0:
    call variables
    call node_7
    return
    
label node_7:    
    $ currentNode = 'node_7'
    #scene change stairs area
    show screen stress_counter
    show emma_neutral
    
    zayn "AGAIN. Dude we get it, you gym hard, but please for the love of God and music stop telling us that"

    menu:
        "It’s cool, I’m interested in his gym routine":
            $ relationKeeper(chapter0_network,currentNode, 'Choice1')
            call node_7_1

        "Yeah lmao stop using the gym as a personality trait":
            $ relationKeeper(chapter0_network,currentNode, 'Choice2')
            call node_7_2

label node_8:   
    $ currentNode = 'node_8'
    zayn "Honestly man anything pop gets me going, the only thing I despise is death metal music. What kind do you like?"

    menu:
        "Same as you, a pop fan.":
            $ relationKeeper(chapter0_network,currentNode, 'Choice1')
            call node_8_1

        "Eastern music mostly":
            $ relationKeeper(chapter0_network,currentNode, 'Choice2')
            call node_8_2

        "EDM stuff is what I jam to":
            $ relationKeeper(chapter0_network,currentNode, 'Choice3')
            call node_8_3

        "Death Metal!!":
            $ relationKeeper(chapter0_network,currentNode, 'Choice4')
            call node_8_4

    
label node_9:
    $ currentNode = 'node_9'
    zayn "Gotta go practice the violin, how about you come with and I teach you too?"
    
    menu:
        "Go to the gym with John":
            $ relationKeeper(chapter0_network,currentNode, 'Choice1')
            call node_9_1

        "Go to the music room with Zayn":
            $ relationKeeper(chapter0_network,currentNode, 'Choice2')
            call node_9_2

        "Stay here by yourself":
            $ relationKeeper(chapter0_network,currentNode, 'Choice3')
            call node_9_3

    "Your leftover classes resume"


label node_7_1:
    #relation John +2
    
    zayn "That’s a first I’ve heard someone say that"
    call node_8
    return

label node_7_2:
    #relation John -2

    john "Dude shut up or I’ll seriously throw you off a ledge or something"
    call node_8
    return

label node_8_1:
    #relation Zayn +2

    zayn "Ayyy man, gang gang"
    call node_9
    return 

label node_8_2:
    #relation Zayn +1

    zayn "Ahhh sitars and tablas, nice, the classics"
    call node_9
    return 

label node_8_3:
    #relation Zayn +1

    zayn "Ayyy party music, love it!"
    call node_9
    return

label node_8_4:
    #relation Zayn -2

    zayn "Ouch…sorry for your loss"
    call node_9
    return

label node_9_1:
    #relation John +3

    player "Guess I’ll hit the weights"

    "You gym for a while then freshen up and go to your classes"
    call node_10
    return

label node_9_2:
    #relation Zayn +3

    player "Guess I’m learning the violin today"

    "You go to the music room, play the violin horribly for a while then go to your classes when time comes"
    call node_10
    return 

label node_9_3:
    #relation both +0

    "John and Zayn both leave. You stay there, bask in the sun and wait till it’s time for your classes. Once it is, you go to your classes"
    call node_10
    return 

label node_10:
    "The end."

