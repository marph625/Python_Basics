### ACTIONS ###

def you_died(why):
    print(f"{why} Bruh.\n\n<GAME OVER>")
    exit(0)

### END ACTIONS ###

### CHARACTERS ###

def guard():

    '''
    Encountering the guard, the player chooses to attack, check or sneak.
    - attack: player dies and the game is over
    - check: sees what the guard is doing, but nothing else happens, and get 3 options again
    - sneak: player sneaks past the guard and wins the game
    '''

    # Actions on the guard
    check_str = "You see the guard is still sleeping, you need to get to that door on the right of him. What are you waiting for?"
    sneak_str = "You approach the guard, he's still sleeping. Reaching for the door, you open it slowly and slip out."
    attack_str = "You swiftly run towards the sleeping guard and knock him out with the hilt of your shiny sword. Unfortunately it wasn't hard enough."
    retreat_str = "That is too risky! That guard is sleeping but heavily armed and armored!"

    actions_dict = {"check" : check_str, "sneak" : sneak_str, "attack" : attack_str, "retreat" : retreat_str}

    print("\nYou take a look at the sleeping guard and think about what to do now.")

    # While loop
    while True:
        action = input("\nWhat do you do? [attack | check | sneak | retreat]\n > ")
        if action in actions_dict.keys():

            # check is just printed and the loop continues in line 36
            print(f"\n{actions_dict[action]}")
            if action == "sneak":
                print("\nYou just slipped through the door before the guard realised it.")
                print("You are now outside and free. Congratulations!")

                # return ends the loop (idk why tbh)
                return                
            elif action == "attack":
                you_died("\nThe guard woke up with a grunt, reached for his dagger and before you know it, the world goes dark and you just died.")
            elif action == "retreat":
                print("You decided to retreat for now and think again.")
                blue_door_room()
                

### END CHARACTERS ###

##### START ROOMS #####

def blue_door_room():
    '''
    The player finds a treasure chest, options to investigate the treasure chest or guard.

    If player chooses
    - Treasure chest: show its contents; option to take treasure or ignore it (proceeds to guard)
    - Guard: nothing for now
    '''

    # So our treasure_chest list contains 4 items
    treasure_chest = ["diamonds", "gold", "silver", "sword"]

    print("\nYou enter the blue room and see a treasure chest on your left.")
    print("On the right is a door but a sleeping guard blocks it.")
    print("Where do you go? Left or Right?")

    # Ask player what to do
    action = input("\nleft or right?\n > ")

    # This is a way to see if the text typed by the player is in the list
    if action.lower() in ["treasure", "chest", "left"]:
        print("\nOooh, treasure!")
        print("Open it? Press '1'")
        print("Leave it alone? Press '2'")
        choice = input("\n > ")
        
        if choice == "1":        
            print("\nLet's see what's in here...")
            print("The chest creaks open loudly but the guard is STILL sleeping. That's one heavy sleeper!")
            print("\nYou found some:")

            # for each treasure (variable created on the fly in the for loop)
            # in the list treasure_chest
            # print treasure
            for treasure in treasure_chest:
                print(treasure)

            # So much for treasure, what to do? Take it or leave it.
            print("\nWhat do you want to do?")

            # Get a number of items in treasure chest with len()
            num_items_in_chest = len(treasure_chest)

            print(f"\nTo take all {num_items_in_chest} treasure items, press '1'")
            print("Leave it, press '2'")

            treasure_choice = input("\n > ")
            if treasure_choice == "1":
                treasure_chest.remove("sword")
                print("\nYou take the shinier sword from the treasure chest. It is well balanced.")
                print("Woohoo! Bounty and a shiny new sword. /drop your crappy sword into the empty treasure chest.")

                # Temporary variable is created and assigned to a copy of treasure_chest
                temp_treasure_list = treasure_chest[:]

                '''
                Temporary variable 'treasure_contents' is created and assined to the remaining 
                elements from 'treasure_chest' and prints them all, separated by a ", "
                
                '''

                treasure_contents = ", ".join(treasure_chest)
                print(f"\nYou also receive: {treasure_contents}.")

                # Removing all the rest of the items in the treasure chest
                for treasure in temp_treasure_list:
                    # Use list remove() function to remove each item in the chest.
                    treasure_chest.remove(treasure)

                # Add the old sword in place of the new sword
                treasure_chest.append("old sword")
                print(f"\nYou close the lid of the chest containing {treasure_chest} for the next adventurer.")
                print(f"Now onward to get past this sleeping guard and the door to freedom.")
                guard()
            
            elif treasure_choice == "2":
                print("\nIt will still be here (I hope), right after I get past this guard.")
                guard()
        
        elif choice == "2":
            print("\nThe guard is more interesting. Let's pay him a visit.")
            guard()
    elif action.lower() in ["guard", "right"]:
        print("\nThe guard is more interesting. Let's pay him a visit.")
        guard()    
    else:
        print("\nWell, not sure what you picked there. Let's poke the guard cos it's fun!")

def red_door_room():
    print("\nThere you see a great red dragon.")
    print("It stares at you with one narrowed eye.")
    print("Do you flee or fight?")

    action = input("\n > ")

    if "flee" in action:
        print("\nWell, that was close. Better be prepared next time.")
        start_adventure()
    else:
        you_died("\nThe dragon just ate you. Well, that was tasty!")

    # Add possibility to fight with your new sword

    if "fight" in action:
        
        pass

### END ROOMS ###

def start_adventure():
    print("\nYou enter a room with a red door and a blue door.")
    print("Which door do you pick?")

    door_picked = input("\nred or blue? \n > ")

    if door_picked == "red":
        red_door_room()
    elif door_picked == "blue":
        blue_door_room()
    else:
        print("\nHow hard is it to write 'red' or 'blue'?? Are you stupid or something?")
        start_adventure()

def main():
    player_name = input("What's your name?\n > ")
    print(f"\nYour name is {player_name.upper()}. Let's start an adventure")
    start_adventure()

if __name__ == "__main__":
    main()