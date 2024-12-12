# fazer um programa que faça com que o computador gere um número aleatório entre 0 e 5
# e o usuário precisa advinhar, se acertar informa que venceu o computador, se errar o
# computador vence

from random import randint

# armazenar um n° aleatório entre 0 e 5
num_al = randint(0, 5)
print(num_al)

# pedir para o usuário digitar um inteiro entre 0 e 5
num_dig = int(input('digite um número entre 0 e 5: '))
print(num_dig)

if num_al == num_dig:
    print('você venceu!')
else:
    print('você perdeu!')
