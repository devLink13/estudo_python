# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados. ok
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = list()
impares = list()

soma_pares = 0
soma_coluna = 0

maior_valor = int

for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'digite um valor para [{l},{c}]: '))
        matriz[l][c] = num

        # verifica se é a iteração da 3° coluna e acumula
        if c == 2:
            soma_coluna = soma_coluna + num

        #  verifica se o número é par e o acumula  caso seja
        if num % 2 == 0:
            pares.append(num)
            soma_pares = soma_pares + num

        else:
            impares.append(num)

        # verifica se é a vez da segunda linha na iteração, se for compara o valor digitado com o maior valor
        if l == 1:
            # verifica se é a primeira iteração da segunda linha, se for então atribua o valor digitado ao maior valor para iniciá-lo
            if c == 0:
                maior_valor = matriz[l][c]

            # compara o valor digitado na segunda linha coluna x com o maior valor da mesma coluna
            if matriz[l][c] > maior_valor:
                maior_valor = matriz[l][c]

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^8}]', end='')
    print()


print(f'A SOMA DOS VALORES PARES DIGITADOS FOI: {soma_pares}')
print(f'A SOMA DOS VALORES DA TERCEIRA COLUNA É: {soma_coluna}')
print(f'O MAIOR VALOR DA SEGUNDA LINHA É: {maior_valor}')
