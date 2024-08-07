# Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
#  que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.


def maior_valor(* valores):
    print(type(valores))
    maior = 0
    qtd_num = len(valores)

    for valor in valores:

        if valor > maior:
            maior = valor

    print(f'Foram informados {qtd_num} valores e o maior deles foi {maior}')


maior_valor(2, 3, 4, 6)
maior_valor(2, 8, 9, 40)
maior_valor(11, 536, 54, 89)
