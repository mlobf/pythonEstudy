# Test of review code

"""
x= 1
y= 50

while x is not y:
    print("This is my life, its now or never {} and {}".format(x,y))
    x += 1
if x == y:
    print("We got an issue now, the winter is coming {} times".format(x))

"""

# Dictionary Comprehensions
# But First, list Comprehensions
# Below, a list with tuples

users = [
    (0, "Bob", "password"),
    (1, "Thomas", "1235"),
    (2, "John", "asdf"),
    (3, "Clara", "tadsf23j"),
    (4, "Jose", "lkjkiiwww2"),
    (5, "Marcos", "123454321"),
    (6, "Antonio", "lalilo"),
]

# Now we want create a mapping of usernames to user information.

username_mapping = {user[1]: user for user in users}

print(username_mapping)





