# CRIAR UM PROGRAMA QUE MOSTRE OS 10 PRIMEIROS COLOCADOS DO BRASILEIRÃO NA ORDEM DE COLOCAÇÃO E DEPOIS,
# MOSTRE OS 5 PRIMEIROS TIMES
# OS 4 ÚLTIMOS COLOCADOS
# TIMES EM ORDEM ALFABÉTICA
# EM QUE POSIÇÃO ESTÁ O CUIABÁ

times = ('FLAMENGO', 'BAHIA', 'BOTAFOGO', 'SÃO PAULO', 'ATHLÉTICO PR', 'BRAGANTINO', 'PALMEIRAS',
         'INTERNACIONAL', 'CRUZEIRO', 'ATLÉTICO MG')

print(f'os times do brasileirão são: {times}')
print('-'*115)

print(f'os 5 primeiros times são: {times[0:4]}')
print('-'*115)

print(f'os 4 últimos colocados são: {times[-4:] }')
print('-'*115)

print('os times em ordem alfabética são {0}'.format(sorted(times)))
print('-'*115)


# USAR ASPAS DUPLA DENTRO DO F STRING QUANDO FOR ACESSAR UM ITEM QUE TAMBÉM É UMA STRING
print(f'o Flamengo está na posição {times.index("FLAMENGO")+1}.')
