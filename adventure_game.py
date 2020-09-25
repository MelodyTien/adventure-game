import time
import random


def printPause(words):
    print(words)
    time.sleep(1)


def validInput(words, validInputs):
    while True:
        choice = input(words)
        if choice in validInputs:
            break
    return choice


def fight():
    if gotNewDagger is False:
        printPause("You do your best...")
        printPause(f"but your {weapon} is no match for the {creature}.")
        printPause("You have been defeatd!")
    else:
        printPause("The Sword of Ogoroth shines brightly in your hand "
                   "as you brace yourself for the attack.")
        printPause("But the dragon takes one look at your "
                   "shink new toy and runs away!")
        printPause("You have rid the town of the dragon. You are victorious!")


def field():
    printPause("\nEnter 1 to knock on the door of the house.")
    printPause("Enter 2 to peer into the cave.")
    printPause("What would you like to do?")


def house():
    printPause("You approach the door of the house.")
    printPause("You are about to knock when the door opens "
               f"and out steps a {creature}.")
    printPause(f"Eep! This is the {creature}'s house!")
    printPause(f"The {creature} attacks you!")
    if gotNewDagger is False:
        printPause("You feel a bit under-prepared for this, "
                   f"what with only having a tiny {weapon}.")


def cave():
    global gotNewDagger
    printPause("You peer cautiously into the cave.")
    if gotNewDagger is False:
        printPause("It turns out to be only a very small cave.")
        printPause("Your eye catches a glint of metal behind a rock.")
        printPause("You have found the magical Sword of Ogoroth!")
        printPause(f"You discard your silly old {weapon} "
                   "and take the sword with you.")
        printPause("You walk back out to the filed.")
        gotNewDagger = True
    else:
        printPause("You've been here before, and gotten all the good stuff. "
                   "It's just an empty cave now.")
        printPause("You walk back out to the field.")


def reset():
    global weapon
    global creature
    global gotNewDagger
    weapon = random.choice(weaponList)
    creature = random.choice(creatureList)
    gotNewDagger = False


def playGame():

    while True:
        printPause("You find yourself standing in an open field, "
                   "filled with grass and yellow wildflowers.")
        printPause(f"Rumor has it that a {creature} is somewhere around here, "
                   "and has been terrifying the nearby village.")
        printPause("In front of you is a house.")
        printPause("To your right is a dark cave.")
        printPause("In your hand you hold your trusty "
                   f"(but not very effective) {weapon}.")

        while True:
            field()
            whereToGo = validInput("(Please enter 1 or 2).\n", ['1', '2'])

            if whereToGo == '1':  # house
                print()
                house()
                choice = validInput("Would you like to (1) fight or "
                                    "(2) run away?", ['1', '2'])
                if choice == '1':  # fight
                    fight()
                    break
                elif choice == '2':  # run away
                    printPause("You run back into the field. Luckily, "
                               "you don't seem to have been follow.")
            elif whereToGo == '2':  # cave
                cave()

        again = validInput("Would you like to play again? (y/n)", ['y', 'n'])
        if again == 'y':
            printPause("Excellent! Restarting the game...")
            reset()
        else:
            printPause("Thanks for playing! See you next time.")
            break


if __name__ == '__main__':
    gotNewDagger = False
    creatureList = ['gorgon', 'troll', 'dragon', 'witch', 'pig']
    weaponList = ['dagger', 'fork', 'spoon']
    weapon = random.choice(weaponList)
    creature = random.choice(creatureList)
    playGame()
