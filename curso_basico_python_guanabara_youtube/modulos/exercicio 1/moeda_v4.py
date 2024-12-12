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


def resume(num, aumento=0, diminuicao=0, format=False):
    print('-'*50)
    txt = f'RESUMO DO VALOR DIGITADO --> ' + f'{moeda(num)}'
    print(f'{txt:^50}')
    print('-'*50)

   # USAR O SEGUNDO COLCHETES DENTRO DA F-STRING PARA DELIMITAR A POSIÇÃO DO PRINT DO VALOR SOLICITADO
   # SEMPRE SERÁ O 50-LEN('TEXTO QUE EU DIGITAR AQUI'), isso fará com que o valor seja sempre ajustado à direita
    print(f'AUMENTO:', end='')
    print(f'{aumentar(num, aumento, format):>{50-len('AUMENTO:')}}')

    print(f'DIMINUICÃO:', end='')
    print(f'{diminuir(num, diminuicao, format):>{50-len('DIMINUIÇÃO:')}}')

    print(f'DOBRO:', end='')
    print(f'{dobro(num, format):>{50-len('DOBRO:')}}')

    print(f'METADE:', end='')
    print(f'{metade(num, format):>{50-len('METADE:')}}')


def moeda(num, moeda='R$'):
    formatacao = f'{moeda}{num:.2f}'.replace('.', ',')
    return formatacao
