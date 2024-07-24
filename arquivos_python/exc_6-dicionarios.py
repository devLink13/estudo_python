# Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

lista_geral = list()
estatistica = dict()
gols = list()
total = 0

while True:

    estatistica['nome'] = str(input('NOME: '))
    estatistica['n_partidas'] = int(input('N° PARTIDAS: '))

    for c in range(0, estatistica['n_partidas']):
        gols.append(int(input(f'N° DE GOLS NA PARTIDA {c+1}: ')))

    if estatistica['n_partidas'] == 0:
        estatistica['n_gols'] = 0
    else:
        estatistica['n_gols'] = gols[:]

    estatistica['tot_gols'] = sum(gols)

    lista_geral.append(estatistica.copy())
    gols.clear()

    if input('CONTINUAR? [S/N] ') in 'nN':
        break

print(lista_geral)

print(f'{"COD":<0}', f'{"NOME":<15}', f'{
      "N° PARTIDAS":<15}', f'{"GOLS":<15}', f'{"TOTAL":<15}')


print('-'*65)

# podemos usar o enumerate para iterar pois estamos iterando uma LISTA
# indice irá retornar o valor do contador, ou seja, o indice da lista
# posição irá retornar todos os valores do dicionário na posição do contador, ou seja, toda a posição 1 da lista que é o primeiro dicionário
# a partir dai podemos iterar sobre os pares chave-valor
for indice, posicao in enumerate(lista_geral):
    # printar primeiro o indice da lista geral
    print(f'{indice:<0}', end=' ')

    # iterar desta forma permite percorrer a lista toda sem abrir um outro contador
    # posição.values() irá retornar os valores em cada posição do dicionário
    # dado irá assumir o valor de cada chave
    for dado in posicao.values():
        # testa para ver se estamos na chave 'tot_gols', se estiver aplica formatação específica
        # se não tiver, aplica formatação geral
        if posicao.keys() == 'tot_gols':
            print(f'{str(dado):>15}', end='')
        else:
            print(f'{str(dado):<15}', end='')
    print()

print('-'*65)

while True:
    opc = int(input('MOSTRAR DADOS DETALHADOS DE QUAL JOGADOR?'))

    print(f'DADOS DETALHADOS DO JOGADOR {lista_geral[opc]['nome']}')

    for c in range(0, len(lista_geral[opc]['n_gols'])):
        print(
            f'  --> No jogo n° {c+1} fez {lista_geral[opc]['n_gols'][c]} gols.')
    print()

    if str(input('DESEJA CONTINUAR? [S/N] ')) in 'Nn':
        break

print(f'{"FIM":*^50}')
