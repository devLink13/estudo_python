"""
Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


#ALGORITMO

1. LER VÁRIOS NÚMEROS PELO TECLADOS, *QUANTOS FOREM INSERIDOS* OK
2. PARAR DE LER AS ENTRADAS QUANDO FOR DIGITADO 999
3. MOSTRAR QUANTOS NÚMEROS FORAM DIGITADOS
4. QUAL A SOMA DOS NÚMEROS DESCONSIDERANDO A FLAG 999


"""

# variavel condicional de laço while principal
cond_laco = True

# variavel de contagem de numeros e variavel acumuladora dos valores digitados
cont_num = 0
acumulador_num = 0


while cond_laco:
    num = int(input('digite um número inteiro: [999 para terminar] '))
    cont_num += 1
    acumulador_num = acumulador_num + num
    # print(cont_num, acumulador_num)

    # verifica se o valor 999 de parada foi digitado, caso tenha sido. parar o programa.
    if num == 999:
        # varivel condicional de laço vai para falso e laço acaba
        cond_laco = False
        # retira 999 na contagem do acumulador para que seja desconsiderado a flag na soma
        acumulador_num = acumulador_num - 999
        # retira 1 na contagem para que seja desconsiderada a flag
        cont_num = cont_num - 1

print('\033[2;35mVOCÊ DIGITOU {} NUMEROS E A SOMA DESTES FOI {}.\033[m'.format(
    cont_num, acumulador_num))
