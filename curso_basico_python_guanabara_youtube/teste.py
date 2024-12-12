# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

lista_geral = list()
estatistica = dict()
gols = list()
total = 0

while True:

    estatistica['nome'] = str(input('NOME: '))
    estatistica['n_partidas'] = int(input('N° PARTIDAS: '))

    if estatistica['n_partidas'] > 0:
        for c in range(0, estatistica['n_partidas']):
            gols.append(int(input(f'N° DE GOLS NA PARTIDA {c+1}: ')))
    elif estatistica['n_partidas'] == 0:
        estatistica['n_gols'] = 0
        estatistica['tot_gols'] = 0
        
    estatistica['n_gols'] = gols
    estatistica['tot_gols'] = sum(gols)

    lista_geral.append(estatistica.copy())

    if input('CONTINUAR? [S/N]') in 'nN':
        break

print(lista_geral)
