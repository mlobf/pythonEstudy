# Revisao de python por Ze Portillha


def soma(x, y):
    return x + y


print(soma(4, 6))

multiplicacao = lambda x, y: x * y


print(multiplicacao(3, 5))

# list comprehension


sequence = [1, 3, 5, 6, 7, 2, 3]


dobro = [x * 2 for x in sequence]

print(dobro)


def double(x):
    return x * 2


# Usar o list comprehension sempre que possivel
print(map(double, sequence))

