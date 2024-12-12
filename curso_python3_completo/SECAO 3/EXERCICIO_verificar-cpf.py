# SUPER EXERCÍCIO
'''
CRIAR UM PROGRAMA DE VERIFICAÇÃO DE CPF

Todo cpf gerado em território brasileiro é formado a partir de um algoritmo, para verificar os cpfs informados
siga o algoritmo abaixo:

------------------------ ALGORITMO PARA CALCULAR E VERIFICAR O PRIMEIRO DÍGITO DO CPF ----------------------
1 -> O algoritmo de validação do CPF calcula o primeiro dígito verificador a partir dos 9 primeiros dígitos do CPF

Calculo do primeiro dígito do CPF
CPF: 746.824.890-70 (EXEMPLO)
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2 (SEQUENCIA DE 10 a 2)
*  7   4  6  8  2  4  8  9  0 (DIGITO A DIGITO)
-------------------------------
   70  36 48 56 12 20 32 27 0  (RESULTADO DA MULTIPLICAÇÃO)

- Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301 

- Multiplicar o resultado anterior por 10
301 * 10 = 3010

- Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

------------------------ ALGORITMO PARA CALCULAR E VERIFICAR O SEGUNDO DÍGITO DO CPF ----------------------
2 -> O algoritmo de validação do CPF calcula o segundo dígito verificador a partir dos 10 primeiros dígitos do CPF

Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2 (sequencia de 11 a 2)
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
--------------------------------
   77 40 54 64 14 24 40 36  0 14 (resultado)

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
'''


# ------------------------------------------ PROGRAMA ----------------------------------

# cpf_informado = '503.951.260-02'
while True:
    cpf_informado = input('informe seu cpf: ')

    # tratamento do cpf
    cpf_informado_tratado = cpf_informado.replace('.', '').replace('-', '')
    tamanho_cpf = len(cpf_informado_tratado)
    # print(cpf_informado_tratado)

    if cpf_informado_tratado.isdigit() and tamanho_cpf == 11:

        primeiro_digito_informado = int(cpf_informado_tratado[-2])
        segundo_digito_informado = int(cpf_informado_tratado[-1])

        # print(primeiro_digito_informado, type(primeiro_digito_informado))
        # print(f'{cpf_informado=}', f'{cpf_informado_tratado=}, f'{tamanho-cpf=}')
        # print(*cpf_informado_tratado, sep='\n') #printando cada digito - VERIFICACAO
        break

    else:
        print('informe o cpf corretamente!!')

# VARIAVEIS GLOBAIS DE ACESSO -----------
validade_primeiro_digito = 'INVALIDO'
validade_segundo_digito = 'INVALIDO'
# ----------------------------------------


# ------------ verificação primeiro digito --------------------------------------------------------------------
multiplo = 10
soma = 0
for digito in cpf_informado_tratado:
    # print(digito, type(digito), end =' | ')

    digito_int = int(digito)
    resultado_unitario = multiplo * digito_int
    soma = soma + resultado_unitario

    # print(f'{digito_int} * {multiplo} = {resultado_unitario}.')
    multiplo = multiplo - 1

    if multiplo < 2:  # 2 é o mínimo na sequência, deve terminar aqui
        multiplo = 0
        break  # mata o for quando multiplo é 2

# print(f'{soma=}') # resultado esperado 301

# calculo do primeiro digito, conforme algoritmo
calculo_primeiro_digito = soma * 10
calculo_primeiro_digito = calculo_primeiro_digito % 11
primeiro_digito_calculado = 0 if calculo_primeiro_digito > 9 else calculo_primeiro_digito

# print(f'{primeiro_digito_calculado=}', f'{primeiro_digito_informado=}')

# atribuir valido ou invalido para primeiro digito
# caso o informado seja o mesmo que o calculado o digito é válido
validade_primeiro_digito = 'VALIDO' if primeiro_digito_calculado == primeiro_digito_informado else 'INVALIDO'  # operação ternária
# print(validade_primeiro_digito)

# fim verificação primeiro digito ---------------------------------------------------------------


# ------------ verificação segundo digito --------------------------------------------------------------------
multiplo = 11
soma = 0
for digito in cpf_informado_tratado:
    # print(digito, type(digito), end =' | ')

    digito_int = int(digito)
    resultado_unitario = multiplo * digito_int
    soma = soma + resultado_unitario

    # print(f'{digito_int} * {multiplo} = {resultado_unitario}.')
    multiplo = multiplo - 1

    if multiplo < 2:  # 2 é o mínimo na sequência, deve terminar aqui
        multiplo = 0
        break  # mata o for quando multiplo é 2

# print(f'{soma=}') # resultado esperado 363

# calculo do segundo digito, conforme algoritmo
calculo_segundo_digito = soma * 10
calculo_segundo_digito = calculo_segundo_digito % 11
segundo_digito_calculado = 0 if calculo_segundo_digito > 9 else calculo_segundo_digito

# print(f'{segundo_digito_calculado=}', f'{segundo_digito_informado=}')

# atribuir valido ou invalido para primeiro digito
# caso o informado seja o mesmo que o calculado o digito é válido
validade_segundo_digito = 'VALIDO' if segundo_digito_calculado == segundo_digito_informado else 'INVALIDO'  # operação ternária
# print(validade_segundo_digito)

# fim verificação segundo digito ---------------------------------------------------------------

validade_digitos = 'DIGITOS VALIDOS' if validade_primeiro_digito == 'VALIDO' and validade_segundo_digito == 'VALIDO' else 'DIGITOS INVALIDOS'

cpf_calculado = cpf_informado_tratado[:9] + \
    str(primeiro_digito_calculado) + str(segundo_digito_calculado)
# print(f'{cpf_informado_tratado=}, {cpf_calculado=}')
formatacao_cpf_CALCULADO = cpf_calculado[:3] + '.' + \
    cpf_calculado[3:6] + '.' + cpf_calculado[6:9] + '-' + cpf_calculado[9:]
formatacao_cpf_INFORMADO = cpf_informado_tratado[:3] + '.' + cpf_informado_tratado[3:6] + \
    '.' + cpf_informado_tratado[6:9] + '-' + cpf_informado_tratado[9:]

if (cpf_informado_tratado == cpf_calculado) and validade_digitos == 'DIGITOS VALIDOS':
    print(f'O CPF {formatacao_cpf_INFORMADO} é VÁLIDO!')

else:
    print(f'O CPF {formatacao_cpf_INFORMADO} é INVÁLIDO!')
