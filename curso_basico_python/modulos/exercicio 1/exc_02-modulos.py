# Exercício Python 108: Adapte o código do desafio #107
# criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moeda_v2 as moeda


preco = float(input('Digite um preço: R$'))
metade = moeda.metade(preco)
dobro = moeda.dobro(preco)
aumento = moeda.aumentar(preco, 10)
diminuicao = moeda.diminuir(preco, 10)

print(f'A METADE DO VALOR {moeda.moeda(preco)} é {moeda.moeda(metade)}.')
print(f'O DOBRO DO VALOR {moeda.moeda(preco)} é {
      moeda.moeda(moeda.dobro(preco))}.')
print(f'AUMENTO 10% DO VALOR {moeda.moeda(
    preco)} TEMOS {moeda.moeda(aumento)}.')
print(f'DIMINUINDO 10% DO VALOR {moeda.moeda(
    preco)} TEMOS {moeda.moeda(diminuicao)}.')

