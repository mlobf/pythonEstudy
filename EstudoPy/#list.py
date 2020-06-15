# list.py

"""

parrot_list = ["non popo", "no more", "a stiff","beret for life"]

parrot_list.append("Norweagian Blue")

for state in parrot_list:
    print("this parrot is " + state)

even = [2,4,6,8] 
ode = [1,3,5,7,9] 

numbers = even + ode 
numbers.sort()

numbers_in_order = sorted(numbers)

print(numbers_in_order)

if numbers == numbers_in_order:
    print("the lists are equal")
else:
    print("the lists are not equal")

if numbers_in_order == sorted(numbers):
    print("the list are iqual")
else:
    print("the list arent")

"""


list_1 = []
list_2 = list()

print("List 1: {}".format(list_1))
print("List 2: {}".format(list_2))

if list_1 == list_2:
    print("List are iqual")

print(list("the list are equal"))
