# trabalhar com operações matemáticas em python

"""
operadores:

+   adição
-   subtração
*   multiplicação
**  exponenciação
/   divisão
//  divisão inteira
%   módulo da divisão 

"""
# pedir para inserir um número, mostrar o seu antecessor e o seu sucessor.
'''
num = int(input("insira um número inteiro: "))
num_suc = num+1
num_ant = num-1

print('o antecessor do número informado é {} \n e o sucessor do número informado é {}'.format(
    num_ant, num_suc),)

'''
# vamos realizar um calculadora usando todos os operadores
num1 = int(input('insira um número: '))
num2 = int(input('insira outro número: '))

som = num1+num2
sub = num1-num2
mult = num1*num2
exp = num1**num2
div = num1/num2
div_int = num1//num2
mod = num1 % num2

print(
    'CALCULADORA DOS NÚMEROS INFORMADOS \n 1. a soma entre os n° é {} \n 2. a subtração entre os n° é {}\n 3. a multiplicação entre os n° é {}\n 4. a exponenciação é {}\n 5. a divisão é {:.3f} '.format(som, sub, mult, exp, div))
