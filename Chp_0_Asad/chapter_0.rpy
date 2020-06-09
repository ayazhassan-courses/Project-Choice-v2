image mountain = im.Scale("scenery.jpg", 1920, 1080)

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

screen stress_counter:
    hbox:
        textbutton "Stress: [stress]" action Show("pop_up")

label chapter_0:
    call variables
    call node_6
    return
    
label node_6:
    #scene change stairs area
    show screen stress_counter
    show emma_neutral

    $ currentNode = "node_6"

    "You walk towards Tapal Cafeteria, trying to clear your head of all the people who are mean to you on a daily basis and before you know it, you’re standing at the door of Tapal Café"

    #scene change outside Tapal

    "You’re about to open the door, when  it suddenly opens itself, revealing…"

    #show aaron_neutral

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

    #scene change inside Tapal

    "You spot your friends Alaina, Amil, Asad, Ayesha all at the same table and go sit with them!"

    player "Did Mitosis occur here? I could’ve sworn I was supposed to meet two of you here"

    alaina "Hardy Har har, we just happened to bump into each other and thought we’d all enjoy lunch together hehe~~"

    player "Well it’s great to see all my favorite people on one table so I’m not complaining"

    "You all start to eat and talk when you suddenly sigh after a few minutes"

    asad "You good [playerName]?"

    player "Yeah, just tired of the annoying people I have to tolerate everyday"
    
    menu:
        "Yeah, just tired of the annoying people I have to tolerate everyday":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_6_1

        "It’s nothing, let’s just eat":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_6_2

        "Just mind your own business and leave me alone for a while okay?":
            $ relationKeeper(chapter0_network, currentNode, "Choice3")
            call node_6_3

    call node_7

    return

label node_7:
    $ currentNode = "node_7"

    "You all finish your lunch and everybody prepares to head for class. You still have time till your next class starts so you go to the Dhabba area to chill after you say goodbye to everyone"

    "As you’re going to the Dhabba Area, you bump into Bakhtawar and Zain"

    player "Yo Bakhtawar and Zayn, what’s up!"

    john "Dude, for the hundredth time, it’s John, not Bakhtawar, I don’t use that name anymore."

    player "Fine fine, {i}John{/i}"

    john "Why do I smell sarcasm in there…"

    player "(smirks) Hmmm, I wonder"

    zayn "Dude, he’s obvio making fun of you"

    john "Huh. Not cool dude. Don’t you know I’ve been hitting the gym again lately? I’d lift you up and throw you into the Naala if I wasn’t so nice"

    zayn "AGAIN. Dude we get it, you gym hard, but please for the love of God and music stop telling us that"

    menu:
        "It’s cool, I’m interested in his gym routine":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_7_1

        "Yeah lmao stop using the gym as a personality trait":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_7_2

    call node_8

    return

label node_8:
    $ currentNode = "node_8"

    zayn "Oh my God, I completely forgot about my singing lessons today at 8. I’m too tired to go today"

    #show Zayn sad

    player "So Zayn, what kind of music do you like to listen to?"

    zayn "Honestly man anything pop gets me going, the only thing I despise is death metal music. What kind do you like?"

    menu:
        "Same as you, a pop fan":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_8_1

        "Eastern music mostly":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_8_2

        "EDM stuff is what I jam to":
            $ relationKeeper(chapter0_network, currentNode, "Choice3")
            call node_8_3

        "Death Metal!!":
            $ relationKeeper(chapter0_network, currentNode, "Choice4")
            call node_8_4

    call node_9

    return

label node_9:
    $ currentNode = "node_9"

    player "So what’re you guys up to?"

    john "Gonna hit the gym, wanna join me?"

    zayn "Gotta go practice the violin, how about you come with and I teach you too?"

    menu:
        "Go to the gym with John":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_9_1

        "Go to the music room with Zayn":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_9_2

        "Stay here by yourself":
            $ relationKeeper(chapter0_network, currentNode, "Choice3")
            call node_9_3

    call node_10

    return

