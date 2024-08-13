# arquivo de teste do modulo moeda, este é o exc numero 1

import moeda

preco = float(input('Digite um preço: R$'))

print(f'A METADE DO VALOR {preco} é {moeda.metade(preco)}.')
print(f'O DOBRO DO VALOR {preco} é {moeda.dobro(preco)}.')
print(f'AUMENTO 10% DO VALOR {preco} TEMOS {moeda.aumentar(preco, 10)}.')
print(f'DIMINUINDO 10% DO VALOR {preco} TEMOS {moeda.diminuir(preco, 10)}.')
