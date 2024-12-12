# Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

# funções para o modulo moeda.py

def aumentar(num, aumento, format=False):
    aumento = (aumento/100) + 1
    num = num * aumento
    num = round(num, 2)

    if format is False:
        return num
    else:
        return moeda(num)


def diminuir(num, diminuicao, format=False):
    diminuicao = (diminuicao/100)*num
    num = num - diminuicao
    num = round(num, 2)

    if format is False:
        return num
    else:
        return moeda(num)


def dobro(num, format=False):
    num = num*2
    num = round(num, 2)

    if format is False:
        return num
    else:
        return moeda(num)


def metade(num, format=False):
    num = num/2
    num = round(num, 2)

    if format is False:
        return num
    else:
        return moeda(num)


def moeda(num, moeda='R$'):
    formatacao = f'{moeda}{num:.2f}'.replace('.', ',')
    return formatacao
