# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

# Ex:
# escreva('Olá, Mundo!')
# Saída:

# ~~~~~~~~~
#  Olá, Mundo!
# ~~~~~~~~~

def escreva(msg):
    # armazena em 'tam' a quantidade de caracteres que eu digitei e adiciona 4
    tam = len(msg) + 4

    # como 'tam' vale len(msg) + 4, eu sempre terei 4 espaços a mais que a mensagem passada
    # logo se eu der 2 espaços antes de printar o msg eu estarei sempre centralizando a mensagem
    print('-'*tam)
    print(f'  {msg}  ')
    print('-'*tam)


escreva('qualquer coisa que eu escreva')
