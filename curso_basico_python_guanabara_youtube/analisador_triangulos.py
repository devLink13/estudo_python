 # criar um projeto que analise todosos dados de um triângulo

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


4. quando se sabe as medidas de to
dos lados de um triângulo, pode ser usada a fórmula de héron para calcular
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

condicao_global: None  # criando uma variável global sem atribuir valor
# condicao_global = bool poderia ser assim também

# variavel global para armazenar o valor do tipo do triangulo, aceita 'equilatero' 'isoceles' ou 'escaleno'
tipo_triangulo = str
# print(type(tipo_triangulo))

if a < (b+c) and b < (a+c) and c < (a+b):
    print(
        '\033[2;32mOs segmentos inseridos formam um triângulo, vamos continuar!\033[m')
    condicao_global = True

else:
    condicao_global = False
    print(
        '\033[2;31mOs segmentos inseridos não formam um triângulo. Encerrando o programa!\033[m')


if condicao_global == True:
    # print('deu certo')

    # testes para saber qual triângulo é
    if a == b and b == c and a == c:
        tipo_triangulo = 'equilátero'
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        tipo_triangulo = 'isóceles'
    elif a != b != c:
        tipo_triangulo = 'escaleno'

    # calculos matemáticos
    # calculo do perímetro e semi perímetro
    per = a+b+c
    sp = per/2

    # formula de heron
    Area = sqrt(sp*(sp-a)*(sp-b)*(sp-c))
    # formatação para 'fstring' para printar 'A' com duas casas decimais. o f é de float
    # print(f'{A:.2f}')

    # formatação dos dados no terminal para exibição

    print('''********* DADOS DO TRIÂNGULO INSERIDO **************
* 1. SEGMENTOS INSERIDOS: {0:.>15.2f}, {1:.2f} e {2:.2f}
* 2. TIPO DE TRIÂNGULO: {3:.>28}
* 3. PERÍMETRO DO TRIÂNGULO: {4:.>23.2f}
* 4. ÁREA DO TRIÂNGULO: {5:.>28.2f} '''.format(a, b, c, tipo_triangulo.upper(), per, Area))
