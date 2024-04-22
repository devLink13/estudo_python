# exercicio 44
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
'''
– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros

'''

import random
import time

print('\033[1;34;47m{:#^50}\033[m'.format(' AUTO PEÇAS LINK '))
valor = random.randint(0, 10000)

print('O total do seu pedido foi\033[2;35m R${0}\033[m'.format(valor))

txt = 'metodos de pagamento:'
print('{0: ^50}'.format(txt.upper()))
print('Selecione seu método de pagamento:')
print('''[ 1 ] A VISTA DINHEIRO / CHEQUE (10% DE DESCONTO)
[ 2 ] A VISTA NO CARTÃO (5% DE DESCONTO)
[ 3 ] ATÉ 2X NO CARTÃO
[ 4 ] 3X OU MAIS NO CARTÃO (20% DE JUROS)''')

opcao = int(input())


if opcao == 1:
    print('Calculando...')
    time.sleep(1)
    valor2 = valor - (valor*0.10)
    print('O VALOR DE R${0} COM O DESCONTO FICA EM R${1}.'.format(
        valor, valor2))
elif opcao == 2:
    print('Calculando...')
    time.sleep(1)
    valor2 = valor - (valor*0.05)
    print('O VALOR DE R${0} COM O DESCONTO FICA EM R${1}.'.format(
        valor, valor2))
elif opcao == 3:
    parcelas = 2
    print('Calculando...')
    time.sleep(1)
    parcelas = valor / parcelas
    valor2 = valor
    print('O VALOR DE R${0} EM 2X DE R${2} FICA EM R${1}.'.format(
        valor, valor2, parcelas))
elif opcao == 4:
    parcelas = int(input('em quantas parcelas? '))
    print('Calculando...')
    time.sleep(1)
    valor2 = valor*1.2
    valor3 = valor2 / parcelas
    print('O VALOR DE R${0} EM {1}x GERA UMA PARCELA DE R${2:.2f} E UM TOTAL DE R${3:.2f}.'.format(
        valor, parcelas, valor3, valor2))
