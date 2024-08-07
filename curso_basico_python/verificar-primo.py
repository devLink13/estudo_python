# construir um identificador de números primos.
'''

um numero primo só possui dois divisores: o número 1 e ele mesmo, ou seja POSSUI APENAS 2 DIVISÕES

-> algoritmo:
1. solicitar uma entrada inteira
2. verificar quantas divisões esse número pode fazer
    2.1 todo número é divisivel por 1
    2.2 verificar quantos divisores ele possui no intervalo entre 1 e ele mesmo
3. para cada divisor aumentar um no contador.
4. verificar se o contador possui mais de 2 divisores, se possuir, ele não é primo, se o contador for 2 exatamente, ele é primo.

    
exemoplo: numero 10
            10/2 = 5 (contar 1)
            10/5 = 2 (contar 1)
            10/10 = 1 (contar 1)

            contar = 3, então se contar for maior que 2, o número não é primo

'''

num = int(input('\033[2;35m DIGITE UM NUMERO: \033[m'))
contador = 0
for c in range(1, num + 1):
    # a cada iteração de c, no intervalo de contagens igual ao número inserido, verificar quantas divisões o número inserido pode fazer de forma exata.
    # ou seja, quantos divisores o número possui

    # verifica se o numero digitado é divisivel por cada um dos números começando de 1 e indo até ele.
    if (num % c) == 0:
        print('\033[2;32m', end='')  # muda a cor pra verde
        contador = contador + 1
        # print('contei +1')
    else:
        print('\033[2;31m', end='')  # muda a cor pra vermelho

    # printa sequencia toda usando cores.
    print('{}|'.format(c), end='')
print('')
# print(contador)


if contador == 2:
    print(
        '\033[2;32mNÚMERO {0} É CLASSIFICADO COMO UM NÚMERO PRIMO!\033[m'.format(num))
else:
    print('\033[2;31mNÚMERO {0} NÃO É CONSIDERADO PRIMO POIS POSSUI {1} DIVISORES\033[m'.format(
        num, contador))
