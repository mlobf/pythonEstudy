_low= 1
high = 1000

print("Think an number betwen {} to {}".format(_low
                                            , high))
input("Press enter to start ")

guesses = 1

while True:
    guess = _low + (high - _low) // 2
    high_low = input(
        "My guess is {}. Should I guess higher or lower? "
        "Enter h or l, or c to if my guess is correct ".format(guess)
    ).casefold()
    if high_low == "h":

        # Guess higher.

        _low = guess + 1
    elif high_low == "l":
        high = guess - 1  # Guess lower
    elif high_low == "c":
        print("I got in {} guesses !".format(guesses))
        break
    else:
        print("Ṕlease enter h, l or c")

    guesses += 1
