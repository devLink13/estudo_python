# Exercício Python 104: Crie um programa que tenha a função leiaInt()
# que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n: ')


def valida_int(entrada):
    entrada = input(entrada)

    while True:

        entrada = entrada.strip()
        if entrada.isnumeric():
            return True
            break
        else:
            entrada = input('ERRO, digite um número válido: ')


def valida_str(entrada):
    entrada = input(entrada).strip()

    while True:
        if entrada.isalpha():
            return True
            break
        else:
            entrada = input('ERRO, digite um texto válido: ')
            return False


valida_int('digite um inteiro: ')
