''' 
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

check list:

1. media de idade = ok
2. nome do  homem = ok
3. idade do homem mais velho = ok
4. quantidade de mulheres com menos de 20 anos = ok


'''

import time

maior_idade = 0
menor_idade = 0
media_idade = 0
nome_homem_velho = ''
cont_mulheres = 0
validador_homem = bool
cont_validador_homem = 0
validador_mulher = bool
cont_validador_mulher = 0

num_pessoas = int(input('Quantas pessoas serão inseridas na base de dados? '))
# print(num_pessoas)

for c in range(0, num_pessoas):

    # formatar dados e solicitar entrada
    print('######## PESSOA Nº {0} ########'.format(c+1))
    nome = str(input('Nome completo: ')).strip().upper()
    # print(nome)
    idade = int(input('Idade: '))
    # print(idade)
    sexo = str(input('Sexo [M / F]: ')).strip().upper()
    # print(sexo)

    # setar valores para base de comparação na primeira iteração
    if maior_idade == 0 and menor_idade == 0:
        maior_idade = idade
        menor_idade = idade

    # acumula a idade na variável, o calculo em si é feito fora do laço, neste momento media_idade é um acumulador.
    media_idade = media_idade + idade

    # verificação do nome do homem mais velho e da idade do mais velho
    if sexo == 'M':
        cont_validador_homem += 1
        if idade >= maior_idade:
            nome_homem_velho = nome
            maior_idade = idade

    # quantia de mulheres menores de 20 anos
    if sexo == 'F':
        if idade < 20:
            cont_mulheres = cont_mulheres + 1
            cont_validador_mulher += 1


# calculo final da media de idade
media_idade = media_idade / num_pessoas


# lógica do validador de dados de homens, se houver homens o contador possui valor maior que zero
if cont_validador_homem == 0:
    validador_homem = False
else:
    validador_homem = True

# se houverem mulheres com menos de 20 anos o contador possuirá valor maior que zero
if cont_validador_mulher == 0:
    validador_mulher = False
else:
    validador_mulher = True


print('########### ANALISANDO ########### ')
time.sleep(1)
print('########### DADOS RELEVANTES ###########')

print('O NÚMERO DE PESSOAS INSERIDAS FOI: {}'.format(num_pessoas))

print('A MÉDIA DE IDADE FOI: {}'.format(int(media_idade)))

# se os validadores permitem quer dizer que há o determinado dado armazenado e será printado
# senão os validores não permitirão imprimir nenhuma informação

if validador_homem == True:
    print('O HOMEM MAIS VELHO POSSUI {0} ANOS E SEU NOME É {1}.'.format(
        maior_idade, nome_homem_velho))
else:
    print('Não houve inserção de dados de homens.')

if validador_mulher == True:
    print('A QUANTIDADE DE MULHERES COM MENOS DE 20 ANOS É {}.'.format(cont_mulheres))
else:
    print('Não houveram inserções de mulheres com menos de 20 anos.')
print('###########        FIM       ###########')
