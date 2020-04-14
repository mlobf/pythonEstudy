import random

available_exits = ["north", "south", "east", "west"]


chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")

    if chosen_exit.casefold() == "quit":
        print("GAME OVER")
        break
else:
    print("Are you glad to get out of here? ")

