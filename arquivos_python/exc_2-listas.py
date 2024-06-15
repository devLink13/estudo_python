# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. ok
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 


lista = list ()

cond = True
verificacao = str

# laço de inserção de valores
while cond:
    verificacao = input('Você Gostaria de cadastrar algum número? [y/n]').upper().strip
    #verificar se o usuário quer cadastrar números na lista
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
print(f'A lista ficou da seguinte maneira: {lista}')

