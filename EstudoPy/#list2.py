#list.py
parrot_list = ["non pinpinpin", "no more","a stiff", "bererth of live" ] 
parrot_list.append("brazilian blue")

for state in parrot_list:
    print("this parrot is a " + state)


even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]

for number_set in numbers:
    print(number_set)

    for value in number_set:
        print(value)
