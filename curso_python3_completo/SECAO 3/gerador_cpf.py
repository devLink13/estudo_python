# confeccionar uma função de gerar cpf a partir do algoritmo de validação de cpf
def gerar_cpf() -> str:

    import random # biblioteca para gerar numeros aleatórios
    import funcao_verificar_cpf as cpf # chamar o arquivo que contém a função de verificar o cpf

    cpf_inicial = ''
    for c in range (0, 3):
        aleatorio_int = random.randint(100, 999)
        #print(aleatorio_int, type(aleatorio_int))

        aleatorio_str = str(aleatorio_int)
        cpf_inicial = cpf_inicial + aleatorio_str

        if c < 2:
            cpf_inicial += '.'
        else:
            cpf_inicial += '-'
            break

    #print(cpf_inicial)

    cpf_inicial_tratado = cpf_inicial.replace('.', '').replace('-', '')
    # print(cpf_inicial_tratado)

    contador_regressivo_1 = 10
    soma_digito_1 = 0
    for digito in cpf_inicial_tratado:
        
        resultado_unitario = int(digito) * contador_regressivo_1
        soma_digito_1 += resultado_unitario

        if contador_regressivo_1 == 2:
            # print(f'{soma_digito_1=}')
            break

        contador_regressivo_1 -= 1

    calculo_digito_1 = (soma_digito_1 * 10) % 11
    # print(f'{calculo_digito_1=}')

    digito_1 = 0 if calculo_digito_1 > 9 else calculo_digito_1
    #print(f'{digito_1=}')

    contador_regressivo_2 = 11
    soma_digito_2 = 0
    for digito in (cpf_inicial_tratado + str(digito_1)):
        
        resultado_unitario = int(digito) * contador_regressivo_2
        soma_digito_2 += resultado_unitario

        if contador_regressivo_2 == 2:
            #print(f'{soma_digito_2=}')
            break

        contador_regressivo_2 -= 1

    calculo_digito_2 = (soma_digito_2 * 10) % 11
    # print(f'{calculo_digito_2=}')

    digito_2 = 0 if calculo_digito_2 > 9 else calculo_digito_2
    #print(f'{digito_2=}')

    cpf_gerado = cpf_inicial + str(digito_1) + str(digito_2)
    #print(f'{cpf_gerado}, {type(cpf_gerado)}')

    # print(f'{cpf_gerado=}, {type(cpf_gerado)}')
    return cpf_gerado


lista_cpfs = list()
for c in range(10):
    cpf = gerar_cpf()
    lista_cpfs.append(cpf)

print(*lista_cpfs, sep='\n')