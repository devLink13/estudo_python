# Escreva um programa que crie um dataframe com informações de produtos e preços e, em seguida, calcule a média de preços dos produtos.
# Para criar o dataframe, você pode usar a função pandas.DataFrame() e passar um dicionário com as informações dos produtos e preços.
# Para calcular a média de preços, você pode usar o método pandas.DataFrame.mean().

import pandas as pd

dados = {
    'PESSOA1': {'NOME': 'ANA', 'IDADE': 23, 'CIDADE': 'SAO PAULO'},
    'PESSOA2': {'NOME': 'WESLEY', 'IDADE': 24, 'CIDADE': 'CAMPO GRANDE'}
}

print(dados['PESSOA1']['CIDADE'])

dt = pd.DataFrame(dados)
print(dt)
