# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

# o 'as' serve para dar um 'apelido' para a função
# 'dt' é o apelido dado
import datetime as dt


def voto(ano):
    ano_atual = dt.datetime.now().year
    ano_nasc = ano

    idade = ano_atual - ano_nasc

    if idade >= 70 or 18 > idade >= 16:
        return f'Com {idade} anos, o voto é opcional.'
    elif idade >= 18:
        return f'Com {idade} anos, o voto é obrigatório.'

    else:
        return f'Com {idade} anos o voto não é permitido.'


print(voto(2009))
