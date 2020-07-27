list = [1, 2, 3, 4, 5, 6, 8, 9, 10]

# list compreentions 1

x = [l * 2 for l in list]

print(x)

# list compreentions 2

y = [l - len(list) for l in list if l > 8]

print(y)

# list compreentions 3

y = [l - len(list) for l in list if l > 8 and l is not 10]

print(y)

#new_list = ['marcos','leme','oliveira','frattine','campanha']

#z = [for f in new_list print f]




