#criar um projeto que analise todosos dados de um triângulo

"""

1. solicitar 3 entradas, verificar se os três segmentos de reta podem gerar um triângulo.
    se puder continua o código
    se não puderem então para o código.

    condição de existência de um triângulo: a < b+c and b < a+c and c < b+a
    "a soma de dois lados é sempre menor que o terceiro lado."

2. analise qual tipo de triângulo será formado, seguindo o seguinte critério:
    – EQUILÁTERO: todos os lados iguais

    – ISÓSCELES: dois lados iguais, um diferente

    – ESCALENO: todos os lados diferentes    

3. entregar ao usuário todos os resultados referentes à geometria do triângulo.
    - calculo de área
    - caclulo de perímetro


4. quando se sabe as medidas de todos lados de um triângulo, pode ser usada a fórmula de héron para calcular
a área do triângulo, seja ele qual for.
    formula de heron: A = sqrt (p(p-a)(p-b)(p-c))
                        p = (a+b+c)/2 (semi perímetro)




"""


from math import sqrt

print('\033[1;35mOlá, bem vindo ao analisador de triângulos.\033[m')
print('\033[7m=-\033[m'*25)

a = float(input('digite o primeiro lado: '))
b = float(input('digite o segundo lado: '))
c = float(input('digite o terceiro lado:'))

condicao_global : None #criando uma variável global sem atribuir valor
# condicao_global = bool poderia ser assim também

if a < (b+c) and b < (a+c) and c < (a+b):
    print('\033[2;32mOs segmentos {0:.2f}, {1:.2f} e {2:.2f} formam um triângulo, vamos continuar!\033[m'.format(a,b,c))
    condicao_global = True

else:
    condicao_global = False
    print('\033[2;31mOs segmentos {0:.2f}, {1:.2f} e {2:.2f} não formam um triângulo. Encerrando o programa!\033[m'.format(a,b,c))


if condicao_global == True:
    print('deu certo')





