"""
1- Sortear 6 números de 1 a 60. Armazenar em uma lista.
2- Pedir para o usuario digitar  6 numeros. Armazenar em uma lista.
3- Checar se o usuario acertou 6, 5 ou 4 numeros.
4- Checar se o usuario acertou algum numero e informar os numeros sorteados.
"""
from random import randrange

numeros_sorteados = []
numeros_cliente = []


def sortiar_numeros():
    for x in range(6):
        numeros_sorteados.append(randrange(0, 60))
    print(numeros_sorteados)

for x in range(6):
    # new_number = input("Coloque o numero")
    if new_number in numeros_cliente:
        pass
        # print("escolha outro numero")

    # numeros_cliente.append(input("Coloque o numero"))

print(numeros_cliente)
