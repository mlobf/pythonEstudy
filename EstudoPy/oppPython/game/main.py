from player import Player
from enemy import Enemy

"""
    getter is an method used to get the value of a date atribute.
    setter is just a method used to set the value of the class data atribute
"""
tim = Player("Tim")

random_monster = Enemy("Basic Enemy", 12, 1)

print(random_monster)

random_monster.take_damage(4)

print(random_monster)
random_monster.take_damage(9)

print(random_monster)
random_monster.take_damage(4)

print(random_monster)