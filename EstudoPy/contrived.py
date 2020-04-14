#lesson76

numbers = [1, 45, 31, 16, 60]

for number in numbers:
    if number % 8 == 0:
        #reject the list
        print("The jumbers are unacceptble")
        break
else:
    print("Now all numbers are fine")
