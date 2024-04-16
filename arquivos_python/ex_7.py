# realizar o sorteio de um nome ou número de uma lista

# import random
# necessito das funções random.shuffle e random.choice
from random import shuffle, choice

nome1 = str(input('digite um nome: '))
nome2 = str(input('digite um nome: '))
nome3 = str(input('digite um nome: '))
nome4 = str(input('digite um nome: '))
nome5 = str(input('digite um nome: '))
lista = [nome1, nome2, nome3, nome4, nome5]
print(lista)
# print("o sorteado foi {}".format(choice(lista)))


shuffle(lista)
print('a nova ordem sorteada agora é {}'.format(lista))
