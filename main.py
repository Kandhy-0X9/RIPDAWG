print("Anna: Captain, I detected an anomaly in the engine room.")
print("You: I'm busy right now Anna, can it wait?")
print("Anna: Captain, this is serious. Please check it out.")
print("\nchoices:\n" \
"1. Investigate the anomaly yourself.\n" \
"2. Send a tell Anna to investigate.\n" \
"3. Ignore the anomaly for now.\n")

choice = input("Enter the number of your choice: ")

if choice == '1':
    print("You decide to investigate the anomaly yourself. As you enter the engine room, you notice a strange humming sound coming from one of the reactors.")
    print("You: Again, I should upgrade these reactors soon,\" you think to yourself.")
    print("A black liquid drips on your forehead from a leaking pipe above.")
    print("You: What the...?")
    print("\nChoices:\n"
    "1. Examine the leaking pipe.\n"
    "2. Call Anna for assistance.\n" 
    "3. Leave the engine room immediately.\n")

    choice2 = input("Enter the number of your choice: ")
    if choice2 == '1':
        print("Suddenly you are sprayed with the black liquid, and everything goes dark...")
        print("you have met a tragic end.")
        3# End of this branch
    
    elif choice2 == '2':
        print("Calvin: Anna is busy right now what do you need Cap?")
        print("You: Can you check the pipes, something seems off.")
        print("Calvin: On it Cap.")
        print("Before you can blink, Calvin's top half is gone as blood sprays everywhere.")
        print("\nchoices:\n" 
        "1. Run away screaming.\n"
        "2. Reach out for your Taser.\n"
        "3. Faint from the horror.\n")

        choice3 = input("Enter the number of your choice: ")
        if choice3 == '1':
            print("You run away screaming, but the creature chases you down and you meet a tragic end.")
            # End of this branch
        elif choice3 == '2':
            print("You reach for your Taser and manage to stun the creature long enough but the reactor overloads and you meet a tragic end.")
            # End of this branch
        elif choice3 == '3':
            print("You faint from the horror and the creature leaves you alone thinking you're dead. However, you later succumb to your injuries.")
            print("You wake up in the medbay.")
            print("Anna: Captain what happened to you?")
            print("You: Calvin...where is he?")
            print("Anna: He is okay, he managed to fix the pipes.")
            print("You: He died...The thing in the engine room...it got him.")
            print("Calvin: Cap you good?")
            print("You: Yeah...just a nightmare I guess.")
            print("Anna: Stop being paranoid Captain, everything is fine.\n")
            print("\nMAKE SURE YOU TAKE YOU MEDS NEXT TIME!\n")
            print("TY 4 Playing!")
            # End of this branch
    
    elif choice2 == '3':
        print("You leave the engine room immediately, but as you exit, you hear a loud explosion behind you.")
        print("half the ship is torn apart and you're dragged into space.")
        print("you have met a tragic end.")
        # End of this branch

