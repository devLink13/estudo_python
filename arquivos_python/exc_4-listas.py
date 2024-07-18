# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.


lista = list()

# variavel de cond de laço de digitação
cond = True

while cond:
    num = input(
        'digite o valor que deseja adicionar a lista, se quiser encerrar digite "x": ')

    # verifica se o usuário quer sair do programa
    if num in 'xX':
        cond = False
        print('encerrando o programa')

    # se não for digitado 'x ou X' continua o programa
    else:
        # acrescenta o valor à lista, convertendo para inteiro primeiro.
        lista.append(int(num))
        print(f'valor {num} inserido com sucesso!')

print(lista)
print('=*'*50)
print('='*10, 'DADOS DA LISTA', '='*10)
print(f'A) FORAM DIGITADOS {len(lista)} ELEMENTOS NA LISTA.')
print(f'B) A LISTA DE VALORES EM ORDEM DECRESCENTE FICA DA SEGUINTE FORMA: {
      sorted(lista, reverse=True)}')

if 5 in lista:
    print('C) O NÚMERO 5 FOI INSERIDO NA LISTA')
else:
    print('C) O NÚMERO 5 NÃO FOI INSERIDO NA LISTA.')
