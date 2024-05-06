"""

Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


# ALGORITMO

1. LER VÁRIAS ENTRADAS NO TECLADOS OK
2. O PROGRAMA DEVE VERIFICAR SE O USUÁRIO DIGITOU 'FIM' PARA TERMINAR PROGRAMA OK
3. MOSTRAR A MÉDIA OK 
4. MOSTRAR MAIOR E MENOR VALOR LIDO. ok
5. USAR TRATAMENTO DE DADO PARA VERIFICAR SE O DADO INSERIDO FOI UM NUMERO OU ENTÃO O CODIGO DE PARADA 'FIM', SE NÃO FOREM ESTES DADOS ENTÃO SOLICITAR QUE REESCREVA O DADO




"""

# variavel condicional de laço while principal
cond_laco = True
cond_laco_verificacao = True

# variavel de contagem de numeros e variavel acumuladora dos valores digitados
cont_num = 0
acumulador_num = 0

# variavel de média, menor e maior valor, INICIAR AMBAS EM 0 e na primeira iteracão atribuir valor
media = 0.0
menor = 0
maior = 0

# variáveis de cores asc
vermelho = '\033[2;31m'
verde = '\033[2;32m'
magenta = '\033[2;35m'
fim_cor = '\033[m'


while cond_laco:
    # solicitar o dado, que pode ser um número ou o código de parada
    dado = input(
        'digite um número inteiro ou digite FIM para parar: ').upper().strip()

    cond_laco_verificacao = True
    while cond_laco_verificacao:
        # retira-se os pontos e os espaços das variáveis, retira o ponto decimal, atribui um campo sem espaço e faz no máximo uma alteração
        # isso é feito apenas na verificação para determinar se o dado vale 'FIM' ou então se ele é um número puro através do isdigit
        
        if dado == 'FIM' or dado.replace('.', '', 1).isdigit():
            print('dado valido', dado)
            cond_laco_verificacao = False
        else:
            # solicitar o dado, que pode ser um número ou o código de parada
            dado = input(
                f'{vermelho}INSERÇÃO INCORRETA, FORNEÇA DADO VALIDO!{fim_cor}: ')

    # verificação para término do programa
    # se for digitado fim, então acaba o programa, se não for: o programa continua normalmente
    if dado == 'FIM':
        print('fim')
        cond_laco = False
    # fluxo natural do programa
    else:
        # print(type(dado)) --> aqui o dado ainda é uma string, devemos convertê-lo para um flutuante
        # converter o dado para um número flutuante, dessa forma ele não será escrito como string
        dado = float(dado)
        # print(type(dado))

        # contador de numeros digitados
        cont_num += 1

        # aproveita o contador e verifica se é a primeira iteração do laço, isto é, o primeiro número digitado, se for, atribuir o menor valor e o maior valor ao numero digitado.
        if cont_num == 1:
            menor = dado
            maior = dado

        # acumula os valores digitados
        acumulador_num = acumulador_num + dado

        # verificação dos maiores e menores valores digitados
        if dado < menor:
            menor = dado
        elif dado > maior:
            maior = dado
media = acumulador_num / cont_num


print('VOCÊ DIGITOU {4}{0}{7} NUMEROS, A MÉDIA CALCULADA FOI {5}{1:.2f}{7}, O MENOR VALOR DIGITADO FOI {5}{2}{7} E O MAIOR VALOR FOI {6}{3}{7}.'.format(
    cont_num, media, menor, maior, magenta, verde, vermelho, fim_cor))
