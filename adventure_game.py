import time
import random


location_options = ['Indian', 'Pacific', 'Atlantic']
location = random.choice(location_options)


def welcome():
    print_pause("Welcome to the Adventure Game.\n", 2)
    global player
    player = input("Please enter your name.\n")
    type_slow("Hello {}, best of luck!".format(player), 0.05, 2)
    create_space(5)


def print_pause(message_to_print, time_to_wait):
    print(message_to_print)
    time.sleep(time_to_wait)


def type_slow(message, type_speed, pause):
    for letter in message:
        time.sleep(type_speed)
        print(letter, end='')
    time.sleep(pause)


def create_space(lines):
    i = 0
    for i in range(lines):
        i = i + 1
        print("")


def intro():
    type_slow("You wake up, feeling very drowsy and "
              "disorientated.\n", 0.05, 3)
    type_slow("Your head is bleeding.\n", 0.05, 3)
    type_slow("Opening your eyes, you notice you are "
              "lying on a beach.\n", 0.05, 2)
    type_slow("Where am I?\n", 0.05, 5)
    type_slow("You reailse your plane must have crashed somewhere across the"
              " {} Ocean".format(location), 0.05, 0)
    type_slow("....\n", 1.5, 2)
    type_slow("You find the strength to get to your feet.\n", 0.05, 2)


'#associated with the sleep function'


def sleep(items):
    if "survivors" in items and "sleep" in items:
        type_slow("Do you really think this is the time to take"
                  " another nap {}?\n".format(player), 0.05, 2)
        decisions(items)
    elif "survivors" in items and "sleep" not in items:
        type_slow("The other team members are a little surprised that "
                  "you have taken"
                  " the opportunity to nap given the situation.\n", 0.05, 2)
        type_slow("They have decided to isolate you from the "
                  "group.\n", 0.05, 2)
        type_slow("Good luck surviving from here.\n", 0.05, 2)
        type_slow("Should you beg for forgiveness?\n", 0.05, 2)
        items.append("sleep")
        forgiveness(items)
    else:
        type_slow("You take a 20 minute nap.", 0.05, 2)
        type_slow("....\n", 0.03, 2)
        type_slow("You wake feeling a little more focussed.\n", 0.05, 2)
        type_slow("However you realise this isn't a bad dream.\n", 0.05, 2)
        type_slow("You decide it is now time to handle this "
                  "situation.\n", 0.05, 2)
        items.append("sleep")
        decisions(items)


def forgiveness(items):
    option = input("1.Yes\n"
                   "2.No\n")
    if option == '1':
        type_slow("The group has considered your offer - and "
                  "they accept.\n", 0.05, 2)
        type_slow("Because they haven't taken naps, they feel "
                  "pretty frazzled.\n", 0.05, 2)
        type_slow("They have voted that despite this hiccup, "
                  "you show some quite good leadership qualities.\n", 0.05, 2)
        type_slow("Surprisingly, your extra sleep has crowned "
                  "you leader.\n", 0.05, 2)
        type_slow("The other survivors are going to have a kip now "
                  "and await your next decision.\n", 0.05, 2)
        items.append("leader")
        decisions(items)
    elif option == '2':
        type_slow("Guess you're on your own now. So much for "
                  "power in numbers....\n", 0.05, 2)
        type_slow("Game over\n", 0.05, 2)
        play_again()
    else:
        type_slow("Please enter a number between 1 and 2.\n", 0.05, 2)
        forgiveness(items)


'#associated with the survivors'


def survivors(items):
    if "survivors" not in items and "sleep" in items:
        type_slow("You shout out as loud as you can.\n", 0.05, 2)
        type_slow("Three people walk over to you, uninjured, "
                  "but distressed.\n", 0.05, 2)
        type_slow("They say you look injured but mentally focussed "
                  "(perhaps after than extra nap).\n", 0.05, 2)
        type_slow("They are willing to be guided by your "
                  "decisions.\n", 0.05, 2)
        items.append("survivors")
        items.append("leader")
        decisions(items)
    elif "survivors" not in items and "sleep" not in items:
        type_slow("You shout out as loud as you can.\n", 0.05, 2)
        type_slow("Three people walk over to you, uninjured, "
                  "but distressed.\n", 0.05, 2)
        items.append("survivors")
        decisions(items)
    else:
        type_slow("You have located all the survivors, "
                  "unfortunately.\n", 0.05, 2)
        type_slow("Luckily your family is home safe "
                  "in San Francisco.\n", 0.05, 2)
        decisions(items)


'#associated with the resources'


