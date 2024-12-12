"""
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

5! = 5x4x3x2x1
5! = 120

"""

# 1.  fazer com for
# 2.  fazer com while

"""resultado = 1
num = int(input('digite um número para calculo de fatorial: '))

for c in range(1, num+1):
    resultado = resultado * c
"""

"""fatorial = 1
num = int(input('digite um numero para calcular o fatorial: '))

for c in range(num, 0, -1):
    fatorial = fatorial * c
print(fatorial)"""

num = int(input('digite um numero para calculo do fatorial: '))
fat = 1

while num >= 1:

    fat = fat * num
    num = num - 1
    print(fat, num)
    
print(fat)
