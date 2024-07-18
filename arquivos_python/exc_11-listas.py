# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
#  e vai sortear 6 números entre 1 e 60 para cada jogo,
#  cadastrando tudo em uma lista composta.

import random
from time import sleep


num_jogos = int(input('QUANTOS JOGOS VOCÊ QUER GERAR? '))

cont = 1
while cont <= num_jogos:
    num_sorteado = random.sample(range(0, 61), 6)
    print(f'JOGO N° {cont}: {num_sorteado}')
    cont += 1

######################## FAZER OUTRA VERSÃO SEM USAR A FUNÇÃO SAMPLE QUE JÁ ENTREGA TUDO PRONTO ######################

########## USAR A FUNÇÃO RANDINT E TRATAR OS NÚMEROS REPETIDOS ####################


import random 
from time import sleep

num = int(input('QUANTOS JOGOS VOCÊ QUER GERAR? '))