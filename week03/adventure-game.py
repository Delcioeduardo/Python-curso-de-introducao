"""
Adventure game set in an enchanted forest with a cave, a trail, and a cabin.
I added different endings, including victories and defeats, to make every
choice important and encourage other people to play the game again.
"""

def adventure_game():
    print("--- THE MYSTERY OF THE ENCHANTED FOREST ---")
    print("You wake up at the entrance of a mysterious forest with only a lantern.")

    # LEVEL 1: 3 possible choices
    choice1 = input("Do you want to enter the CAVE, follow the TRAIL, or investigate the CABIN? ").strip().upper()

    if choice1 == "CAVE":
        print("\nYou enter the dark cave and hear a strange noise coming from deep inside.")

        # LEVEL 2 (Cave): 2 choices
        choice2 = input("Do you decide to TURN ON the lantern to see better or RUN back? ").strip().upper()

        if choice2 == "TURN ON":
            print("\nThe light reveals a sleeping dragon resting on a pile of gold coins!")

            # LEVEL 3 (Cave -> Turn On): 2 choices
            choice3 = input("Do you want to TAKE the gold or LEAVE quietly? ").strip().upper()

            if choice3 == "TAKE":
                print("\n[ENDING 1] The dragon wakes up because of the noise and turns you into ashes! Game over.")
            elif choice3 == "LEAVE":
                print("\n[ENDING 2] You escape safely and discover that the real treasure is staying alive. Victory!")
            else:
                print("\n[Invalid Option] You hesitated for too long, the dragon woke up and ate you.")

        elif choice2 == "RUN":
            print("\nYou desperately run outside and trip into a hidden hole.")

            # LEVEL 3 (Cave -> Run): 2 choices
            choice3 = input("Do you try to CLIMB out or SHOUT for help? ").strip().upper()

            if choice3 == "CLIMB":
                print("\n[ENDING 3] With great effort, you climb out of the hole and safely return home. Victory!")
            elif choice3 == "SHOUT":
                print("\n[ENDING 4] A pack of wolves hears your screams and comes closer... Game over.")
            else:
                print("\n[Invalid Option] You froze in fear, and no one came to rescue you.")

        else:
            print("\n[Invalid Option] While you were thinking about what to do, the cave entrance collapsed!")

    elif choice1 == "TRAIL":
        print("\nYou walk along the trail and find a river with a very old wooden bridge.")

        # LEVEL 2 (Trail): 2 choices
        choice2 = input("Do you prefer to CROSS the bridge or SWIM across the river? ").strip().upper()

        if choice2 == "CROSS":
            print("\nThe bridge CREAKS with every step, and you reach the middle.")

            # LEVEL 3 (Trail -> Cross): 2 choices
            choice3 = input("Do you decide to RUN to finish quickly or WALK slowly? ").strip().upper()

            if choice3 == "RUN":
                print("\n[ENDING 5] The wooden boards break because of your impact, and you fall into the abyss! Game over.")
            elif choice3 == "WALK":
                print("\n[ENDING 6] You carefully cross the bridge and find the path to the sacred city. Victory!")
            else:
                print("\n[Invalid Option] You stayed still on the bridge until a strong wind knocked it down.")

        elif choice2 == "SWIM":
            print("\nYou jump into the cold water. The current is surprisingly strong.")

            # LEVEL 3 (Trail -> Swim): 2 choices
            choice3 = input("Do you decide to DIVE to escape the current or FLOAT to save energy? ").strip().upper()

            if choice3 == "DIVE":
                print("\n[ENDING 7] You find an underwater tunnel that leads you to a secret chamber full of jewels! Victory!")
            elif choice3 == "FLOAT":
                print("\n[ENDING 8] The current carries you toward a dangerous waterfall. Game over.")
            else:
                print("\n[Invalid Option] You swallowed water because you did not make a decision and drowned.")

        else:
            print("\n[Invalid Option] You took too long to choose, and night fell, leaving you lost on the trail.")

    elif choice1 == "CABIN":
        print("\nYou arrive at an old abandoned cabin with the door slightly open.")

        # LEVEL 2 (Cabin): 2 choices
        choice2 = input("Do you want to ENTER the cabin or PEEK through the window? ").strip().upper()

        if choice2 == "ENTER":
            print("\nInside the cabin, there is an ancient book glowing on the table.")

            # LEVEL 3 (Cabin -> Enter): 2 choices
            choice3 = input("Do you choose to READ the book or BURN the book? ").strip().upper()

            if choice3 == "READ":
                print("\n[ENDING 9] The book is a spellbook that grants you magical powers! Victory!")
            elif choice3 == "BURN":
                print("\n[ENDING 10] When you burn the book, a curse is released and sets the entire forest on fire! Game over.")
            else:
                print("\n[Invalid Option] You hesitated while touching the book, and a trap was activated.")

        elif choice2 == "PEEK":
            print("\nYou look through the dirty window and see a mysterious figure preparing a potion.")

            # LEVEL 3 (Cabin -> Peek): 2 choices
            choice3 = input("Do you decide to KNOCK on the door and introduce yourself or ESCAPE silently? ").strip().upper()

            if choice3 == "KNOCK":
                print("\n[ENDING 11] The figure is a kind wizard who offers you food and a safe map. Victory!")
            elif choice3 == "ESCAPE":
                print("\n[ENDING 12] While escaping, you make noise on the dry branches, and the mysterious figure casts a sleeping spell on you. Game over.")
            else:
                print("\n[Invalid Option] The figure sees your shadow through the window and captures you.")

        else:
            print("\n[Invalid Option] You hesitated at the door, and a pack of creatures surrounded the cabin.")

    else:
        print("\n[Invalid Option] That was not one of the available paths. You stood still until darkness consumed you!")


# Run the game
adventure_game()
