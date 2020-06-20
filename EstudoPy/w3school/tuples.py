#tuples by w3shool

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple)



#Access tuple items
# = apple 
print(thistuple[1])


#Just testing key bindings

#Access tuple using negative index 
# = cherry
print(thistuple[-1])

#Print an range of tuples
# = 
print(thistuple[0:3])

#Print an negative range of tuples
# = "apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"
print(thistuple[-4:-1])

#Change value of an tuples.
#Tuples are unchangeable, or immutable sooo this is an  CHEAT 
#this is an example to "change" chery for kiwi
x = ("apple","banana","cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#Loop throught a tuple
# Using for
#
for x in thistuple:
    print(x)

#Check if this tuple exist
if "apple" in thistuple:
    print("Yes, we got apples")

#To see the tuple lenght
print(len(thistuple))

#Create tuple with ONE ITEM
thistupleOne = ("apple",)
print(type(thistupleOne))

thistupleTwo = ("apple")
print(type(thistupleTwo))

#You can remove itens of tuple. They are immutables
# But you can delete all tuple
#del(thistupleTwo)

# Join tuples 
thistupleTwo = ("apple",)
tuple3 = thistupleOne + thistupleTwo
print(tuple3)
print(type(tuple3))

# Tuple Constructor
thistuple = tuple(("apple","banana","cherry"))
print(thistuple)
#---------------------------------------------------
print("-"*80)
#---------------------------------------------------





















#---------------------------------------------------






