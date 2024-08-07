# Escreva um programa que crie uma lista de números inteiros aleatórios e, em seguida, imprima o maior e o menor número da lista.
# Para criar uma lista de números inteiros aleatórios, você pode usar a biblioteca random do Python.

import random

cont = 0
maior = int()
menor = int()
lista = list()

n_ele = int(input('quantos elementos você deseja que a lista tenha? '))

# laço para gerar n elementos, conforme solicitado
while cont < n_ele:
    num_aleat = int(random.random()*100)
    lista.append(num_aleat)
    cont += 1

# iteração sobre a lista para identificar o maior e o menor
for i, item in enumerate(lista):
    if i == 0:
        menor = item
        menor = item
    else:
        if item > maior:
            maior = item
        elif item < menor:
            menor = item
# posso fazer da maneira acim iterando na mão item por item, ou usar as funções max() e min ()
print(lista)
print(min(lista), max(lista))
print(menor, maior)
