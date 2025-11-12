print("Anna: Captain, I detected an anomaly in the engine room.")
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
        elif choice3 == '2':
            print("You reach for your Taser and manage to stun the creature long enough but the reactor overloads and you meet a tragic end.")
        elif choice3 == '3':
            print("You faint from the horror and the creature leaves you alone thinking you're dead. However, you later succumb to your injuries.")


elif choice == '2':
    print("You tell Anna to investigate the anomaly.")
    print("Anna's Radio: Captain, you should come check this out... static...Captain!!")
    print("You: Anna? Are you okay?")
    print("\nChoices:\n"
    "1. Rush to the engine room to help Anna.\n"
    "2. Try to contact Anna again.\n" 
    "3. Wait for Anna to respond.\n")

    # choice2 = input("Enter the number of your choice: ")