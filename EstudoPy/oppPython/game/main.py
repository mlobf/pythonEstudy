from player import Player

"""
    getter is an method used to get the value of a date atribute.
    setter is just a method used to set the value of the class data atribute
"""
tim = Player("Tim")

print(tim.name)
print(tim.lives)

tim.lives -= 1

print(tim)

tim.lives -= 1

print(tim)


tim.lives -= 1

print(tim)


tim.lives -= 1

print(tim)

tim.level = 2
print(tim)


tim.level += 5
print(tim)

tim.level = 3

print(tim)
