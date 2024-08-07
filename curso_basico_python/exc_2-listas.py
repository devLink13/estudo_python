# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. ok
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


lista = list()

cond = True
verificacao = str

# laço de inserção de valores
while cond:
    verificacao = input(
        'Você Gostaria de cadastrar algum número? [y/n]').upper().strip()

    if verificacao == 'Y':
        numero = int(input('Digite um número: '))
        if numero in lista:
            print('Esse número já foi cadastrado, digite outro.')
        else:
            lista.append(numero)

    # caso não queira mais, terminar a inserção de valores
    if verificacao == 'N':
        cond = False
        print('ENCERRANDO.')

# ordena a lista
if len(lista) != 0:
    #cria uma nova lista ordenando ela
    lista_ord = sorted(lista)

    #usando o método sort() a gente ordena a própria lista, ou seja, a modifica.
    #por isso que para este fim não podemos utilizá-lo.
    # lista.sort()
    print(f'A lista inserida foi: {lista}, e a lista ordenada é: {lista_ord}')

if len(lista) == 0:
    print('não há elementos na lista.')
