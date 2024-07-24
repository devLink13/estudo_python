lista = list()
while True:

    # solicito os 3 dados
    nome = str(input('NOME: '))
    nota_1 = float(input('NOTA 1: '))
    nota_2 = float(input('NOTA 2: '))
    media = (nota_1 + nota_2) / 2

    # FORMA DE CADASTRAR UMA LISTA COPIADA DO GUANABARA
    # ÓTIMA FORMA DE SIMPLIFICAR CÓDIGO
    lista.append([nome, [nota_1, nota_2], media])

    # verifico se o usuário quer continuar
    cond = input('CONTINUAR? [S/N]')
    if cond in 'nN':
        break

print(lista[0][1][1])
