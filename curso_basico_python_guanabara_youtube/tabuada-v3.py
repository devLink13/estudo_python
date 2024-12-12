"""
Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
 O programa será interrompido quando o número solicitado for negativo. 


 ALGORITMO:

 1. SOLICITAR UMA ENTRADA PARA CALCULO DE SUA TABUADA
 2. CALCULAR SUA TABUADA E MOSTRAR O  SEU VALOR
 3. AO INDICAR NÚMERO NEGATIVO ENCERRA-SE O PROGRAMA

 
 """

while True:
    num = input('DIGITE O NÚMERO QUE VOCÊ DESEJA A TABUADA: ')

    # verifica constantemente se a entrada digitada foi um número
    while True:
        # aplica o replace para retirar o negativo na verificação, dessa forma não atrapalha-se a condição de parada
        if num.replace('-', '', 1).isdigit():
            print('dado valido')
            break
        else:
            num = input('DIGITE UM NÚMERO VALIDO: ')

    # faz a conversão do dado num inteiro
    num = int(num)

    if num < 0:
        print('ENCERRANDO TABUADA!')
        break

    cont = 0
    while cont <= 10:
        resultado = num * cont
        # print(resultado)
        print(f'{num} x {cont} = {resultado}')
        cont += 1

print('FIM')
