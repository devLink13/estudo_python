# Escreva um programa que leia uma lista de números inteiros do usuário e exiba a soma de todos os números ímpares na lista.

lista = list()
soma = 0

# solicito a entrada de dados na forma de lista
lista = input('digite uma lista separando um elemento de outro usando ",": ')
# separo a lista a cada encontro de ','
lista = lista.split(',')
# print(lista)

# converto cada elemento da lista de str para int
for i, item in enumerate(lista):
    lista[i] = int(item)

    # após a conversão do item, verifico se ele é impar, se for, eu já acumulo ele na variavel soma
    if (lista[i] % 2) != 0:
        soma = soma + lista[i]

print(soma)
