# refazer o exercicio de pesaquisa binária para fixar o conhecimento e agora comparar ele com uma pesquisa simples

'''
    pesquisa binária: consiste em pesquisar sempre pela metade do valor total de itens da lista, eliminando metade dos valores a cada iteração.
        n° de etapas --> log_2 Nbuscas, exemplo: lista com 100 numeros, log_2 100 = 7 tentativas no máx.
    

    pesquisa simples: iterar valor por valor da lista até encontrar o valor de interesse.
        n° de etaás --> Nbuscas, exemplo: lista com 100 numeros, 100 tentativas no máximo caso o numero desejado esteja na ultima posição.


'''
import random


def busca_simples(lista, item_buscado):
    cont = 1

    for item in lista:

        if item == item_buscado:
            print(f'A lista possui tamanho de {len(lista)} e foram necessária {
                  cont} buscas para encontrar o valor {item_buscado}.')

        else:
            cont = cont + 1


def busca_binaria(lista, item_buscado):

    cont = 1
    inicio = 0
    final = len(lista)

    while True:
        metade = (final + inicio) / 2
        metade = int(metade)

        palpite = lista[metade]

        if palpite == item_buscado:
            print(f'A lista possui tamanho de {len(lista)} e foram necessária {
                  cont} buscas para encontrar o valor {item_buscado}.')
            break

        elif palpite > item_buscado:
            final = metade - 1
            cont += 1

        elif palpite < item_buscado:
            inicio = metade + 1
            cont += 1


def gerador_lista(n_itens):
    lista = list()

    for c in range(0, n_itens):
        num_aleat = random.random() * 100
        num_aleat = int(num_aleat)
        lista.append(num_aleat)

    lista.sort()
    return lista


lista = gerador_lista(5)

item = lista[0]

busca_simples(lista, item)
busca_binaria(lista, item)