def resources(items):
    if "survivors" in items and "wood" in items and "food" in items:
        type_slow("You have located all the resources, "
                  "unfortunately.\n", 0.05, 2)
        decisions(items)
    elif "survivors" in items and "wood" not in items and "food" not in items:
        type_slow("A survivor mentions the plane wreckage "
                  "is 1km away.\n", 0.05, 2)
        type_slow("Would you like all survivors to go, or "
                  "just one?\n", 0.05, 2)
        delegate_survivors(items)
    elif "survivors" in items and "food" in items and "wood" not in items:
        type_slow("You have plenty of food, but perhaps "
                  "some wood would come in handy.\n", 0.05, 2)
        wood(items)
    elif "survivors" not in items and "food" not in items \
            and "wood" not in items:
        type_slow("You think you can see smoke about 1km away "
                  "but you are in poor health to move too far.\n", 0.05, 2)
        type_slow("Should you go looking for supplies by yourself "
                  "in this condition?\n", 0.05, 2)
        risk_it(items)
    elif "survivors" not in items and "food" in items and "wood" not in items:
        type_slow("You have already checked out the plane.\n", 0.05, 2)
        type_slow("Should you go looking for more supplies by "
                  "yourself in this condition?\n", 0.05, 2)
        risk_it(items)


def wood(items):
    wood_search = input("1.Yes, ask the team to look for wood.\n"
                        "2.Nah, she'll be right mate. "
                        "All sorted with supplies.\n")
    if wood_search == '1':
        type_slow("Feeling better after receiving medical attention, "
                  "you lead the group to find wood.\n", 0.05, 2)
        type_slow("You return with an abundance of wood.\n", 0.05, 2)
        items.append("wood")
        decisions(items)
    if wood_search == '2':
        type_slow("Fair enough. Your call.\n", 0.05, 2)
        decisions(items)
    else:
        type_slow("Please enter a number between 1 and 2.\n", 0.05, 2)
        wood(items)


def delegate_survivors(items):
    supplies = input("1.Just one.\n"
                     "2.Everyone go.\n")
    if supplies == '1':
        type_slow("One survivor wanders off towards the plane"
                  " site.\n", 0.05, 2)
        type_slow("What would you like the other survivors"
                  " to do?\n", 0.05, 2)
        wood_vs_food(items)
    elif supplies == '2':
        type_slow("The survivors return with multiple crates of food "
                  "and medical supplies.\n", 0.05, 2)
        type_slow("One of them uses the medical supplies to attend"
                  " to your injuries.\n", 0.05, 2)
        type_slow("That feels better.\n", 0.05, 2)
        items.append("food")
        decisions(items)
    else:
        type_slow("Please make a decision of either "
                  "1 or 2.\n", 0.05, 2)
        delegate_survivors(items)


def wood_vs_food(items):
    others = input("1.Stay here.\n"
                   "2.Order to go look for wood.\n")
    if others == '1':
        type_slow("The survivor returns with a crate of food and "
                  "medical supplies.\n", 0.05, 2)
        type_slow("Medical supplies are administered to you for "
                  "your head injury.\n", 0.05, 2)
        items.append("food")
        decisions(items)
    elif others == '2':
        type_slow("The survivors return with a crate of food and "
                  "medical supplies.\n", 0.05, 2)
        type_slow("The other survivors return with stray"
                  " dried branches.\n", 0.05, 2)
        items.append("food")
        items.append("wood")
        decisions(items)
    else:
        type_slow("Please make a decision of either "
                  "1 or 2\n", 0.05, 2)
        wood_vs_food(items)


def risk_it(items):
    solo = input("1.Yes, risk it for a biscuit.\n"
                 "2.No, I know my limitations.\n")
    if solo == '1':
        type_slow("You start wandering towards smoke "
                  "and collapse "
                  "of exhaustion.\n", 0.05, 2)
        type_slow("Game over.\n", 0.05, 2)
        play_again()
    elif solo == '2':
        type_slow("Good decision, Einstein.\n", 0.05, 2)
        type_slow("Perhaps only as a last resort.\n", 0.05, 2)
        decisions(items)
    else:
        type_slow("Please enter a number between 1 and 2.\n", 0.05, 2)
        risk_it(items)


'#associated with building the hut'