label node_10:
    $ currentNode = "node_10"

    "Your leftover classes resume"

    "Before you even know it, all of your classes have ended and it's evening already"

    #scene changes to garden/dhaba

    "You go out to the garden area to grab some of Rahim Bhai's fries before leaving"

    "You notice that it's the time of the year when evenings are really dark"

    "You quickly grab your fries and go to the Courts Area to watch some sports"

    "The Courts Area is an area with Basket Ball and Tennis Courts and across that a place to sit so people can come and enjoy the sports with their friends"

    "As you're passing by the nets, your eyes cross that of someone who'd be the last person you'd want to see at the end of such a tiring day"

    "Your eyes meet Ahsen's..."

    ahsen "(Comes over by the net) Here to tell the teacher that I’m playing basketball, [playerName]?"

    player "Look, I only did that because you were being manipulative of the club as president and the members were not happy. I was forced to involve the teachers"

    ahsen "Save the excuses for someone else, I know you were just jealous of my leadership and couldn’t bear to see the spotlight on someone else than yourself."

    player "But I was just a freshie then, why would I feel jealous of anything. I didn’t even know who was who until the whole incident happened"

    ahsen "Listen, if you so even try to come near me or try to ruin my reputation again, I will do something so bizarre even…"

    "Just as Ahsen is about to go wild, Sean shows up"

    sean "Hey Ahsen, you gonna play or just threaten people? Come on, it’s your turn on the field"

    "Ahsen angrily leaves, cursing at you under his breath"

    sean "Seems like he was about to have a meltdown"

    player "Yeah, he has those whenever he sees me. He was abusing his power as club president a while back and I got SL and the professors involved which made him look really bad so he despises me for it. Anyway thanks for helping me!"

    sean "Any time man! It’s been a while since we’ve talked, what’s up nowadays"

    menu:
        "Uhhh nothing. I should leave.":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_10_1

        "You know the same old same old; trying to just pass the semester and failing miserably":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_10_2

    "You wave to Sean and leave"

    "You get into your car and drive back home"

    "You finally reach home and drop dead on the bed. You ponder over all that happened today and as you’re dreaming, you fall asleep"

    call node_chp0_end

    return

label node_chp0_end:
    return

label node_6_1:
    #relation all + 2

    asad "Ohhh, you wanna talk about it?"

    menu:
        "I’d rather not…":
            call node_6_1_1

        "It’s just these few people bullying me and I’m started to grow tired of it":
            call node_6_1_2

        "There’s a few people I’m considering murdering, I might actually do it":
            call node_6_1_3


    return

label node_6_1_1:
    #relation all + 0

    alaina "Whatever makes you comfortable, but know that we’re all here for you any time you need to rant or anything okay?~~"

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

    alaina "Hehe, [playerName], you’re joking…right?"

    player "I really hope I was"

    ayesha "Listen [playerName] if something is bothering you please tell us but please don’t make bad jokes like these, lives are not something we can throw away so easily even if they inconvenience us"

    player "..."

    player "Okay fine, my bad, sorry."

    ayesha "Nice to see that you understand"

    "The mood at the table is awkward as you all try to finish your lunch after the scene that happened"

    return

label node_6_2:
    #relation all +0

    ayesha "You sure? You can always talk to us you know, we’ll always be here for you…"

    menu: 
        "No it’s cool. I know I can trust you guys. I’ll be sure to let y’all know if something is up":
            call node_6_2_1
        
        "Please, just leave me alone for a while to manage my stuff okay? No need to be so nosy where y’all don’t belong":
            call node_6_2_2

        "I guess I could tell you guys…":
            call node_6_2_3


    return


label node_6_2_1:
    #relation all +1

    alaina "Whatever makes you comfortable, but know that we’re all here for you okay? If anything’s bothering you or you need help be sure to reach out m’kay?~~"

    player "Yeap, thanks guys…means a lot!"

    "You all continue eating your food but you feel uneasy"

    return 

label node_6_2_2:
    #relation all -2

    amil "Amil: “No need to lash out [playerName], she was just worried is all"

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

    alaina "[playerName]…"

    amil "Wasn’t a nice thing to say but we’ll leave you to it"

    player "Thanks, appreciate it."

    "The mood at the table became incredibly hostile and sad, everyone seems down and Asad feels sad because to hm it feels like he triggered you or something"

    return 

label node_7_1:
    #relation John +2
    
    zayn "That’s a first I’ve heard someone say that"

    return

label node_7_2:
    #relation John -2

    john "Dude shut up or I’ll seriously throw you off a ledge or something"

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

label node_9_1:
    #relation John +3

    player "Guess I’ll hit the weights"

    "You gym for a while then freshen up and go to your classes"

    return

label node_9_2:
    #relation Zayn +3

    player "Guess I’m learning the violin today"

    "You go to the music room, play the violin horribly for a while then go to your classes when time comes"

    return 

label node_9_3:
    #relation both +0

    "John and Zayn both leave. You stay there, bask in the sun and wait till it’s time for your classes. Once it is, you go to your classes"

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

