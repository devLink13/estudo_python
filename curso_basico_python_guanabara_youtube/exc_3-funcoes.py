# Exercício Python 098: Faça um programa que tenha uma função chamada contador(),
#  que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

# a) de 1 até 10, de 1 em 1 --> ok
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    fim_ajustado = 0

    # encontrei dificuldade em testar as variaveis uma vez que usei if e depois elif para todas as condições
    # porém só podemos usar o elif (senão se:) para testar diferentes condições de uma mesma coisa
    # para coisas diferentes usar o if
    # analise o código abaixo com calma para perceber

    if inicio > fim and passo > 0:
        passo = passo * -1

    elif inicio > fim and passo < 0:
        passo = passo

    elif inicio < fim and passo > 0:
        passo = passo

    elif inicio < fim and passo < 0:
        passo = passo * -1

    # quando eu for analisar o passo usar if, uma vez que ele precisa ser analisado independentemente dos outros parâmetros
    if passo == 0:
        passo = 1
    
    # aqui podemos usar o elif pois há dois testes para fazer em cima do parâmetro fim
    if fim >= 0:
        fim_ajustado = fim + 1

    elif fim < 0:
        fim_ajustado = fim - 1

    print(fim_ajustado)
    print(f' -> A CONTAGEM PERSONALIZADA DE {inicio} ATÉ {
          fim} INDO DE {passo} EM {passo} FICOU ASSIM:')

    for c in range(inicio, fim_ajustado, passo):
        print(c, end=' ', flush=True)
        sleep(0.25)

        if c == fim:
            print('FIM!')


print(' -> CONTAGEM DE 1 ATÉ 10, INDO DE 1 EM 1:')
for c in range(1, 11):
    # precisamos definir o flush = True no print que possui um sleep logo após pois senão será criado um buffer e mostrado tudo no final.
    print(c, end=' ', flush=True)
    sleep(0.25)

    if c == 10:
        print('FIM!')

# teste sem o flush para entender melhor...
# for c in range(1, 11):
#     print(c, end=' ')
#     sleep(0.5)

#     if c == 10:
#         print('FIM!')

# contagem de 10 até 0 com passo de 2
print(' -> CONTAGEM DE 10 ATÉ 0 INDO DE 2 EM 2:')
for c in range(10, -1, -2):
    print(c, end=' ', flush=True)
    sleep(0.25)

    if c == 0:
        print('FIM!')

# inicio da interação com o usuário:

print('AGORA É SUA VEZ DE PERSONALIZAR A CONTAGEM: ')

inicio = int(input('DIGITE O N° INICIAL DA SUA CONTAGEM: '))
fim = int(input('DIGITE O N° FINAL DA SUA CONTAGEM: '))
passo = int(input('DIGITE O PASSO DA SUA CONTAGEM: '))

contador(inicio, fim, passo)
