# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

import moeda_v4 as moeda

preco = float(input('Digite um preço: R$'))

moeda.resume(preco, 10, 10, format=True)

lista = [100, 150, 200, 250]

for c in range(0, len(lista)):
    aumento = moeda.aumentar(lista[c], 50)
    print(aumento)
