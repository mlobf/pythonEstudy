    """Contar 
    """



list_of_ats = []

count = 0


mylist = [
    "@lall",
    "@kikik",
    "@sasaasa",
    "@fkjasf",
    "@sasaasa",
    "@kikik",
    "@fkjasf",
    "@kikik",
    "@sasaasa",
    "@fkjasf",
    "@sasaasa",
    "@kikik",
    "@fkjasf",
    "@fkjasf",
    "@fkjasf",
    "@fkjasf",
    "@sasaasa",
    "@fkjasf",
    "@lall",
    "@sasaasa",
    "@lall",
    "@kikik",
    "@sasaasa",
    "@sasaasa",
    "@sasaasa",
    "@sasaasa",
    "@lall",
    "@sasaasa",
    "@kikik",
    "@lall",
    "@kikik",
    "@lall",
    "@lall",
    "@kikik",
    "@lall",
    "@lall",
    "@kikik",
]

for element in mylist:
    # criar uma lista com os valores unicos
    if element in list_of_ats:
        print('ai ja esta o elemento')
    else:
        list_of_ats.append(element)
        print(list_of_ats)






print(count)

