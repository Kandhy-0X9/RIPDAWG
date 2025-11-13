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

    elif choice2 == '2':
        print("You try to contact Anna again but there is no response.")
        print("You: Anna, please respond.")
        print("Suddenly, you hear a loud crash from the engine room.")
        print("\nchoices:\n"
        "1. Rush to the engine room to investigate.\n"
        "2. Call for backup.\n"
        "3. Look at the ship's security cameras.\n")
        

elif choice == '3':
    print("The engines suddlenly stop functioning and the ship drifts into an asteroid field.")
    print("You call on the crew to fix the engines but there is no power")
    print("You: Come on... stupid ship")
    print("You look outside the window")
    print("You: We're doomed...")
    print("Congrats to eliminated the anomaly at the expense of the entire crew.")
    print("you have met a tragic end.")
    # End of this branch