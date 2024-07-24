# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

lista_geral = list()
cad_pessoas = dict()


# loop principal
while True:

    # loop de validação de nome
    while True:
        nome = str(input('NOME: ')).upper().strip()
        # verifica se 'nome' contém apenas letras
        if nome.isalpha():
            cad_pessoas['nome'] = nome
            break
        else:
            print('Por favor, digite um nome válido.')

    # loop de validação de sexo
    while True:
        sexo = str(input('SEXO: [M/F]')).upper().strip()
        # verifico se o conteúdo de sexo são letras e se são apenas 'MmFf'
        if sexo.isalpha() and sexo in 'mMfF':
            cad_pessoas['sexo'] = sexo
            break
        else:
            print('Por favor, digite apenas [M/F].')

    # loop de validação de idade
    while True:
        idade = str(input('IDADE: ')).upper().strip()
        # verifico se idade é um número
        if idade.isnumeric():
            # converto idade para o tipo int, vacilitará os cálculos posteriores.
            idade = int(idade)
            cad_pessoas['idade'] = idade
            break
        else:
            print('Por favor, digite apenas números.')

    # loop de validação de opção de encerramento de cadastro

        # variável auxiliar para encerramento de loop principal
    cond_encerramento = False
    while True:
        opc_saida = str(input('CONTINUAR? [S/N] ')).upper().strip()
        # verifico se o conteúdo da variável opc_saida é composto apenas por letras e se possui apenas os valores 'sSnN'
        if opc_saida.isalpha() and opc_saida in 'sSnN':
            # se eu não quiser mais cadastrar ninguém...
            if opc_saida == 'N':
                print('ENCERRANDO CADASTRO...')
                # mudo a condicão de encerramento para True, o que validará a condição para encerramento do loop principal
                cond_encerramento = True
                # uso o break para sair do laço de validação da opção de encerramento
                break

            # se eu quiser continuar...
            elif opc_saida == 'S':
                # apenas uso o break para sair do laço de validação da opção de encerramento
                break
        else:
            print('Por favor, digite apenas [S/N].')

    # inserir os dados do dicionário atual na lista geral e limpar o dicionário atual

    # crio uma cópia dos dados de cad_pessoas para dentro de lista
    lista_geral.append(cad_pessoas.copy())
    # limpo o dicionário, lembrando que isso é opcional pois o dicionario substitui os valores a cada atribuição
    cad_pessoas.clear()

    # avalia se a condição de encerramento recebeu o valor True no momento que o cod passou pelo laço de validação da condição de encerramento
    # se continuar como False, continua o programa normalmente.
    if cond_encerramento == True:
        break

# obtendo quantidade de pessoas cadastradas
num_pessoas_cad = len(lista_geral)

# calculando a média de idade das pessoas
med_idade = 0
for c in range(0, len(lista_geral)):
    med_idade = med_idade + lista_geral[c]['idade']
med_idade = med_idade / len(lista_geral)

# obtendo listas de homens e mulheres cadastradas
lista_mulheres = list()
lista_homens = list()
for c in range(0, len(lista_geral)):
    if lista_geral[c]['sexo'] == 'F':
        lista_mulheres.append(lista_geral[c]['nome'])
    else:
        lista_homens.append(lista_geral[c]['nome'])

# obtendo lista de pessoas com idade acima da média do grupo
acima_med_idade = list()
for c in range(0, len(lista_geral)):
    if lista_geral[c]['idade'] > med_idade:
        acima_med_idade.append(lista_geral[c])

# INICIANDO PARTE DE EXIBIÇÃO DOS RESULTADOS

# dois prints vazios para dar 2 espaços
for c in range(0, 2):
    print()

print(f'{" ANÁLISE DOS DADOS CADASTRADOS ":*^70}')
# dois prints vazios para dar 2 espaços
for c in range(0, 2):
    print()

print(f'A) AO TODO FORAM CADASTRADAS {num_pessoas_cad} PESSOAS.')
print(f'B) A MÉDIA DE IDADE DAS PESSOAS CADASTRADAS É {med_idade:.0f} ANOS.')
print('C) AS MULHERES CADASTRADAS FORAM: ', end='')
for mulher in lista_mulheres:
    print(mulher, end='; ')
print()

print('D) LISTA DAS PESSOAS QUE POSSUEM IDADE ACIMA DA MÉDIA DO GRUPO: ')
for c in range(0, len(acima_med_idade)):
    print(f'   -> nome = {acima_med_idade[c]['nome']}, sexo = {acima_med_idade[c]['sexo']}, idade = {acima_med_idade[c]['idade']}')

# dois prints vazios para dar 2 espaços
for c in range(0, 2):
    print()

print(f'{' FIM ':*^70}')
