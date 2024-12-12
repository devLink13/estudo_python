class CPFisInvalidError(Exception):
    pass

def validar_cpf(cpf):
    '''
        ESTA FUNÇÃO VERIFICA O CPF INFORMADO COMO ARGUMENTO, PARA TANTO ELE PRECISA RESPEITAR AS REGRAS 
        DE DIGITAÇÃO DO CPF, PODENDO OU NÃO COLOCAR '.' E '-', OUTROS CARACTERES NÃO SERÃO ACEITOS

        OBS: NA VERIFICAÇÃO DO SEGUNDO DIGITO NÃO FOI ACRESCIDO DO 
    '''
    cpf_informado = cpf

    # tratamento do cpf
    cpf_informado_tratado = cpf_informado.replace('.', '').replace('-', '')
    tamanho_cpf = len(cpf_informado_tratado)
    # print(cpf_informado_tratado)

    
    if cpf_informado_tratado.isdigit() and tamanho_cpf == 11: # PRIMEIRA VERIFICAÇÃO

        if (cpf_informado_tratado[0] * tamanho_cpf) == cpf_informado_tratado: # SEGUNDA VERIFICAÇÃO
            raise CPFisInvalidError()

        primeiro_digito_informado = int(cpf_informado_tratado[-2])
        segundo_digito_informado = int(cpf_informado_tratado[-1])

        # print(primeiro_digito_informado, type(primeiro_digito_informado))
        # print(f'{cpf_informado=}', f'{cpf_informado_tratado=}, f'{tamanho-cpf=}')
        # print(*cpf_informado_tratado, sep='\n') #printando cada digito - VERIFICACAO

    else:
        raise CPFisInvalidError()

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

    #print(f'{primeiro_digito_calculado=}', f'{primeiro_digito_informado=}')

    # atribuir valido ou invalido para primeiro digito
    # caso o informado seja o mesmo que o calculado o digito é válido
    validade_primeiro_digito = 'VALIDO' if primeiro_digito_calculado == primeiro_digito_informado else 'INVALIDO'  # operação ternária
    # print(validade_primeiro_digito)

    # fim verificação primeiro digito ---------------------------------------------------------------


    if validade_primeiro_digito == 'VALIDO':
    # ------------ verificação segundo digito --------------------------------------------------------------------
        multiplo = 11
        soma = 0
        for digito in cpf_informado_tratado:
            #print(digito, type(digito), end =' | ')

            digito_int = int(digito)
            resultado_unitario = multiplo * digito_int
            soma = soma + resultado_unitario

            #print(f'{digito_int} * {multiplo} = {resultado_unitario}.')
            multiplo = multiplo - 1

            if multiplo < 2:  # 2 é o mínimo na sequência, deve terminar aqui
                multiplo = 0
                break  # mata o for quando multiplo é 2

        # print(f'{soma=}') # resultado esperado 363

        # calculo do segundo digito, conforme algoritmo
        calculo_segundo_digito = soma * 10
        calculo_segundo_digito = calculo_segundo_digito % 11
        segundo_digito_calculado = 0 if calculo_segundo_digito > 9 else calculo_segundo_digito

        #print(f'{segundo_digito_calculado=}', f'{segundo_digito_informado=}')

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
            # print(f'O CPF {formatacao_cpf_INFORMADO} é VÁLIDO!')
            return True

        else:
            # print(f'O CPF {formatacao_cpf_INFORMADO} é INVÁLIDO!')
            return False

    else:
        #print('nem o primeiro digito é válido')
        return False
# ----------- testes ---------------
# validade_cpf = validar_cpf('03455997058')
# print(validade_cpf)

# validade_cpf = validar_cpf('034.559.970-58')
# print(validade_cpf)

# validade_cpf = validar_cpf('03455997058')
# print(validade_cpf)

# validade_cpf = validar_cpf('0345599705a') #typeError
# print(validade_cpf)
#validade_cpf = validar_cpf('0345599705858') #ValueError

# validade = 'VÁLIDO' if validar_cpf(input('cpf: ')) == True else 'INVÁLIDO'
# print(validade)
