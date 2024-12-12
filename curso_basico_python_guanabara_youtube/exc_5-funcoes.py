# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#  A primeira função vai sortear 5 números e vai colocá-los dentro da lista
#  e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import random, randint

numeros = list()
numeros_pares = list()


def sortear(qtd):
    global numeros
    for c in range(0, qtd):
        num_aleatorio = random()*100
        numeros.append(int(num_aleatorio))
    print(numeros)


def soma_par(lista):
    soma = 0
    global numeros_pares

    for valor in lista:
        if valor % 2 == 0:
            numeros_pares.append(valor)
            soma += valor
            # soma = soma + valor

    # print('A SOMA ENTRE OS VALORES ', end='')
    # for valor in numeros_pares:
    #     print(valor, end=', ')
    # print(f'FOI DE {soma}')

    # posso printar desta forma ou então, da seguinte:

    # usando *numeros_pares, nós conseguimos desempacotar a lista e printá-la sem os conchetes
    # não é possível usar este método dentro de um f-string
    print('A SOMA ENTRE OS VALORES', *numeros_pares, f'É DE {soma}')


sortear(5)
soma_par(numeros)
