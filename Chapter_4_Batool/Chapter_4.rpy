label node_29:

    "As you wake up to a dreadful morning, you’re taken aback by the overwhelming mental trauma you’ve received over the past few days"

    "You reluctantly get out of bed and get ready to go to university since you have no other options."

    "When you reach university, you witness a bizarre show of police, journalists, media personnel, parents and other workers as well"

    "Concerned, you ask Asad, who’s been standing there for a while now on what is happening?"

    "Asad explains that the police and media arrived this morning and that the police have started investigating the scenes of the murders"

    asad "Apparently, they’ve locked down all the scenes of the murders. No students, faculty or staff goes in or out."

    asad "Media’s here too. They wanted to scoop up some dirt on us, now sadly they have plenty of it."

    "You see Zayn pacing around really anxious with what’s going on."

    player "What’s his problem?"

    asad "He’s been like this since morning. Telling people to get the police out and stuff; pacing like that and being suspicious overall."

    player "You don’t think…he-?"

    asad "I honestly don’t know man. What amazes me is that the murder was very intelligent on where he did it and how he did it. None of it has been caught on camera so even the police are confused on how to investigate this case further. Aaron’s dad and Ahsen’s family have their hands on the admin’s throat. I cannot even imagine how this all will play out."

    amil "It’s been a real series of tragedies honestly."

    player "Indeed it has been…"

    "After a pause, Asad speaks again."

    asad "And that is the officer in chief"

    "Asad points to the officer in charge of the investigation"

    #show officer

    #show asad

    "You decide that enough is enough and that you’ll reveal all your findings to the chief police officer"

    player "Hello sir, are you the chief investigating officer over here?"

    cop "Yes, yes I am. Now, unless you have something important to say, I’d recommend moving back and not approaching this area for a while till our work is finished over here."

    player "Yes, it is in fact something related to the murders…"

    cop "Yeah? I’m listening."

    "You start speaking. At first it is just incoherent rambling as you try to find the words to explain everything you saw. Slowly it all starts to make sense; the murders, what you found out during your investigations, the details and the lack thereof, everything…"

    cop "Wow. So you were present at all the scenes of the crime and in fact were a key witness? And you played round with the bodies thinking you’re what? Sherlock Holmes?"

    player" “I never intended to involve myself, it just happened. I’d rather not be a part of all this if it were up to me to be honest."

    "The officer breathes a heavy sigh"

    cop "So…Who do you think is the murderer?"

    player "If I had to guess…"

    menu:

        "It's me":
            call Node_GoodvsNeutral

        "Alaina":
            call Node_Bad_Ending
        "Amil":
            call Node_Bad_Ending
        "Sean":
            call Node_Bad_Ending
        "John":
            call Node_Bad_Ending
        "Ayesha":
            call Node_Bad_Ending
        "Asad":
            call Node_Bad_Ending
        "Zayn":
            call Node_Bad_Ending
        "Shanzayy":
            call Node_Bad_Ending
    return

label Node_Bad_Ending:

    #scene hospital
    #with fade

    "You wake up to the scene of a hospital, unable to make sense of anything."

    "You try to get up but you’re strapped to the bed and can’t move."

    doctor "So what are the results?"

    if stress > 60:
        $ dialogue = "which were unacceptably high, showing lack of mental therapeutic effects."
    else:
        $dialogue = "which shows improvement compared to the previous levels when the patient was admitted."

    nurse "Patient shows a lack of empathy quotient. Even though the murdered victims and the notes placed on their bodies clearly indicated the patient’s involvement, the patient still chose not to believe their involvement. Stress levels were [stress] [dialogue]. Overall, patient has shown little to no improvement."

    doctor "So the experiment failed…"

    doctor "Administer 35 mgs of the Chlordiazepoxide, Clonazepam and Midazolam concoction to wipe the patient’s memories and put them into an induced comma again. We will execute the experiment again after the wait period of 3 days."

    nurse "Understood."

    "Before you can say anything, the nurse injects you with something, and you…slowly…fall…to…sleep…again…"

    #Black screen
    #Game end screen
    return

label Node_GoodvsNeutral:
    $value=60
    if stress>value:
        call Node_Neutral_Ending
    else:
        call Node_Good_Ending
    return


