# EXERCÍCIO / JOGO DE PERGUNTAS E RESPOSTAS USANDO LISTAS E DICIONÁRIOS

import random

lista_perguntas = [

    {
        'PERGUNTA': 'QUANTO É  5 x 5?',
        'OPCOES': ('0', '25', '29', '36'),
        'RESPOSTA': '25',
    },
    {
        'PERGUNTA': 'QUAL A CAPITAL DA FRANÇA?',
        'OPCOES': ('LONDRES', 'BERLIM', 'PARIS', 'MADRI'),
        'RESPOSTA': 'PARIS',
    },
    {
        'PERGUNTA': 'QUAL O RESULTADO DE 8 + 3?',
        'OPCOES': ('10', '11', '12', '13'),
        'RESPOSTA': '11',
    },
    {
        'PERGUNTA': 'QUAL O MAIOR OCEANO DO MUNDO?',
        'OPCOES': ('ATLÂNTICO', 'ÍNDICO', 'PACÍFICO', 'ÁRTICO'),
        'RESPOSTA': 'PACÍFICO',
    },
    {
        'PERGUNTA': 'QUEM DESCOBRIU A AMÉRICA?',
        'OPCOES': ('CRISTÓVÃO COLOMBO', 'PEDRO ÁLVARES CABRAL', 'VASCO DA GAMA', 'FERNÃO DE MAGALHÃES'),
        'RESPOSTA': 'CRISTÓVÃO COLOMBO',
    },
    {
        'PERGUNTA': 'QUAL O ELEMENTO QUÍMICO REPRESENTADO PELO SÍMBOLO O?',
        'OPCOES': ('OURO', 'OXIGÊNIO', 'PRATA', 'FERRO'),
        'RESPOSTA': 'OXIGÊNIO',
    },
    {
        'PERGUNTA': 'QUAL O PLANETA MAIS PRÓXIMO DO SOL?',
        'OPCOES': ('TERRA', 'MARTE', 'MERCÚRIO', 'VÊNUS'),
        'RESPOSTA': 'MERCÚRIO',
    },
    {
        'PERGUNTA': 'QUANTOS CONTINENTES EXISTEM NA TERRA?',
        'OPCOES': ('4', '5', '6', '7'),
        'RESPOSTA': '7',
    },
    {
        'PERGUNTA': 'QUAL A LÍNGUA OFICIAL DO BRASIL?',
        'OPCOES': ('ESPANHOL', 'PORTUGUÊS', 'INGLÊS', 'FRANCÊS'),
        'RESPOSTA': 'PORTUGUÊS',
    },

]
qtd_perguntas = len(lista_perguntas)
opcoes = ('a', 'b', 'c', 'd')
numero_perguntas = list(range(0, qtd_perguntas))
contador_acertos = 0
contador_erros = 0
contador_perguntas = 0

while True:
    print(numero_perguntas)
    # num_aleatorio = random.randint(0, qtd_perguntas-1)
    num_aleatorio = random.choice(numero_perguntas)
    print(num_aleatorio)
    numero_perguntas.remove(num_aleatorio)
    # print(f'{num_aleatorio=}')

    print(f'Pergunta: {lista_perguntas[num_aleatorio]['PERGUNTA']}')
    print()

    print('OPÇÕES:')
    tupla_posicoes = lista_perguntas[num_aleatorio]['OPCOES']
    # print(tupla_posicoes)
    for opcao in tupla_posicoes:
        index_opcao = tupla_posicoes.index(opcao)
        print(f'{opcoes[index_opcao]})', end=' ')
        print(opcao)

    while True:
        opcao_selecionada = input('ESCOLHA UMA OPCAO ou [s]air: ').lower()
        if opcao_selecionada in opcoes:
            contador_perguntas += 1 # acumula o numero de perguntas feitas
            adequar_index = opcoes.index(opcao_selecionada)
            # print(adequar_index)
            opcao_selecionada = lista_perguntas[num_aleatorio]['OPCOES'][adequar_index]
            print()
            print(f'VOCÊ RESPONDEU: {opcao_selecionada}')
            break
        elif opcao_selecionada in 'sS':
            print(f'VOCÊ ACERTOU {contador_acertos} DE {contador_perguntas} PERGUNTAS.')
            print('ATÉ LOGO.')
            exit()  # encerra o programa

        else:
            print('ESCOLHA APENAS A, B, C OU D.')

    resposta = lista_perguntas[num_aleatorio]['RESPOSTA']
    # print(resposta)

    if opcao_selecionada == resposta:
        print(f'PARABÉNS, VOCÊ ACERTOU !!! A RESPOSTA É {resposta}.')
        contador_acertos += 1
    else:
        print(f'VOCÊ ERROU, A RESPOSTA CORRETA É {resposta}...')
        contador_erros += 1

    if len(numero_perguntas) == 1:
        print()
        print('='*50)
        print('VOCÊ RESPONDEU TODAS AS PERGUNTAS.')
        print(f'VOCÊ ACERTOU {contador_acertos} DE {contador_perguntas} REALIZADAS.')

        continuar = input('DESEJA CONTINUAR JOGANDO? [S] OU [N] ').lower()

        if continuar in 'Ss':
            numero_perguntas = list(range(0, qtd_perguntas))
            contador_perguntas = 0
            contador_acertos = 0
            contador_erros = 0
        
        else:
            exit()

    print('-'*50)
    print()

    
