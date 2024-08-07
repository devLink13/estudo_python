'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.

'''

# criando variável de controle de laço
condicao_laco = True

# solicita duas entradas
num1 = int(input('digite um número: '))
num2 = int(input('digite outro número: '))


while condicao_laco:
    print('''MENU DE OPÇÕES:
            [ 1 ] somar
            [ 2 ] multiplicar
            [ 3 ] maior
            [ 4 ] novos números
            [ 5 ] sair do programa
                                ''')

    opcao = int(input('SELECIONE SUA OPÇÃO: '))

    if opcao == 1:
        print('a soma vale: ', num1+num2)
    elif opcao == 2:
        print('a multiplicação vale: ', num1*num2)
    elif opcao == 3:
        if num1 > num2:
            print('o primeiro número é maior que o segundo')
        elif num2 > num1:
            print('o segundo número é maior que o primeiro')
        else:
            print('os numeros são iguais.')
    elif opcao == 4:
        # solicita duas entradas
        num1 = int(input('digite um número: '))
        num2 = int(input('digite outro número: '))
    elif opcao == 5:
        print('saindo do programa, até mais!')
        condicao_laco = False
    else:
        print('opção inválida, digite novamente.')

print('finalizado')
