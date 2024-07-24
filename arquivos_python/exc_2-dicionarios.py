# Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

# importar uma biblioteca para sortear numeros inteiros aleatórios
import random
# importar o sleep para uso de delay
from time import sleep
# importar uma função para iterar sobre o dicionário
from operator import itemgetter

numeros = dict()
numeros_ordenados = dict()
maior_valor = int

for c in range(0, 4):
    num_sorteado = random.randint(1, 6)
    numeros[f'jogador_{c+1}'] = num_sorteado

for k, v in numeros.items():
    print(f'O {k} tirou o número {v} no dado.')
    sleep(1)

# usar um ooutro dicionário para ordenar o em ordem descrescente, usando a função itemgetter(1) é possível aplicar o sorted nos values, que
# correspondem a key = 1
# OBS IMPORTANTE: A FUNÇÃO SORTED IRÁ RETORNAR UMA LISTA DE TUPLAS, TRATAR A PARTIR DE AGORA COMO LISTA E NÃO COMO DICIONÁRIO
numeros_ordenados = sorted(numeros.items(), key=itemgetter(1), reverse=True)

# print do ganhador
print(f'O GANHADOR FOI {numeros_ordenados[0][0]} que tirou o número {
      numeros_ordenados[0][1]} no dado')

# print do ranking
# aqui podemos usar o enumerate pois estamos falando de uma lista
print('=-'*25)
for i, v in enumerate(numeros_ordenados):
    print(f'{i}° lugar: {v[0]} que tirou {v[1]} no dado.')

print(numeros_ordenados)
