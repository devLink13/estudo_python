"""
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


ex.:
    sacar 100,00 --> 100/50 = 2
    2 x 50



    sacar 130,00 --> 130 / 50 = 2
                 --> 130 - (50x2) = 30
                 --> 30 / 20 = 1
                 --> 30 - (20x1) = 10
                 --> 10 / 10 = 1

    2 x 50 = 100
    1 x 20 = 20
    1 x 10 = 10
           = 130


    150/100 -> 1  150-(100*1) = 50
    50/20 -> 2    50-(20*2) = 10
    10/10 -> 1    10-(10*1) = 0


"""


notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_1 = 0

while True:
    sacar = int(input('DIGITE UM VALOR PARA SAQUE: '))

    while True:

        if sacar >= 50:
            notas_50 = sacar // 50
            sacar = sacar - (50*notas_50)
            print(sacar)

        if sacar >= 20:
            notas_20 = sacar // 20
            sacar = sacar - (20*notas_20)
            print(sacar)

        if sacar >= 10:
            notas_10 = sacar // 10
            sacar = sacar - (10*notas_10)
            print(sacar)

        if sacar >= 1:
            notas_1 = sacar // 1
            sacar = sacar - (1*notas_1)
            print(sacar)

        if sacar == 0:
            break

    print(f'TOTAL DE {notas_50} CÉDULAS DE R$50.')
    print(f'TOTAL DE {notas_20} CÉDULAS DE R$20.')
    print(f'TOTAL DE {notas_10} CÉDULAS DE R$10.')
    print(f'TOTAL DE {notas_1} CÉDULAS DE R$1.')
        
    if input('CONTINUAR SAQUE? [S - SIM /  N - NÃO]').upper() == 'NÃO':
        break