def shelter(items):
    if "wood" in items and "food" in items and "survivors" in items and \
            "fire" not in items:
        type_slow("Together you build a hut to shelter you from "
                  "the elements.\n", 0.05, 2)
        type_slow("It is exhausting work under this Sun.\n", 0.05, 2)
        type_slow("You all reenergise with some food supplies.\n", 0.05, 2)
        items.append("shelter")
        decisions(items)
    elif "food" in items and "wood" not in items and 'survivors' not in items:
        type_slow("You have food, but you might need "
                  "some resources "
                  "and support to build the shelter.\n", 0.05, 2)
        decisions(items)
    elif "food" not in items and "wood" not in items and 'survivors' in items:
        type_slow("You have the help, but you have nothing "
                  "to build this with...yet.\n", 0.05, 2)
        decisions(items)
    elif "food" not in items and "wood" not in items and "survivors" \
            not in items and "sleep" in items:
        type_slow("If you spent a little less time napping, and a "
                  "little more time hunter gathering, "
                  "you might be in less of a mess.\n", 0.05, 2)
        type_slow("You need wood and some assistance building"
                  " this shelter, particularly given "
                  "your condition.\n", 0.05, 2)
        decisions(items)
    elif "food" in items and "wood" in items and "survivors" in items \
            and "fire" in items and "shelter" not in items:
        type_slow("All your wood has been used on building "
                  "this raging fire.\n", 0.05, 2)
        type_slow("Some survivors leave to go search for more "
                  "wood and don't return.\n", 0.05, 2)
        type_slow("The significant heat from this fire leaves you "
                  "and the other survivor quite dehydrated.\n", 0.05, 2)
        type_slow("The other survivor walks off to search for the "
                  "other two - and takes some food supplies.\n", 0.05, 2)
        type_slow("It is at this point that you wish the game designer "
                  "had created the option to not "
                  "burn all the wood.\n", 0.05, 2)
        type_slow("Game over.\n", 0.05, 2)
        play_again()
    elif "food" in items and "wood" not in items and 'survivors' in items:
        type_slow("You have the help, and food to eat "
                  "inside your future hut, but"
                  " you have nothing to build this with...yet.\n", 0.05, 2)
        decisions(items)
    elif "food" in items and "wood" not in items and 'survivors' not in items:
        type_slow("You might need some resources and support "
                  "in building your shelter.\n", 0.05, 2)
        decisions(items)
    else:
        type_slow("You need wood, energy and some assistance building this "
                  "shelter; particularly given your condition.\n", 0.05, 2)
        decisions(items)


'#associated with starting a fire'


def fire(items):
    if "survivors" in items and "food" in items and "wood" in items and \
            "shelter" in items and 'fire' not in items:
        type_slow("You create a small fire with the wood you have"
                  " left from the shelter.\n", 0.05, 2)
        type_slow("Thankfully you have protection from the elements, "
                  "so you can take it in turns to find more wood "
                  "to increase its strength.\n", 0.05, 2)
        type_slow("During the day, the fire intensity increases.\n", 0.05, 2)
        type_slow("On day two, a search plane discovers your "
                  "smoke trail.\n", 0.05, 2)
        type_slow("It is now a week later, and you are reunited with your "
                  "family, as you sign a book deal describing "
                  "your ordeal.\n", 0.05, 2)
    elif "survivors" in items and "food" in items and "wood" in items and \
            "shelter" not in items and 'fire' not in items:
        type_slow("You create a large fire with all the wood "
                  "you have collected.\n", 0.05, 2)
        type_slow("The smoke trail is significant, however with no shelter "
                  "you are all getting exhausted.\n", 0.05, 2)
        type_slow("Will someone find you in time? It is a gamble.\n", 0.05, 2)
        items.append("fire")
        decisions(items)
    else:
        type_slow("You can't build a fire out of thin air,"
                  " or can you?\n", 0.05, 2)
        decisions(items)


'#main decision tree'


def decisions(items):
    type_slow("What do you choose to do next {}?\n".format(player), 0.05, 1)
    decision = input("1.Go back to sleep.\n"
                     "2.Search for other survivors.\n"
                     "3.Search for resources.\n"
                     "4.Build hut.\n"
                     "5.Create signal fire and warmth.\n")
    if decision == '1':
        sleep(items)
    elif decision == '2':
        survivors(items)
    elif decision == '3':
        resources(items)
    elif decision == '4':
        shelter(items)
    elif decision == '5':
        fire(items)
    else:
        print_pause("Please enter a number between 1 and 5.\n", 2)
        decisions(items)


'#playing game again function - used following a game over.'


def play_again():
    type_slow("Would you like to play again {}?\n".format(player), 0.05, 2)
    play_again = input("y = yes/n = no\n")
    if play_again == 'y':
        create_space(5)
        items = []
        intro()
        decisions(items)
    elif play_again == 'n':
        type_slow("Goodbye, thanks for playing {}!\n".format(player), 0.05, 2)
    else:
        type_slow("Please enter y or n", 0.05, 2)
        play_again()


def play_game():
    items = []
    welcome()
    intro()
    decisions(items)


play_game()
