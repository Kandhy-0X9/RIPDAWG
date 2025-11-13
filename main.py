import os
import time

def pause(seconds=1.5):
    time.sleep(seconds)

def clear():
    # Clears the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    print("Anna: Captain, I detected an anomaly in the engine room.")
    pause()
    print("You: I'm busy right now Anna, can it wait?")
    pause()
    print("Anna: Captain, this is serious. Please check it out.")
    pause()

    print("\nChoices:\n"
          "1. Investigate the anomaly yourself.\n"
          "2. Tell Anna to investigate.\n"
          "3. Ignore the anomaly for now.\n")

    choice = input("Enter the number of your choice: ")

    # --- Choice 1 ---
    if choice == '1':
        print("\nYou decide to investigate the anomaly yourself. As you enter the engine room, you notice a strange humming sound coming from one of the reactors.")
        pause()
        print('You: "Again, I should upgrade these reactors soon," you think to yourself.')
        pause()
        print("A black liquid drips on your forehead from a leaking pipe above.")
        pause()
        print("You: What the...?")
        pause()

        print("\nChoices:\n"
              "1. Examine the leaking pipe.\n"
              "2. Call Anna for assistance.\n"
              "3. Leave the engine room immediately.\n")

        choice2 = input("Enter the number of your choice: ")

        if choice2 == '1':
            print("\nSuddenly you are sprayed with the black liquid, and everything goes dark...")
            pause()
            print("You have met a tragic end.")
            pause()

        elif choice2 == '2':
            print("\nCalvin: Anna is busy right now, what do you need Cap?")
            pause()
            print("You: Can you check the pipes? Something seems off.")
            pause()
            print("Calvin: On it, Cap.")
            pause()
            print("Before you can blink, Calvin's top half is gone as blood sprays everywhere.")
            pause()

            print("\nChoices:\n"
                  "1. Run away screaming.\n"
                  "2. Reach out for your Taser.\n"
                  "3. Faint from the horror.\n")

            choice3 = input("Enter the number of your choice: ")

            if choice3 == '1':
                print("\nYou run away screaming, but the creature chases you down and you meet a tragic end.")
            elif choice3 == '2':
                print("\nYou reach for your Taser and manage to stun the creature long enough, but the reactor overloads and you meet a tragic end.")
            elif choice3 == '3':
                print("\nYou faint from the horror, and the creature leaves you alone thinking you're dead. However, you later wake up in the medbay.")
                pause()
                print("Anna: Captain, what happened to you?")
                pause()
                print("You: Calvin... where is he?")
                pause()
                print("Anna: He's okay, he managed to fix the pipes.")
                pause()
                print("You: He died... The thing in the engine room... it got him.")
                pause()
                print("Calvin: Cap, you good?")
                pause()
                print("You: Yeah... just a nightmare, I guess.")
                pause()
                print("Anna: Stop being paranoid, Captain. Everything is fine.")
                pause()
                print("\nMAKE SURE YOU TAKE YOUR MEDS NEXT TIME!\n")
                print("TY 4 Playing!")
            else:
                print("Invalid choice.")

        elif choice2 == '3':
            print("\nYou leave the engine room immediately, but as you exit, you hear a loud explosion behind you.")
            pause()
            print("Half the ship is torn apart and you're dragged into space.")
            pause()
            print("You have met a tragic end.")
        else:
            print("Invalid choice.")

    # --- Choice 2 ---
    elif choice == '2':
        print("\nYou tell Anna to investigate the anomaly.")
        pause()
        print("Anna's Radio: Captain, you should come check this out... *static* ...Captain!!")
        pause()
        print("You: Anna? Are you okay?")
        pause()

        print("\nChoices:\n"
              "1. Rush to the engine room to help Anna.\n"
              "2. Try to contact Anna again.\n"
              "3. Wait for Anna to respond.\n")

        choice2 = input("Enter the number of your choice: ")

        if choice2 == '1':
            print("\nYou rush to the engine room and find trails of blood.")
            pause()
            print("You: Anna? Anna!!")
            pause()

            print("\nChoices:\n"
                  "1. Follow the blood trail.\n"
                  "2. Call for backup.\n"
                  "3. Initiate an emergency lockdown.\n")

            choice3 = input("Enter the number of your choice: ")

            if choice3 == '1':
                print("\nYou follow the blood trail deeper into the engine room and suddenly a creature leaps out and attacks you.")
                pause()
                print("You have met a tragic end.")
            elif choice3 == '2':
                print("\nRasta: Capitan man, what de problem man?")
                pause()
                print("You: There's been an attack in the engine room, I need help!")
                pause()
                print("Rasta: Count on me man, I gat you. What we doin'?")
                pause()
                print("You: Go in there and secure the area.")
                pause()
                print("Rasta: On it, Capitan.")
                pause()
                print("You: I will get the others ready.")
                pause()

                print("\nChoices:\n"
                      "1. Close the engine room while Rasta is in there.\n"
                      "2. Go to the Weaponry to arm yourself.\n"
                      "3. Call for help from HQ.\n")

                choice4 = input("Enter the number of your choice: ")

                if choice4 == '1':
                    print("\nYou close the engine room door while Rasta is inside.")
                    pause()
                    print("After a few moments, you hear a loud thud and silence.")
                    pause()
                    print("Congrats! You have eliminated the anomaly but at the cost of Rasta's life.")
                elif choice4 == '2':
                    print("\nYou head to the Weaponry and arm yourself with a laser rifle.")
                    pause()
                    print("You return to the engine room to find Rasta fighting the creature.")
                    pause()
                    print("With your help, you manage to subdue the creature and secure the area.")
                    pause()
                    print("You: You good, Rasta?")
                    pause()
                    print("Rasta: What de hell was dat ting, man?")
                    pause()
                    print("You: I don't know, but we need to report this to HQ.")
                    pause()
                    print("You and Rasta look down at the creature—suddenly it sprays black liquid everywhere.")
                    pause()
                    print("You have met a tragic end.")
                elif choice4 == '3':
                    print("\nYou call for help from HQ.")
                    pause()
                    print("HQ: This is Nanite Systems, anyway we can help?")
                    pause()
                    print("You: Our ship is under attack by an unknown creature in the engine room. We need immediate assistance.")
                    pause()
                    print("HQ: ...")
                    pause()
                    print("You: I should have known better than to trust Nanite Systems.")
                    pause()
                    print("You have met a tragic end.")
                else:
                    print("Invalid choice.")

            elif choice3 == '3':
                print("\nYou initiate an emergency lockdown, sealing the engine room.")
                pause()
                print("You lock yourself with your crew in the ship and all die of suffocation.")
                pause()
                print("You have met a tragic end.")
            else:
                print("Invalid choice.")

        elif choice2 == '2':
            print("\nYou try to contact Anna again but there is no response.")
            pause()
            print("You: Anna, please respond.")
            pause()
            print("Suddenly, you hear a loud crash from the engine room.")
            pause()

            print("\nChoices:\n"
                  "1. Rush to the engine room.\n"
                  "2. Call for backup.\n"
                  "3. Check the ship's security cameras.\n")

            choice3 = input("Enter the number of your choice: ")

            if choice3 == '1':
                print("\nMegan: This is Megan from security. We have a situation in the engine room. Everyone stay calm.")
                pause()
                print("You rush to the engine room and find Anna injured but alive.")
                pause()
                print("Anna: Captain... thank god you came.")
                pause()
                print("You: What happened here?")
                pause()
                print("Anna: It was... something... it attacked me.")
                pause()
                print("Anna: Captain, watch out!")
                pause()
                print("You have met a tragic end.")
            elif choice3 == '2':
                print("\nYou call for backup.")
                pause()
                print("You: This is the Captain of Bastion One. Anyone copy?")
                pause()
                print("HQ: This is Nanite Systems, we read you Captain. What's your situation?")
                pause()
                print("You: Our ship is under attack by an unknown creature in the engine room.")
                pause()
                print("HQ: We're dispatching a team to assist you. Hold tight.")
                pause()
                print("You: Thank you.")
                pause()
                print("You look at the radar.")
                pause()
                print("You: Why is an orbital strike heading towards us?")
                pause()
                print("You have met a tragic end.")
            elif choice3 == '3':
                print("\nYou access the ship's security cameras and see a creature moving through the engine room.")
                pause()
                print("You: What is that thing?")
                pause()
                print("You suddenly wake up in the medbay.")
                pause()
                print("Anna: Captain, you forgot to take your meds again.")
                pause()
                print("You: Oh... right.")
                pause()
                print("\nMAKE SURE YOU TAKE YOUR MEDS NEXT TIME!\n")
                print("TY 4 Playing!")
            else:
                print("Invalid choice.")

        elif choice2 == '3':
            print("\nYou wait for Anna to respond...")
            pause(3)
            print("No answer ever comes. Silence fills the ship.")
            pause()
            print("You have met a tragic end.")
        else:
            print("Invalid choice.")

    # --- Choice 3 ---
    elif choice == '3':
        print("\nThe engines suddenly stop functioning and the ship drifts into an asteroid field.")
        pause()
        print("You call on the crew to fix the engines but there is no power.")
        pause()
        print("You: Come on... stupid ship.")
        pause()
        print("You look outside the window.")
        pause()
        print("You: We're doomed...")
        pause()
        print("Congrats, you eliminated the anomaly at the expense of the entire crew.")
        pause()
        print("You have met a tragic end.")
    else:
        print("Invalid choice.")

    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if replay == "yes":
        clear()
        print("\n--- Restarting the story ---\n")
        pause()
        main()
    else:
        print("\nGoodbye, Captain.")

if __name__ == "__main__":
    main()
