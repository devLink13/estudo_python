#  Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
          'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    entrada = int(input('Digite um número entre 0 e 20: '))

    if entrada == -1:
        print('\033[33mENCERRANDO PROGRAMA \033[m')
        break

    if entrada >= 0 and entrada <= 20:
        print(f'o número digitado foi {numero[entrada]}')

    else:
        print('dado incorreto, digite novamente um número válido entre 0 e 20.')
