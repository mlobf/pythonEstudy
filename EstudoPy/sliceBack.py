#PythonCourse

#          5432109876543210987654321
#          0123456789012345678901234
letters = "abcdefghijklmnopqrstuvwxz"

#Não incluindo a primeira letras
#backwards = letters[26:0:-1]


# Dentro do [] temos tres campos, o 26 = inicio da contagem dos caracteres , 0 = é o final da contagem dos caracteres , -1 = Normalmente é a "passada"a ser percorrida e está é data em numero de caracteres, mas neste caso é apresentado na ordem apresentada é reversa.


#Incluindo a primeira letra
#backwards = letters[26::-1]

# O mesmo resultado pode ser apresentado da sequinte forma

#backwards = letters[::-1]

#print(backwards)

#Desafio
#Criar um slice que apresenta 'qpo'

backwards = letters[16:13:-1]
print(backwards)

#resolvido
#Desafio
#                             'edcba'
#                   apresenta os ultimos caracteres em ordem reversa
backwards = letters[4::-1]
print(backwards)
#Resolvido

#Produzir os 8 ultimos acateres em ordem reversa.
backwards = letters[:-9:-1]
print(backwards)


gato = '123456'



for x in gato:
    print("oi_mamae")
else:
    print(gato)

print("Eu disse para se falar de uma forma mais justa {0}".format)



idade = int(input("coloque a sua idade aqui "))

print(idade)

if idade > 65:
    print("vc vai morrer de corona virus se for a paulista")
else:
    print("Va e apanhe dos petistas")



