'''
Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.

'''

"""
1. solicitar dados:
    primeiro termo
    razão
2. imprimir os primeiros 10 termos.    

"""
# solicitar entradas
a1 = int(input('DIGITE O PRIMEIRO TERMO DA PA: '))
r = int(input('DIGITE A RAZÃO DA PA: '))

# iniciar variáveis

# contador de laço
cont = 0

# variavel de calculo
termo = a1

# variavel da quantidade de termos, iniciar com 10
qtd = 10
qtd_total = 0

# variavel de controle de laço
condicao = True


# calculo do enesimo termo, usar inicalmente a qtd, pois ela vale 10 e mostrará inicialmente os 10 primeiros termos da PA
enesimo = a1 + (qtd - 1)*r
print(enesimo)

# enquanto o contador for menor que a quantidade setada, o programa continua. Por padrão serão ao menos 10 irterações
while cont < qtd:
    print(termo, '--> ', end='')
    termo = termo + r
    cont += 1

    # verificar se a contagem já chegou na quantidade escolhida, lembrando que na primeira iteração serão inseridos 10 termos
    # após a primeira iteração a quantidade de termos dependerá do valor inserido pelo usuário quando
    # 1° --> qtd == 10? então pergunte quantos termos mais e some eles na quantidade total
    # 2° --> qtd == vai depender do usuário
    if cont == qtd:
        print('PAUSA')
        # solicita uma entrada para mostrar mais termos ou não, se digitar 0 acaba o programa
        num = int(
            input('Quantos termos mais precisam ser mostrados? para cancelar digite 0! '))
        qtd = qtd + num
        # verifica se o número digitado foi 0, zero acaba o programa
        if num == 0:
            print('FINALIZANDO PA, obrigado!')
            qtd_total = qtd
            qtd = 0

print('FIM. FORAM MOSTRADOS {0} TERMOS DA PA INFORMADA'.format(qtd_total))
