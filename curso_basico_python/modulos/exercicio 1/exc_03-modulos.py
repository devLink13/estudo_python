# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

import moeda_v3 as moeda

preco = float(input('Digite um preço: R$'))

print(f'A METADE DO VALOR {moeda.moeda(preco)} é {moeda.metade(preco, True)}.')
print(f'O DOBRO DO VALOR {moeda.moeda(preco)} é {moeda.dobro(preco, True)}.')
print(f'AUMENTANDO 10% DO VALOR {preco} TEMOS {
      moeda.aumentar(preco, 10, True)}.')
print(f'DIMINUINDO 10% DO VALOR {moeda.moeda(preco)} TEMOS {
      moeda.diminuir(preco, 10)}.')
