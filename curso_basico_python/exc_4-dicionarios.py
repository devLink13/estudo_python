# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

estatistica = dict()
gols = list()
total = 0

estatistica['nome'] = str(input('NOME: '))
estatistica['n_partidas'] = int(input('N° PARTIDAS: '))

for c in range(0, estatistica['n_partidas']):
    gols.append(int(input(f'N° DE GOLS NA PARTIDA {c+1}: ')))

estatistica['n_gols'] = gols

# é possível fazer desta forma para somar o total de valores de uma lista.
# for gol in gols:
#     total = total + gol

# estatistica['tot_gols'] = total

# ou então podemos usar a função sum para simplificar.
estatistica['tot_gols'] = sum(gols)


print(estatistica)
print('=-'*30)

for k, v in estatistica.items():
    print(f'  - O campo {k} tem valor {v}.')

print('=-'*30)

print(f'O jogador {estatistica["nome"]} jogou {estatistica["n_partidas"]} partidas no campeonato.')
for c in range(0, estatistica['n_partidas']):
    print(f'   -> Na partida {c+1}, fez {estatistica["n_gols"][c]} gols')
