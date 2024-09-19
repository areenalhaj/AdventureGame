import random
import time

# --- Database starts ---
enemies = [
    "troll",
    "wicked fairie",
    "cobra",
    "ogre",
    "pirate",
    "gorgon",
    "dragon",
]
weapons = ["dagger", "stone", "knife"]


# opens new page by printing 41 new lines
def new_page():
    lines(41)


# printing the number of lines you give
def lines(n):
    print(n * "\n")


# printing with 1 second sleep time after
def print_slowly(word):
    print(word)
    time.sleep(2)


# printing with new line after and 1 second sleep time after
def printl_slowly(word):
    print_slowly(word + "\n")


# takes the question and puts it in input to take the answer
# from user and returns the answer
def answer_this(question):
    choice = input(question)
    return choice


# takes the input and the valid options and checks if the input
# is included in the given valid options or not
def check_valid(choice, options):
    if choice in options:
        return True
    else:
        return False


# prints the introduction story
def intro_story():
    print_slowly("You find yourself standing in an open field,")
    print_slowly("filled with grass and yellow wildflowers.")
    print_slowly(f"Rumor has it that a {enemy} is somewhere around here,")
    print_slowly("and has been terrifying the nearby village....")
    print_slowly("In front of you is a house.")
    print_slowly("To your right is a dark cave.")
    printl_slowly(
        f"In your hand you hold your trusty (but not very effective) {weapon}."
    )


# the Scenario of going to the field
def field():
    global cave_state
    global super
    answer = ""
    print_slowly("Enter 1 to knock on the door of the house.")
    print_slowly("Enter 2 to peer into the cave.")
    print_slowly("What would you like to do?")
    while not check_valid(answer, ["1", "2"]):
        answer = answer_this("(Please enter 1 or 2).\n")
    if answer == "1":
        house()
    else:  # answer='2'
        cave()
        cave_state = True
        field()


# the Scenario of going to the house
def house():
    global super
    print_slowly("You approach the door of the house.")
    print_slowly("You are about to knock when the door"
                 f" opens and out steps a {enemy}.")
    print_slowly(f"Eep! This is the {enemy}'s house!")
    print_slowly(f"The {enemy} attacks you!")
    if not super:
        print_slowly(
            "You feel a bit under-prepared for this,"
            f"what with only having a tiny {weapon}."
        )
    answer = answer_this("Would you like to (1) fight or (2) run away?\n")
    while not check_valid(answer, ["1", "2"]):
        answer = answer_this("(Please enter 1 or 2).\n")
    if answer == "1":
        fight()
    else:  # when answer='2'
        run_away()


# the Scenario of fight with 2 options, based on the weapon you have
def fight():
    # global super
    if not super:
        print_slowly("You do your best...")
        print_slowly(f"but your {weapon} is no match for the {enemy}.")
        printl_slowly("You have been defeated!")
    else:
        # you have a SUPER WEAPON
        print_slowly(f"As the {enemy} moves to attack,"
                     " you unsheath your new sword.")
        print_slowly(
            "The Sword of Ogoroth shines "
            "brightly in your hand as you brace"
            " yourself for the attack."
        )
        print_slowly(
            f"But the {enemy} takes one look at"
            " your shiny new toy and runs away!"
        )
        printl_slowly("You have rid the town of the"
                      f" {enemy}. You are victorious!")


# the Scenario of running away
def run_away():
    printl_slowly(
        "You run back into the field. Luckily,"
        " you don't seem to have been followed."
    )
    field()


# the Scenario of going to the cave
def cave():
    global super
    if not super:
        print_slowly("You peer cautiously into the cave.")
        print_slowly("It turns out to be only a very small cave.")
        print_slowly("Your eye catches a glint of metal behind a rock.")
        print_slowly("You have found the magical Sword of Ogoroth!")
        super = True
        print_slowly("You discard your silly old "
                     f"{weapon} and take the sword with you.")
        printl_slowly("You walk back out to the field.")
    else:
        print_slowly("You peer cautiously into the cave.")
        print_slowly(
            "You've been here before, and gotten all the"
            " good stuff. It's just an empty cave now."
        )
        printl_slowly("You walk back out to the field.")


# asks if you want to play again or not
def play_again():
    global running
    valid = False
    answer = answer_this("Do you want to play again? y/n\n")
    while not valid:
        valid = check_valid(answer, ["y", "n"])
        if valid:
            if answer == "y":
                new_page()
                print("Game restarting...")
                lines(4)
            else:  # when answer='n'
                running = False
        else:
            answer = answer_this("please enter 'y' or 'n'.\n")


# THE GAME MAIN PROCCESS
running = True
while running:
    cave_state = False
    super = False
    enemy = random.choice(enemies)
    weapon = random.choice(weapons)
    new_page()
    intro_story()
    field()
    play_again()
lines(3)
printl_slowly("OK. Game Ends. Goodbye")
lines(3)
