import time
import random

defense_list = ["Hylian Shield", "Mirror Shield", "Golden Gauntlets"]
defense = random.choice(defense_list)

offense_list = ["Master Sword", "Biggoron's Sword", "Great Fairy's Sword"]
offense = random.choice(offense_list)


def print_pause(statement, delay):
    print(statement)
    time.sleep(delay)


def valid_input_2(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("I don't know what that means", 3)
    return response


def valid_input_3(prompt, option1, option2, option3):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        elif option3 in response:
            break
        else:
            print_pause("I don't know what that means", 3)
    return response


def intro():
    print_pause("It's your first day in the simulation", 2)
    print_pause("You load in and walk into a room with "
                "three doors.", 2)
    print_pause("The first door is red.", 2)
    print_pause("The second door is green.", 2)
    print_pause("And the third door is blue.", 2)


def red_door(items):
    print_pause("You walk up to the red door.", 2)
    if {defense} in items:
        print_pause("The door is shut.", 2)
        print_pause("You made sure to lock "
                    "it on the way out.", 2)
        many_doors(items)
    else:
        print_pause("The door is slightly ajar.", 2)
        print_pause("You push it open, and see "
                    f"the {defense}", 2)
        print_pause("You take it. Might come in handy.", 2)
        items.append(f"{defense}")
        many_doors(items)


def green_door(items):
    print_pause("You walk up to the green door.", 2)
    print_pause("...", 1)
    print_pause("...", 1)
    print_pause("...", 1)
    if defense in items:
        if offense in items:
            print_pause("You hear loud chanting on the other side.", 2)
            enter_leave = valid_input_2("Do you enter or leave?\n",
                                        "enter", "leave")
            if "enter" in enter_leave:
                print_pause("You open the door", 2)
                print_pause("A crazed knight awaits on the otherside!", 2)
                print_pause("You fight valiently, and win!", 2)
                print_pause("Congratulations!", 2)
                play_again(items)
            elif "leave" in enter_leave:
                many_doors(items)
        else:
            print_pause("Someone is inside.", 2)
            print_pause("You can hear it.", 2)
            enter_leave = valid_input_2("Do you enter or leave?\n",
                                        "enter", "leave")
            if "enter" in enter_leave:
                print_pause("You open the door", 2)
                print_pause("A knight awaits on the otherside", 2)
                print_pause("You fight valiently, but are bested.", 2)
                print_pause("You should use a sword next time.", 2)
                play_again(items)
            elif "leave" in enter_leave:
                many_doors(items)
    elif offense in items:
        print_pause("Someone is inside.", 2)
        print_pause("You can hear it.", 2)
        enter_leave = valid_input_2("Do you enter or leave?\n",
                                    "enter", "leave")
        if "enter" in enter_leave:
            print_pause("You open the door", 2)
            print_pause("A knight awaits on the otherside", 2)
            print_pause("You fight valiently, but are bested "
                        "by the knight and their superior armour.", 2)
            play_again(items)
        elif "leave" in enter_leave:
            many_doors(items)
    else:
        print_pause("It's quiet... Too quiet...", 2)
        enter_leave = valid_input_2("Do you enter or leave?\n",
                                    "enter", "leave")
        if "enter" in enter_leave:
            print_pause("You open the door", 2)
            print_pause("An arrow hits you straight in the head, "
                        "and you die", 2)
            play_again(items)
        elif "leave" in enter_leave:
            many_doors(items)


def blue_door(items):
    print_pause("You walk up to the blue door.", 2)
    if offense in items:
        print_pause("The doorhandle has turned to stone.", 2)
        print_pause("You can't open this door anymore.", 2)
        many_doors(items)
    else:
        print_pause("The doorknob turns on its own", 2)
        print_pause(f"The {offense} is "
                    "sitting across the room.", 2)
        print_pause("You pull the sword "
                    "from the sheath", 2)
        items.append(offense)
        many_doors(items)


def play_again(items):
    again = valid_input_2("Would you like to play again? Yes/No\n",
                          "yes", "no")
    if "yes" in again:
        adventure_game()
    if "no" in again:
        print_pause("Come back soon!", 2)


def many_doors(items):
    print_pause("What door would you like to open?", 2)
    door = valid_input_3("The red door, the green door, "
                         "or the blue door?\n", "red", "green", "blue")
    if "red" in door:
        red_door(items)
    elif "green" in door:
        green_door(items)
    elif "blue" in door:
        blue_door(items)


def adventure_game():
    items = []
    intro()
    many_doors(items)


adventure_game()
