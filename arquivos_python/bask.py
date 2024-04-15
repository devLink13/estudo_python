# farei um programa para resolver bhaskara
'''
x = (-b +- sqrt(delta))/2*a
-b = b_1
sqrt(delta) =  raiz_delta

x1 = (b_1 + raiz_delta)/(2*a)
x2 = (b_1 - raiz_delta)/(2*a)


abstrair o problema:

1 uma entrada para b(fazer virar -b)
2 uma entrada para a
3 uma entrada para c
4 destrinchar o delta, delta pode ser escrito assim: d=b**2-4*a*c
5 calcular delta
6 tirar a raiz de delta sem usar o sqrt, como assim? ex.: sqrt 4 = 4**(1/2)
7 fazer as operações matemáticas
'''

# calculo das entradas
b = int(input('digite o valor de b: '))
b_1 = b*(-1)
# print(b, b_1)
a = int(input('digite o valor de a: '))
c = int(input('digite o valor de c: '))

# calculo do delta
delta = (b**2)-4*a*c
print(delta)

# tirar raiz quadrada do delta
raiz_delta = delta**(1/2)
# print(int(raiz_delta))

# operações matemáticas
x1 = (b_1 + raiz_delta)/(2*a)
x2 = (b_1 - raiz_delta)/(2*a)

# usar essa formatação permite definir o número com float sem casas decimais
print('o valor de x1 é {:.0f}\n e o valor de x2 é {:.0f}'.format(x1, x2))
