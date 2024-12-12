"""
sequencia de fibonacci: 0 , 1, 1, 2, 3, 5, 8 e por ai vai.... somar o ultimo termo com o seu antecessor e construir a partir dai

FAZER UM PRORGRAMA QUE MOSTRE A SEQUENCIA DE FIBONACCI DE UM DETERMINADO INTEIRO DIGITADO:

1. solicitar as entradas
    quantidade de termos da sequencia OK

2. executar os calculos lógicos
    0 - 1 - 1 - 2 - 3 - 5 - 8 - 13 -    
    t1  t2  t3                                  1° iteracao
        t1  t2  t3                              2°
            t1  t2  t3                          3°
                t1  t2  t3                      4°
                    t1  t2  t3                  5°

    fazer o calculo de tres em tres elementos

    ex: começando no quinto elemento
    t3 = t2 + t1
    t3 = 2  +  1
    t3 = 3

    para calcular o sexto elemento:

    t1 = t2
    t1 =  2

    t2 = t3
    t2 = 3
    
    t3 = t2 + t1
    t3 = 3  + 2
    t3 = 5




"""

termo = int(input('QUAL TERMO DA SEQUENCIA DE FIBONACCI VOCE QUER SABER? '))


# variavel de controle de laco, começar em dois para dar certo a procura do numero de fibonacci

cont = 2
t1 = 0
t2 = 1
t3 = 0
# print(t1, '-->', t2, '-->', end=' ')

while cont <= termo:
    t3 = t2 + t1
    # print(t3, '-->',  end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('O {0}° TERMO DA SEQUENCIA DE FIBONACCI É {1}.'.format(
    termo, t3,))
