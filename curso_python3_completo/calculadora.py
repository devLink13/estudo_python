#desenvolver uma calculadora simples

adicao = False
subtracao = False
multiplicacao = False
divisao = False


print('bem vindo a calculadora, para sair digite 0000 a qualquer momento.')
precisao_calculadora = int(input('quantas casas decimais após a virgula você deseja? '))
while True:

    operando_1 = input('digite um operando: ')
    if operando_1 == '0000': break

    if operando_1.replace('.', '').isdigit():
        try:
            operando_1_float = float(operando_1)

        except:
            print('verfique se você digitou um numero valido...')

    else:
        print('você não digitou um numero válido')
        continue

    operador = input('digite um operador: ')

    if operador == '0000': break

    if operador == '+':
        adicao = True
    elif operador == '-':
        subtracao = True
    elif operador == '*':
        multiplicacao = True
    elif operador == '/':
        divisao = True
    else:
        print(f'o operador {operador} não é permitido, verique se foi digitado corretamente...')
        continue

    operando_2 = input('digite um operando: ')
    if operando_2 == '0000': break


    if operando_2.replace('.', '').isdigit():
        try:
            operando_2_float = float(operando_2)

        except:
            print('verfique se você digitou um numero valido...')
    else:
        print('verifique se você digitou um numero válido...')
        continue


    if adicao:
        resultado = operando_1_float + operando_2_float
    
    if subtracao:
        resultado = operando_1_float - operando_2_float

    if multiplicacao:
        resultado = operando_1_float * operando_2_float
    
    if divisao:
        resultado = operando_1_float / operando_2_float

    if resultado % 1 == 0: # verifique se o numero é inteiro
        resultado = int(resultado) # converte o resultado para inteiro
    else:
        resultado = f'{resultado:.{precisao_calculadora}f}'



    print(f'{operando_1} {operador} {operando_2} = {resultado}')