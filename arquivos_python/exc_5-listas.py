# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = list()
lista_par = list()
lista_impar = list()

# laço de inserção de dados
while True:
    num = input('digite um número para inserção, caso queira sair digite "x": ')

    # conferir se foi digitado o cod de saida
    if num in 'xX':
        print('encerrando a inserção de dados...')
        break

    # caso não deseja sair, continue inserindo valores na lista principal
    else:
        lista.append(int(num))

# variavel de controle de laço de varredura
pos = 0

# laço de varredura
while pos < len(lista):

    # verifica em cada indice da lista se o seu conteúdo é divisível por 2 ou não.
    if lista[pos] % 2 == 0:
        # caso seja par, acrescenta este valor à lista dos pares
        lista_par.append(lista[pos])

    else:
        # se não for par, só pode ser ímpar, acrescentar este valor a lista dos impares.
        lista_impar.append(lista[pos])

    pos = pos + 1


print('=*'*10, 'RESUMO DAS INSERÇÕES', '=*'*10)
print(f'\033[35mA lista com todas inserções foi: {lista}\033[m \n\033[32mA lista dos pares é: {
      lista_par}\033[m\n\033[33mA lista dos impares é: {lista_impar}\033[m')