elif choice == '2':
    print("You tell Anna to investigate the anomaly.")
    print("Anna's Radio: Captain, you should come check this out... static...Captain!!")
    print("You: Anna? Are you okay?")
    print("\nChoices:\n"
    "1. Rush to the engine room to help Anna.\n"
    "2. Try to contact Anna again.\n" 
    "3. Wait for Anna to respond.\n")

    choice2 = input("Enter the number of your choice: ")
    if choice2 == '1':
        print("You rush to the engine room and find trails of blood.")
        print("You: Anna? Anna!!")
        print("\nchoices:\n"
        "1. Follow the blood trail.\n"
        "2. Call for backup.\n"
        "3. Instantiate an emergency lockdown.\n")

        choice3 = input("Enter the number of your choice: ")
        if choice3 == '1':
            print("You follow the blood trail deeper into the engine room and suddenly a creature leaps out and attacks you.")
            print("You have met a tragic end.")
            # End of this branch
        elif choice3 == '2':
            print("Rasta: Capitan man, what de problem man?")
            print("You: There's been an attack in the engine room, I need help!")
            print("Rasta: Count on me man, I gat you. What we doin?")
            print("You: Go in there and secure the area.")
            print("Rasta: On it Capitan.")
            print("You: I will get the others ready.")
            print("\nChoices:\n"
            "1. Close the engine room while Rasta is in there\n"
            "2. Go to the Weaponry to arm yourself.\n"
            "3. Call for help from HQ.\n")
            choice4 = input("Enter the number of your choice: ")
            if choice4 == '1':
                print("You close the engine room door while Rasta is inside.")
                print("After a few moments, you hear a loud thud and silence.")
                print("Congrats! You have eliminated the anomaly but at the cost of Rasta's life.")
                # End of this branch
            elif choice4 == '2':
                print("You head to the Weaponry and arm yourself with a laser rifle.")
                print("You return to the engine room to find Rasta fighting the creature.")
                print("With your help, you manage to subdue the creature and secure the area.")
                print("You: you good Rasta?")
                print("Rasta: What de hell was dat ting man?")
                print("You: I don't know, but we need to report this to HQ.")
                print("You and Rasta look down at the creature, suddenly it sprays black liquid everywhere.")
                print("you have met a tragic end.")
                # End of this branch
            elif choice4 == '3':
                print("You call for help from HQ.")
                print("HQ: This is Nanite Systems, Anyway we can help?")
                print("You: Our ship is under attack by an unknown creature in the engine room. We need immediate assistance.")
                print("HQ:...")
                print("You: I should have known better than to trust Nanite Systems.")
                print("you have met a tragic end.")
                # End of this branch
        elif choice3 == '3':
            print("You initiate an emergency lockdown, sealing the engine room.")
            print("You lock yourself with your crew in the ship and all die of suffocation.")
            print("you have met a tragic end.")
            # End of this branch

    elif choice2 == '2':
        print("You try to contact Anna again but there is no response.")
        print("You: Anna, please respond.")
        print("Suddenly, you hear a loud crash from the engine room.")
        print("\nchoices:\n"
        "1. Rush to the engine room to investigate.\n"
        "2. Call for backup.\n"
        "3. Look at the ship's security cameras.\n")
        choice3 = input("Enter the number of your choice: ")
        if choice3 == '1':
            print("Megan: This is Megan speaking, from security. We have a situation in the engine room. Everyone stay calm.")
            print("you rush to the engine room and find Anna injured but alive.")
            print("Anna: Captain...thank god you came.")
            print("You: What happened here?")
            print("Anna: It was...something...it attacked me.")
            print("Anna: captain watch out!")
            print("you have met a tragic end.")
            # End of this branch
        elif choice3 == '2':
            print("You call for backup.")
            print("You: This is the captain of Bastion one. Anyone copy?")
            print("HQ: This is Nanite Systems, we read you Captain. What's your situation?")
            print("You: Our ship is under attack by an unknown creature in the engine room.")
            print("HQ: We're dispatching a team to assist you. Hold tight.")
            print("You: Thank you.")
            print("You look at the radar")
            print("You: Why is an orbital strike heading towards us?")
            print("you have met a tragic end.")
            # End of this branch
        elif choice3 == '3':
            print("You access the ship's security cameras and see a creature moving through the engine room.")
            print("You what is that thing?")
            print("You suddenly wake up in the medbay.")
            print("Anna: Captain you forgot to take your meds again.")
            print("You: Oh... right.")
            print("\nMAKE SURE YOU TAKE YOU MEDS NEXT TIME!\n")
            print("TY 4 Playing!")
            # End of this branch

elif choice == '3':
    print("The engines suddlenly stop functioning and the ship drifts into an asteroid field.")
    print("You call on the crew to fix the engines but there is no power")
    print("You: Come on... stupid ship")
    print("You look outside the window")
    print("You: We're doomed...")
    print("Congrats to eliminated the anomaly at the expense of the entire crew.")
    print("you have met a tragic end.")
    # End of this branch