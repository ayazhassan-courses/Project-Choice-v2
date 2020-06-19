label node_23:
    "You all start chatting again."
    "As you’re chatting, Asad finishes his fries and utters that he wants to eat some Makai next"
    asad "Guys let’s go to Learn courtyard!, I really wanna have some Makai right now!"
    player "Sure!"
    amil "Let’s make a dash through Earth Courtyard; it’ll be closer to go from there."
    player "Sure, that’s fine by me."
    "You all start walking towards Learn Courtyard."
    "You finally reach Earth Courtyard."
    #Scene change Earth courtyard
    "…and see Ahsen with his face submerged in the Earth Courtyard fountain’s water."
    "Asad decides to tease Ahsen."
    asad "Hey man! This is no place to wash your face!"
    "Amil decides to chime in!"
    amil "Yeah man, there’s better ways to get that permanent grime off your face, hahaha."
    "…while you stand there awkwardly thinking about the scene that happened earlier…"
    "They both tease him for a few minutes, but he doesn’t reply."
    player "Uhhhh guys…how long has he been submerged in that water?"
    amil "We’ve been taunting him for 5 minutes straight."
    asad "Oh My God get him out!!!"
    "You run and pull his face out of the water…only to see…"
    "HIS FACE HAS BEEN BADLY BASHED AND IS BLEEDING."
    player "GUYS!"
    "Amil checks for a pulse but Ahsen’s long gone"
    amil "Dead…"
    player "WHAT IS HAPPENING"
    "You suddenly scream. Amil and Asad start looking concerned too."
    player "Guys we should…"

    menu:
        "See if there are any clues nearby (Investigate)":
            call node_23_1
        "Forget everything and call campus security (Don’t investigate)":
            call node_23_2
    call node_24
    return

label node_23_1:
    $ stress-=4
    "As you eye around, you see a note which gives off a very familiar feeling."
    "You open it and the note reads: ‘No, you’re next :)’"
    "Reading this sends shivers down your spine."
    "It’s just like the note from before…what is happening…why is this happening…"
    "You investigate further and notice that Ahsen’s head was bashed with a rock. You find a bloodied rock nearby!"
    player "Guys look! That’s probably what was used to break Ahsen’s face in!"

    $ Asadrelation = relationshipdict['Asad']
    $ value=20
    if Asadrelation > value: #Asad (automatic)
        call node_23_1_1
    else:
        call node_23_1_2

    return

label node_23_1_1:
    $ stress-=4
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
    $ stress +=0
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
    $ stress +=4
    player "Let’s call the security guys; this is out of our hands. Not one but two murders? This is getting crazy and I am not in a mental condition to deal with it right now."
    amil "Yeah, let’s get out of here quick. I can’t bear looking at that body anymore"
    "You all leave the scene and go to the campus security office in order for them to take care of the matter."
    return


label node_24:
    "You reach the security office and explain everything to them in detail. How you saw Ahsen’s body submerged in water, how you pulled him out and everything afterwards."
    "Campus security follows you to the scene at Earth Courtyard where a bunch of students have already gathered."
    "There you show them the body and how you discovered it."
    "Listening to this, everyone suddenly starts giving you weird looks as they already suspected you to be involved in the basement murder."
    "Seeing all this commotion and the uneasiness of people around you, you run and flee from the scene which makes everyone suspect you even more."
    "Within a few minutes, everyone has started giving you weird looks. Your bloodied shirt gives everyone the wrong impression so you try to get away from everyone as soon as possible and dash for the courts area to be alone."
    "When you reach there, you see Shanzayy on her phone. She looks up from her phone and sees you."

    $ Shanzayyrelation = relationshipdict['Shanzayy']
    $ value=20
    if Shanzayyrelation > value: #Shanzayy (automatic)
        call node_24_1
    else:
        call node_24_2

    call node_25
    return

label node_24_1:
    $ stress - =4
    shanzayy "H-Hey…"
	player "Hey…"
	shanzayy "So I heard…"
    #show player sad
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
    #show player happy
    player "Mhm, thanks…Shanzayy…"
	"Shanzayy smiles sweetly, probably the first time she’s smiled at you and afterwards, she leaves…"
    return

label node_24_2:
    $ stress + =4
	shanzayy "Oh My God, murderer…"
	player "Let me explain, it wasn’t m-"
	"You’re cut off by Shanzayy."
	shanzayy "NO! Everyone’s saying you’re the guy who killed them both and I will not stand here and be the third!"
	"After saying this, she makes a dash for it and you’re left there alone sobbing, unsure of what to do or whether to even live or not."
    return



label node_25:
    "You stay there for a while, thinking back on everything that happened today, scared of what’s to come."
    "After a while, you decide to finally go home."
    "Avoiding any eye contact, you leave for home."
    #Scene change home
    "When you reach home you make a dash for your bedroom."
    #scene change bedroom
    "…and you collapse on the bed, unable to think of what to do next…"
    #Black screen fade in
    return
