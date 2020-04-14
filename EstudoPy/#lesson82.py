#lesson82.py
choice = "-"

while  choice != "0":
    if choice in "12345":
        print("you choose {}".format(choice))
    else:
        print("Ṕlease choose your option from the list below ")
        print("1: \t Learn Python")
        print("2:\t Learn Java")
        print("3:\t Go swiming")
        print("4:\t Have dinner")
        print("5:\t Go to bed")
        print("0:\t Exit")
    
    choice = input("")

