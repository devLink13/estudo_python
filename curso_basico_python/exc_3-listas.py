# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

# NÃO CONSEGUI FAZER SOZINHO, ABAIXO SERÁ A RESOLUÇÃO DO GUANABARA


lista = list()

for c in range(0, 5):
    valor = int(input('digite um valor: '))

    # se for a primeira iteração atribua o valor a lista
    if c == 0:
        lista.append(valor)
        print(f'inserindo no inicio da lista')

    # se o valor digitado for maior que o maior valor da lista, atribua novo valor ao fim da lista
    elif valor > lista[len(lista)-1]:
        lista.append(valor)
        print('inserindo no fim da lista, pois é o maior valor atual')

    # algoritmo para saber em qual posição deve ser inserido
    # precisamos varrer toda a lista
    else:
        # variável de controle de laço
        pos = 0

        # laço de varredura, verificando onde há um número maior ou igual
        while pos <= len(lista):

            # verifica em qual posição há um número maior que o valor digitado
            if valor <= lista[pos]:

                # quando achar um número maior, coloca o valor digitado na posição dele e empurra o mesmo para a direita
                lista.insert(pos, valor)
                print(f'inserindo na posição {pos}...')

                # quando achar o número e inserir pode dar um break para sair do while, pois já foi feita a operação de inserção.
                break

            # acumulador de laço
            pos = pos + 1

print(lista)
