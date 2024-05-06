"""
Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

ALGORITMO:

1. SELECIONAR UMA OPÇÃO A CADA RODADA, 1 - IMPAR OU 2 - PAR
2. A CADA VITÓRIA ACUMULAR 1 AO NUMERO DE VITORIAS
3. INTERROMPER O JOGO NA PRIMEIRA DERROTA
4. MOSTRAR O NUMERO DE VITORIAS



"""

# importar biblioteca random
import random
from time import sleep

escolha_pc = 0
num_pc = 0

numero_par = ['0', '2', '4']
numero_impar = ['1', '3', '5']

cont = 0

while True:

    cont += 1

    # SOLICITA A ENTRADA DE PAR OU IMPAR DO USUÁRIO
    escolha_usuario = input(
        'SELECIONE IMPAR OU PAR [1 - IMPAR / 2 - PAR / SAIR]: ').strip().upper()

    if escolha_usuario == 'SAIR':
        break

    # verificar se a escolha de impar ou par foi correta
    while True:
        if escolha_usuario == '1' or escolha_usuario == '2':
            # print('dado valido')
            break
        else:
            escolha_usuario = input(
                'DADO INVÁLIDO, POR FAVOR DIGITE 1 OU 2: ')

    if escolha_usuario == '1':
        # SOLICITA O NÚMERO ESCOLHIDO PELO USUÁRIO
        num_usuario = input('ESCOLHA UM NÚMERO IMPAR ENTRE 1 E 5: ')

        while True:
            if num_usuario in numero_impar:
                # print('digitou numero impar')
                break
            else:
                num_usuario = input(
                    'VOCÊ DEVE DIGITAR UM NÚMERO IMPAR, OPÇOES [1,3,5]: ')

    elif escolha_usuario == '2':
        # SOLICITA O NÚMERO ESCOLHIDO PELO USUÁRIO
        num_usuario = input('ESCOLHA UM NÚMERO PAR ENTRE 0 E 5: ')

        while True:
            if num_usuario in numero_par:
                # print('digitou numero par')
                break
            else:
                num_usuario = input(
                    'VOCÊ DEVE DIGITAR UM NÚMERO PAR, OPÇOES [0,2,4]: ')

    escolha_usuario = int(escolha_usuario)
    num_usuario = int(num_usuario)

    if escolha_usuario == 1:
        escolha_pc = 2
        num_pc = random.choice(numero_par)
        print(f'o pc escolheu {num_pc}')
    elif escolha_usuario == 2:
        escolha_pc = 1
        num_pc = random.choice(numero_impar)
        print(f'o pc escolheu {num_pc}')

# TERMINAR A LÓGICA DE APRESENTAÇÃO DO VENCEDOR
