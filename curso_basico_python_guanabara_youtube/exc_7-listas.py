# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas. ok
# B) Uma listagem com as pessoas mais pesadas. ok
# C) Uma listagem com as pessoas mais leves. ok

lista = list()
lista_temp = list()
maior_peso = menor_peso = 0
pessoa_maior = str
pessoa_menor = str
while True:

    lista_temp.append(str(input('digite um nome para inserção: ')))
    lista_temp.append(float(input('digite o peso da pessoa: ')))

    lista.append(lista_temp[:])
    lista_temp.clear()

    if maior_peso == 0 and menor_peso == 0:
        menor_peso = lista[0][1]
        maior_peso = lista[0][1]

    if input('deseja continuar? [s/n] ') in 'nN':
        break

for pos in lista:
    if pos[1] >= maior_peso:
        maior_peso = pos[1]
        pessoa_maior = pos[0]

    elif pos[1] <= menor_peso:
        menor_peso = pos[1]
        pessoa_menor = pos[0]


print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'a pessoa mais pesada é: {pessoa_maior}, com {maior_peso}kg.')
print(f'a pessoa mais leve é: {pessoa_menor}, com {menor_peso}kg.')
