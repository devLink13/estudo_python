# implementação de um algoritmo de ordenação por seleção

"""
    neste tipo de algoritmos precisamos ordenar uma lista criando outra, ou seja
    precisamos percorrer n elementos de uma lista, testar e verificar um por um afim
    de identificar o maior e o menor, e então acrescentá-los a uma outra lista.

    cada iteração sobre essa lista leva um tempo O(n) e precisamos verificar essa lista
    n vezes, logo o tempo de execução deste algoritmo é O(n * n), logo o tempo é O(n²)

"""
# lista desordenada
arr = [0, 10, 4, 3, 5, 2]

# lista para receber a ordenação
novoArr = list()

# tamanho da lista ordenada
n = len(arr)

# implementação do livro "entendendo algoritmos um guia ilustrado..."


def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacaoporSelecao(arr):
    novoArr = []

    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr


print(arr)
print(ordenacaoporSelecao(arr))
