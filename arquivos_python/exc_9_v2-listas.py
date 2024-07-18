# FAREI AGORA A VERSÃO DO GUSTAVO GUANABARA PARA O EXERCÍCIO N° 9

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# primeiro faremos uma estrutura de repetição para a linha e depois para as colunas
# o método do guanabara consiste em aninhar os laços 'for'

# for da linha
for l in range(0, 3):
    # for da coluna
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite o valor para [{l},{c}]: '))
print(matriz)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^8}]', end='')
    print()