label Node_Neutral_Ending:

    #scene hospital
    #with fade

    "You wake up to the scene of a hospital, unable to make sense of anything."

    "You try to get up but you’re strapped to the bed and can’t move."

    #show nurse

    "The Nurse comes and unstraps you"

    doctor "So what are the results?"

    nurse "The Patient shows a positive empathy quotient. When faced with the consequences of their previous choices, the patient somehow realized what was going on and was ready to accept themselves as the culprit. However, their stress levels were [stress], which were unacceptably high, showing lack of mental therapeutic effects."

    doctor "So the experiment was a partial success?"

    nurse "Quantitatively so."

    doctor "At least it’s progress."

    "You seem confused so the doctor explains."

    doctor "You must be confused. Let me explain. When you were admitted here, you were caught by the police, while committing a murder. Those three murders; you committed them. You suffered from Dissociative identity disorder caused by your elevated levels of stress because of your environment. It was because of that stress, that when you experienced bullying or harassment which you could not tolerate, another personality would take over, so that your mind could cope with the pressure you were feeling. However, this second personality had no moral compass, so it saw fit to remove the hurdles which were affecting your mental state. And by remove the hurdles, I of course mean murder them."

    player "Wait so I murdered those people? How? Wasn’t I here?"

    doctor "No, these murders have happened beforehand, but because of your mental disorder those memories were repressed. You did not remember doing anything. Furthermore, your other personality was quite cunning. It was able to commit all those murders till it was finally caught and you were brought here."

    player "So how was I seeing those memories? And why was I reliving them?"

    doctor "We tried to help you but all other forms of therapy failed. This therapy was one which we have just invented. We put you into a coma using specific medication and hypnosis. Using the hypnosis we were able to tap into those suppressed memories and send you into them, to experience the loss of life as any other bystander would. This forced you to confront your guilt and actions and to make a choice, to either accept your guilt, accept your actions, even though you had very little clues on whether it was your or not, or to neglect everything and act as though you had no hand in it. You chose the former, and accepted that what happened was wrong, and that you probably had some part to play in it."

    player "So am I better now?"

    doctor "You have almost the same stress levels as you had when you were admitted here. However, you accepted that murder is wrong, which your former self didn’t. You tried to live a slightly more healthier and friendlier life in your mental simulation. So I wouldn’t call it a complete failure, but we do need to decrease your stress levels somehow for it to be called a complete success."

    player "Ahhh I see…"

    doctor "Since we weren’t able to help you completely, we will keep you here for slightly longer. We might try other therapies and medicine as well. Since you’ve shown improvement, it’s possible you might finally be cured of your illness."

    player "Thank you doctor, I’ll try my best to get better as soon as I can."

    doctor "And we’ll be here to help you throughout that process."

    "The doctor instructs the nurse to escort you out of the hospital room, and she takes you to another room where you can rest before your next therapy session starts…"

    #Screen slowly fades out
    #Game end screen

    return



label Node_Good_Ending:

    #scene hospital
    #with fade

    "You wake up to the scene of a hospital, unable to make sense of anything."

    "You try to get up but you’re strapped to the bed and can’t move."

    #show nurse

    "The Nurse comes and unstraps you"

    doctor "So what are the results?"

    nurse "The Patient shows a positive empathy quotient. When faced with the consequences of their previous choices, the patient somehow realized what was going on and was ready to accept themselves as the culprit. Their stress levels were [stress], which shows a massive decrease in stress levels than when the patient was first admitted here."

    doctor "So the experiment was a success!"

    nurse "Quantitatively so."

    "You seem confused so the doctor explains."

    doctor "You must be confused. Let me explain. When you were admitted here, you were caught by the police, while committing a murder. Those three murders; you committed them. You suffered from Dissociative identity disorder caused by your elevated levels of stress because of your environment. It was because of that stress, that when you experienced bullying or harassment which you could not tolerate, another personality would take over, so that your mind could cope with the pressure you were feeling. However, this second personality had no moral compass, so it saw fit to remove the hurdles which were affecting your mental state. And by remove the hurdles, I of course mean murder them."

    player "Wait so I murdered those people? How? Wasn’t I here?"

    doctor "No, these murders have happened beforehand, but because of your mental disorder those memories were repressed. You did not remember doing anything. Furthermore, your other personality was quite cunning. It was able to commit all those murders till it was finally caught and you were brought here."

    player "So how was I seeing those memories? And why was I reliving them?"

    doctor "We tried to help you but all other forms of therapy failed. This therapy was one which we have just invented. We put you into a coma using specific medication and hypnosis. Using the hypnosis we were able to tap into those suppressed memories and send you into them, to experience the loss of life as any other bystander would. This forced you to confront your guilt and actions and to make a choice, to either accept your guilt, accept your actions, even though you had very little clues on whether it was your or not, or to neglect everything and act as though you had no hand in it. You chose the former, and accepted that what happened was wrong, and that you probably had some part to play in it."

    player "So am I better now?"

    doctor "You have half the stress levels as when you were admitted here. You accepted that murder is wrong, which your former self didn’t. You tried to live a healthier and friendlier life in your mental simulation. I wouldn’t call that any less than massive improvement."

    player "Ahhh I see…"

    doctor "Be happy, the experiment was a success. Your mental state improved immensely. It is now no more in shatters. In fact you might be able to leave this place soon too."

    player "Thank you doctor, thank you so much."

    doctor "Thank yourself; it was what got you out of this mess."

    "The doctor instructs the nurse to escort you out of the hospital room, and for once in the apparent past few days, you feel optimistic of what’s to come..."

    #Screen slowly fades out
    #Game end screen
    return
