# Lesson 100, an intro for dicionaries an Python

fruit = {
    "orange": "a sweet , orange fruit",
    "apple": "good for making soda",
    "lemom": "a sour fruit, and yellow also",
    "grape": "fruit grown in buches",
    "lime": "its green fruit",
    "apple": "round and crunch",
}


#Print all elements on dicionaries
print(fruit)
#Print only lemom fruit
print(fruit["lemom"])
#Will add pear on Dictionary fruit
fruit["pear"] = "an odd shape apple"
#Print pear only
print(fruit["pear"])
#Delete lemom
del fruit["lemom"]
print(fruit)
#Try print the deleted lemom
#print(fruit["lemom"])
#For delete only the info on especific Dictionary and keep the dictionart in self,
#   is important use this.
fruit.clear()
print("Only below by now")
print(fruit)

# The funcion .get  allows retorn individuals elements on dictionaries and if that element does not exist,
#   the function retorn a NULL value
"""
while True:
    dict_key = input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    description = fruit.get(dict_key,"Sorry but dont have " + dict_key)
    print(description)
"""
#   if dict_key in fruit:
#       description = fruit.get(dict_key)
#       print(description)
#   else:
#       print("We dont have a" + dict_key)a

"""
x=1
while x < 100:
    for snack in fruit:
        print(fruit[snack])
    print("") 
    x += 1

for i in range(100):
    for snack in fruit:
        print(snack + " is " + fruit[snack])
    print('-' * 40)
"""

# print(fruit)

"""
orderd_key = list(fruit.keys())
orderd_key.sort()
"""
"""
orderd_key = sorted(list(fruit.keys()))
for i in orderd_key:
    print(f +"-" + fruit[f])
"""
# for f in sorted(fruit.keys()):
#    print(f + "-" + fruit[f])

# print("*"* 50)

# for val in fruit.values():
#    print(val)

# fruit_keys = fruit.keys()
# print(fruit_keys)

# fruit["tomato"] = "not nice ice cream"
# print(fruit_keys)

print(fruit)
print(fruit.items())

# Criar um tuple com uma funçao apartir do um dictionary

f_tuple = tuple(fruit.items())
print(f_tuple)
for snack in f_tuple:
    item, descripiton = snack
    print(item + " is " + descripiton)

print(dict(f_tuple))  # dictionary created from tuple


# There is a lot of interation between list, tuple and  dicionary
