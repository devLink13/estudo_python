# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta

'''
    matriz =  [ x   x   x ]
              [ x   x   x ]
              [ x   x   x ]  
'''

matriz = [[],[],[]]

cont = 0

# laço que garante a inserção das 3 linhas
while cont < 3:

    # inserção dos valores de cada coordenada da matriz 3x3
    for c in range(0, 3):
        num = int(input(f'digite um valor para {[cont, c]}: '))
        # na linha tal insira os valores para cada coordenada
        matriz[cont].insert(c, num)

        # confere se os 3 valores para a coluna já foram inseridos, se sim, acumula 1 ao contador.
        if c == 2:
            cont += 1

# estrutura de repetição para exibição de valores
for l in range(0, 3):

    for c in range(0, 3):
        print(f'[{matriz[l][c]:^6}]', end='')
    # após mostar 3 valores inserir um print para quebra de linha
    print()
