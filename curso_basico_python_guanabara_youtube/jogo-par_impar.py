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

impar_par = 'PAR'

while True:

    escolha_jogador = input(
        'ESCOLHA IMPAR OU PAR [1- IMPAR / 2 - PAR / SAIR - PARA PARAR]: ').upper()

    if escolha_jogador == 'SAIR':
        break

    while True:
        if escolha_jogador == '1' or escolha_jogador == '2':
            break
        else:
            escolha_jogador = input(
                'ESCOLHA UMA OPÇÃO VÁLIDA, DIGITE [1 - IMPAR / 2 - PAR]: ')

    num_jogador = input('DIGITE UM NÚMERO ENTRE 0 E 5: ')

    while True:
        if int(num_jogador) in range(0, 6):
            break
        else:
            num_jogador = input(
                'NUMERO INVÁLIDO, VOCÊ DEVE DIGITAR UM NÚMERO ENTRE 0 E 5: ')

    num_pc = random.randint(0, 5)
    soma = int(num_jogador) + num_pc

    if (soma % 2) == 0:
        impar_par = 'PAR'
    elif (soma % 2) != 0:
        impar_par = 'IMPAR'

    if escolha_jogador == '2' and (soma % 2) == 0:
        print(f'O JOGADOR ESCOLHEU {num_jogador} E O COMPUTADOR ESCOLHEU {
              num_pc}, A SOMA FOI {soma} QUE É {impar_par}. O JOGADOR VENCEU!')
    elif escolha_jogador == '1' and (soma % 2) != 0:
        print(f'O JOGADOR ESCOLHEU {num_jogador} E O COMPUTADOR ESCOLHEU {
              num_pc}, A SOMA FOI {soma} QUE É {impar_par}. O JOGADOR VENCEU!')
    else:
        print(f'O JOGADOR ESCOLHEU {num_jogador} E O COMPUTADOR ESCOLHEU {
              num_pc}, A SOMA FOI {soma} QUE É {impar_par}. O COMPUTADOR VENCEU!')
