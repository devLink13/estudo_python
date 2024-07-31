# implementando uma pesquisa binária com python

# a ideia é desenvolver um algoritmo que faça busca de um elemento dentro de uma lista ordenada
'''
    1. Devemos ter um lista ordenada para que seja possível aplicar a busca binária
    2. Devemos conhecer o tamanho da lista.
    3. Devemos direcionar o próximo numero da busca para a metade da lista. Ou seja, o palpite sempre será a metade da lista atual.
'''
lista = [0, 3, 6, 9, 10, 15, 20, 30, 45, 50]
print(len(lista))

item = 3
metade_lista = int
inicio_lista = 0
fim_lista = len(lista)


cont = 1

while True:
    # calcula sempre a metade da lista atual com base nos valores de inicio e fim
    metade_lista = (fim_lista + inicio_lista) / 2
    metade_lista = int(metade_lista)

    # chuta o valor que está na metade da lista
    chute = lista[metade_lista]

    if chute == item:
        print(f'achei o valor {item} que é igual ao chute {
              chute} na {cont}° tentativa.')
        break

    # se o chute for muito alto, ou seja, se o chute for maior que o valor do item:
    # precisamos eliminar todos valores da metade pro final da lista, pois o chute já foi alto demais.
    elif chute > item:
        # o parâmetro de fim de lista receberá o valor da metade da lista - 1
        # lista = [0, 3, 6, 9, 10, x, x, x, x, x]
        # agora receberá o valor 4, pois metade_lista valia 5
        # a nova lista para analisar será lista = [0, 3, 6, 9, 10]
        fim_lista = metade_lista - 1
        cont += cont

    # se o chute for muito baixo, ou seja, o valor do chute for menor que o valor do item:
    # precisamos eliminar a metade para baixo da lista, pois o valor do chute já foi muito baixo.
    elif chute < item:

        # o inicio de lista receberá a metade da lista + 1, pois agora precisamos analisar os valores que estão após o meio
        # veja : lista = [x, x, x, x, x, x, 20, 30, 45, 50]
        # a lista que deveremos analisar agora será: lista = [20, 30, 45, 50]
        inicio_lista = metade_lista + 1
        cont += cont
