# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

dados = dict()

dados['nome'] = str(input('Nome do Trabalhador: '))

ano_nasc = int(input('Ano de nascimento do trabalhador: '))
dados['idade'] = datetime.now().year - ano_nasc

dados['ctps'] = int(input('N° da Carteira de Trabalho (0 para não ter): '))

if dados['ctps'] == 0:
    for k, v in dados.items():
        print(f'{k} tem valor {v}')
else:
    dados['ano_cont'] = int(input('Digite o ano de contratação: '))
    dados['salario'] = float(input('Valor do salário: '))

    dados['ano_apos'] = dados['ano_cont'] + 35
    dados['idade_apos'] = (dados['ano_apos'] -
                           datetime.now().year) + dados['idade']

    for k, v in dados.items():
        print(f' -{k} tem valor {v}')
