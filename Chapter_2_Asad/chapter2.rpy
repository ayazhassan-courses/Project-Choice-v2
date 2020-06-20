label node_20:
    
    $ currentNode = "node_20"
    
    "You wake up with blurry eyes, unable to recognize what’s happening around you."

    "Your eyes focus to your empty bedroom. It takes a while before you’ve regained your consciousness properly. As soon as you do, you’re reminded of the unnerving scene which you witnessed yesterday."

    player "(sighs) Guess I should get ready..."

    "You sigh again"

    #scene change to university

    player "Why is it so quiet?"

    "You ponder to yourself as you enter campus expecting drama and screaming people."

    #scene changes to central street

    player "Why isn't there more....more...."

    aaron "Drama, action, media and publicity?"

    "You turn around to see Aaron behind you"
    
    #show Aaron
    player "Yeah…I mean, someone did die, I thought there’d be more people concerned about it."

    aaron "Ahhhh naïve young little boy."

    player "What...?"

    aaron "Didn’t you know? Adam was always the family disgrace. Mediocre grades, mediocre extra-curricular activities, thuggish behavior and always made a laughing stock of the entire Zaidi family. He caused them more trouble than he was worth."

    player "Yeah so?"

    aaron "Sooo, my young stupid child, his father wanted him gone anyway. In fact, if he wasn’t the gentle man he is, he would’ve kicked him out of the family. Him dying was like a sigh of relief for Adam’s father. The child not wanted, finally gone. And he didn’t even have to lift a finger to do it. It just happened for him. So he cut a deal with Habib. Habib doesn’t go public with this murder, Habib saves face, his dad gets off a dead weight, Habib issues a hush order to stop the flow of information, everyone wins, and no one loses."

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

    player "Y-Yeah..."

    "You’re trying to process everything when suddenly Sean yells…"

    #show Sean

    sean "Oh my God [playerName]"

    "You see Sean and Zayn walking by together"

    sean "Are you okay? I heard you got involved with something unpleasant. Maybe you should’ve taken the day off today."

    zayn "Heck yeah mannn, no one should have to come to uni after an incident like that oooh."

    menu:
        "I’m fine, I’d rather be here than alone with my thoughts at home after what I saw":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_20_1
        
        "It’s my choice whatever I do with my life, do y’all both have to butt in??":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_20_2

    call node_21

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

    player "Bye guys!"

    "You decide to go to the area outside Tapal cafeteria to study"

    "As you’re on the way, you come across Ahsen."

    ahsen "My oh my, why if isn’t the murderer of Warren Street."

    player "I’m not the fascist here Ahsen, you are."

    ahsen "At least I’m no murderer you blood sucker."

    menu:
        "Calling me a vampire, when you’re the pale-dead looking one? Hahaha":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_21_1

        "Look dude, I’m not the murder! WHY IS EVERYONE ACCUSING ME?":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_21_2

    call node_22

    return

label node_21_1:
    #stress -2
    #relation -2 Ahsen

    ahsen "Ahhh is my fancy white color why you despise me so much you filthy muggle?"

    player "Racist much Ahsen?"

    ahsen "Not in the least [playerName]"

    return

label node_21_1:
    #stress +3
    #relation -2 Ahsen

    ahsen "The dude had an obvious connection to you, who else would kill him? Bigfoot?"

    player "Like I’ve been explaining to people since morning, I just got to the scene of the crime, I did not kill him!"

    ahsen "Keep telling yourself that!"

    return

label node_22:

    $ currentNode = "node_22"

    player "(sighs) Could you please be nice for once? I’m going through a lot right now?"

    "Ahsen just takes advantage of you being down, and used it to push down harder on you."

    "Ahsen starts screaming."

    ahsen "GOING THROUGH A LOT? A LOT? WHAT ABOUT WHEN YOU MADE MY LIFE MISERY FOR 6 WHOLE MONTHS? WHEN THE PROFESSORS REFUSED TO EVEN ACKNOWLEDGE MY EXISTENCE?"

    player "Nothing of the sort happened. Stop screaming about it."

    ahsen "AHHH YES. YOU DO WHATEVER YOU WANT AND WHEN SOMEONE TRIES TO SPEAK UO YOU GASLIGHT THEM. REALLY NICE, REALLY NICE [Player]. NEXT THING YOU KNOW YOU’RE GONNA ASK ADAM’S PARENTS NOT TO SCREAM BECAUSE IT MAKES YOU FEEL BAD?? WELL BOOHOO"

    "You’re about to start sobbing from all the screaming."

    ahsen "WHO’RE YOU GONNA MURDER NEXT HUH? THAT DUDE FROM YOUR CALCULUS CLASS? OR THAT TEACHER'S ASSISTANT YOU DON’T LIKE. COME TELL ME HUH! WHO? WHO?"

    "You try extremely hard to stop yourself from dropping just there and crying."

    player "...."

    amil "Tormenting an already down man? How Draco Malfoy of you, Ahsen."

    asad "You’d think Draco would get a life after the whole fiasco he had. Guess it’s true when they say ‘You can never straighten a dog’s tail'."

    amil "Exactly!"

    player "Guys...."

    ahsen "Well if it isn’t Shaggy and Scooby, here to save the day!"

    amil "Indeed! I just hope there’s no office involved in saving the day this time, if you know what I mean."

    "Amil winks"

    ahsen "Pfffft, I’m outta here. Have a good day you gorillas."

    "Noticing that since other people are here now, and that he won’t be able to manipulate you, Ahsen leaves the scene"

    player "T-Thanks guys…"

    asad "(smiles) What're friends for?"

    amil "Exactly!"

    "You all talk to each other for a few minutes and then decide to go to the Dhabba to get some fries."

    asad "Let's goooo!"

    #scene change to Dhaba

    "You guys order fries and as they’re being prepared, you excuse yourself for a few minutes."

    player "Guys I’ll be back, just gonna go to the washroom real quick."

    amil "Sure, we’re gonna be waiting here."

    player "Cool!"

    "You go to the washroom…"

    #scene change to washroom

    #black screen for 5 seconds

    #scene change back to washroom

    "You finally go back to the Dhabba."

    player "Hey, I’m back!"

    asad "Took you long enough, you were gone for fifteen-ish minutes."

    player "Whattttt? Nooo?"

    asad "Yeah lol, you were...."

    menu:
        "Wow, I didn’t notice. Oops, sorry.":
            $ relationKeeper(chapter0_network, currentNode, "Choice1")
            call node_22_1

        "Mind your own business okay, I can stay however long I want":
            $ relationKeeper(chapter0_network, currentNode, "Choice2")
            call node_22_2

    call node_23

    return

label node_22_1:
    #relation +3 Asad, Amil

    asad "Hahaha it’s cool, we were just worried is all"

    amil "Yeap..."

    player "Thanks for caring guys! Love you!"

    asad "Love you too!"

    amil "Likewise!"

    return

label node_22_2:
    #relation -3 Asad, Amil

    amil "Of course friend, we were just worried is all."

    asad "Yeah man, that’s all"

    player "Yeah sure, thanks…"

    return 
