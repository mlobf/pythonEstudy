
parrot ="Norwegian Blue" 


print(parrot[0:6:2])

print(parrot[0:6:3])

#Usando estes separadores para realizar demarcações na string

number = "9,123;372:036 854,775;807"

seperators = number[1::4]

print(seperators)


#Ai vai a encrenca


values = "".join(char if char not in seperators else " " for char in number).split()

print([int (val)for val in values])









