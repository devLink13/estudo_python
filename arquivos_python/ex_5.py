# separar partes de um número, inteira e decimal usando biblioteca .math
from math import modf
num = float(input('digite um número: '))
print(modf(num))  # printa forma como a função retorna o valor
# aplica a função em duas variváveis
num1, num2 = modf(num)
print('a parte inteira do número digitado foi {} e a parte decimal foi {:.2f}'.format(
    int(num2), num1))
