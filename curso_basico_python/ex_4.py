# realizar a quebra de um número, em sua parte inteira
# usando biblioteca inteira, uma parte dela ou então sem usá-la

"""import math

# usando a biblioteca math inteira
num = float(input("digite um n°: "))
print("o número digitado foi {} e sua parte inteira é {}".format(
    num, math.trunc(num)))
"""

# importando apenas trunc

'''
from math import trunc
num = float(input("digite um número: "))
print("o número digitado foi {} e sua parte inteira é {}".format(num, trunc(num)))
'''

# sem usar biblioteca
num = float(input('digite um número: '))
# int(variável) forçamos o número a ser convertido para o tipo descrito
print('o número digitado foi {} e sua parte inteira é {}'.format(num, int(num)))
num = num-int(num)
print('a parte decimal é {:.2f}'.format(num))
