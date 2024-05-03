# Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


# ESTA É A VERSÃO DO GUANABARA

from random import randint

computador = randint(0, 10)
print(computador)

# variável de condição, iniciar como True para dar inicio ao while
acertou = True
# contador
tentativa = 0

while acertou:
    tentativa += 1
    jogador = int(input('qual é o seu palpite entre 0 e 10? '))
    if jogador > computador:
        print('digite um numero menor...')
    elif jogador < computador:
        print('digite um numero maior...')
    if jogador == computador:
        # mudar estado booleano para falso para parar o laço quando acertar
        acertou = False

print('acertou', tentativa)
