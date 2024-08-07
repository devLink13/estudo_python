# criar uma tupla com valores e procurar eles a partir de uma entrada de usuário

from random import randint

numeros = tuple(randint(1, 10) for _ in range(10))
print(numeros)


while True:
    cond = str(input('você gostaria de fazer uma pesquisa na tupla? [y/n]'))
    if cond == 'y':
        num = int(input('qual número gostarias de pesquisar a posição?'))
        print(f'o número {num} está na posição {numeros.index(num)} da tupla.')
    elif cond == 'n':
        print('\033[34mENCERRANDO O PROGRAMA\033[m')
        break
