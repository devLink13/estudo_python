# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0):

    if nome.isalpha() and len(nome) > 0:
        nome_jogador = str(nome)
    else:
        nome_jogador = '<desconhecido>'

    if gols.isnumeric() and gols != '':
        n_gols = int(gols)
    else:
        n_gols = 0

    print(f'o jogador {nome_jogador} fez {n_gols} gols no campeonato.')


ficha(input('digite o nome do jogador: '), input(
    'digite o numero de gols do jogador: '))
