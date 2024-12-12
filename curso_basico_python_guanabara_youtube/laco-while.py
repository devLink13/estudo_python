# apredendo a usar o while com phyton

# exercicio 1:
'''
Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.

# Solicitar o sexo da pessoa, usar tratamento de strings
sexo = str(input('\033[2;35mDigite seu sexo: [M/F] \033[m')).upper().strip()
while sexo not in 'MF':
    print('\033[2;31mDADO INSERIDO DE FORMA INCORRETA!\033[m')
    sexo = str(
        input('\033[2;35mDigite seu sexo: [M/F] \033[m')).upper().strip()
    print(sexo)
print('dados ok')

'''

# exercicio 2:
'''
Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

'''
# para sortear um numero devemos incluir a biblioteca random

# sorteia um numero entre 0 e 10
import random
numero_sorteado = random.randrange(0, 11)
# solita a primeira entrada
numero_digitado = int(input('\033[2;35mDIGITE UM NÚMERO ENTRE 0 E 10: \033[m'))

# inicia o contador de tentativas
tentativa = 0

# avaliar para ver se eu acertei de primeira
if numero_digitado == numero_sorteado:
    print('\033[2;32mVOCÊ VENCEU DE PRIMEIRA!!\033[m')
    print('o número digitado foi {0} e o número sorteado pelo computador foi {1}'.format(
        numero_digitado, numero_sorteado))
# se eu não acertei de primeira, então continuar tentando até acertar
else:
    print('\033[2;31mVOCÊ NÃO ACERTOU DE PRIMEIRA!\033[m')
    while numero_digitado != numero_sorteado:
        tentativa = tentativa + 1
        print('\033[2;35mUSUÁRIO: {0}\033[m'.format(numero_digitado))
        print('\033[2;31mCOMPUTADOR: {0}\033[m'.format(numero_sorteado))
        numero_sorteado = random.randrange(0, 11)
        numero_digitado = int(input('digite um numero entre 0 e 10: '))

print('\033[2;32mVOCÊ VENCEU, O COMPUTADOR ESCOLHEU {0} E VOCÊ DIGITOU {1}, FORAM NECESSÁRIAS {2} TENTATIVAS PARA VENCER!\033[m'.format(
    numero_sorteado, numero_digitado, tentativa))
