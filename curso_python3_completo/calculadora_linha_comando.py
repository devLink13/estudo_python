# tentar desenvolver uma calculadora que seja capaz de entender a estrutura digitada e realizar a operação

operacao = input('digite a operação: ')
tamanho_operacao = len(operacao)
digito = ''
digito_float = 0.0
digito_int = 0

lista_dig_operador = []
fim_verificacao = tamanho_operacao - 1


# ex: 123.5+45

# algortimo:
'''
    1° - percorrer o numero enquanto for digito e armazená-lo em uma variavel
'''
contador = 0
while contador < tamanho_operacao:

    if operacao[contador].isdigit() or operacao[contador] == '.':
        digito += operacao[contador]
        print(digito)

    elif operacao[contador].isdigit() is not True and operacao[contador] != '.' or contador == fim_verificacao:

        if operacao[contador] == '+':

            if '.' in digito:
                digito_float = float(digito)
                lista_dig_operador.append(digito_float)
                digito = ''
            else:
                digito_int = int(digito)
                lista_dig_operador.append(digito_int)
                digito = ''

            operador = operacao[contador]
            lista_dig_operador.append(operador)

        elif operacao[contador] == '-':
            if '.' in digito:
                digito_float = float(digito)
                lista_dig_operador.append(digito_float)
                digito = ''
            else:
                digito_int = int(digito)
                lista_dig_operador.append(digito_int)
                digito = ''

            operador = operacao[contador]
            lista_dig_operador.append(operador)

    if contador == fim_verificacao:
        if '.' in digito:
            digito_float = float(digito)
            lista_dig_operador.append(digito_float)
            digito = ''
        else:
            digito_int = int(digito)
            lista_dig_operador.append(digito_int)
            digito = ''

    contador += 1

print(lista_dig_operador)

#[125.5, '+', 10, '-', 25]
# nas posições de indice par temos os operandos
# nas posicoes de indice impar temos os operadores


#calculo do resultado
resultado = lista_dig_operador[0]
i = 1
while i < len(lista_dig_operador):
    operador = lista_dig_operador[i]
    numero = lista_dig_operador[i+1]

    if operador == '+':
        resultado += numero
    elif operador == '-':
        resultado -= numero
    
    i += 2 #avança para próximo operador
print(resultado)