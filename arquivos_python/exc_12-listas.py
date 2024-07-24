# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.


boletim = list()
boletim_temp = list()
lista_medias = list()
media = 0
# nota_med = 0

while True:

    # solicito os 3 dados
    nome = str(input('NOME: '))
    nota_1 = float(input('NOTA 1: '))
    nota_2 = float(input('NOTA 2: '))

    # armazeno os dados numa lista temporária auxiliar
    boletim_temp.append(nome)
    boletim_temp.append(nota_1)
    boletim_temp.append(nota_2)

    # método para armazenar a média junto a lista auxiliar e jogar estas informações juntos na lista principal
    media = (nota_1 + nota_2) / 2
    boletim_temp.append(media)

    # faço uma cópia da lista temporária na lista principal
    boletim.append(boletim_temp[:])

    # limpo a lista temporária
    boletim_temp.clear()

    # verifico se o usuário quer continuar
    cond = input('CONTINUAR? [S/N]')
    if cond in 'nN':
        break


# # método para calcular a média após inserir as informações na lista do boletim
# # o método usado acima eu pensei depois e se mostrou mais eficiente e prático de usar

# for c in range(0, len(boletim)):
#     for n in range(1, 3):
#         nota_med += boletim[c][n]
#     media = nota_med / 2
#     lista_medias.append(media)
#     nota_med = 0

print('=-'*20)
print(f'{"N°":<10}{"NOME":^10}{"MEDIA":>20}')
print(f'-'*40)

# formatação de print
for i, b in enumerate(boletim):
    print(f'{i:<10}{b[0]:^10}{b[3]:>20}')

# verificar a nota de um aluno específico:
while True:
    al = input('VERIFICAR AS NOTAS DE QUAL ALUNO? [X PARA SAIR]')

    if al in 'Xx':
        print('encerrando boletim, obrigado.')
        break
    elif al.isnumeric():
        al = int(al)
        if al <= (len(boletim)-1):
            print(f'O ALUNO {boletim[al][0]} OBTEVE AS SEGUINTES NOTAS: NOTA 1 {
                  boletim[al][1]} E NOTA 2 {boletim[al][2]}')

        else:
            print('NÃO HÁ ALUNO PARA ESTA CORRESPONDÊNCIA, TENTE NOVAMENTE.')
    else:
        print('Por favor digite um valor válido!')
