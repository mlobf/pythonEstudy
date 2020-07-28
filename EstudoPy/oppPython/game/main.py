import player

"""
    getter is an method used to get value of date atribute.
    setter is just a method used to set the value of the class data atribute
"""
tim = player.Player("Tim")
print(tim.name)
print(tim.lives)

tim.lives = 9

print(tim)


tim._lives = 9
print(tim)
