# --------- EXERCÍCIO 1 ------------
# Faca um programa que peca ao usuário para digitar um número inteiro
# e diga se é par ou ímpar,
# caso o usuário nao digite um numero inteiro informe que nao é um número inteiro.

# numero = input("digite um numero inteiro: ")
# try:
#     numero_int = int(numero)

#     if (numero_int % 2) == 0:
#         print("numero par")
#     else:
#         print("numero impar")

# except:
#     print("voce nao digitou um numero inteiro")

    # ou ainda, para evitar que convertamos um float e usemos somente sua parte
    # inteira podemos verificar se a classe do numero é int.
# while True:
#     numero = input("digite um numero inteiro: ")

#     if numero in 'Xx':
#         break

#     if '.' not in numero: #se não houver ponto, provavelmente é um inteiro
#         try: #tente converter a str para int
#             numero_int = int(numero)
#             if (numero_int % 2) == 0:
#                 print('numero par.')
#             elif numero_int == 0:
#                 print('você digitou zero')
#             else:
#                 print('numero impar')
#         except: #caso não de...
#             print(f'ERRO, você digitou "{numero}", verique se é um inteiro ou possui caracteres especiais...')
#     else: # se houver ponto provavelmente é um float
#         print('VOCÊ NÃO DIGITOU UM INTEIRO, VERIFIQUE O QUE FOI DIGITADO.')
    

#------------------ EXERCICIO 2 ------------------
# Faca um programa que pergunte a hora e imprima a saudacao correta,
#  exiba: bom dia (0-11), boa tarde (12-17), boa noite(18-23)

# import datetime as dt

# nome = input('qual seu nome? ')
# hora_atual = dt.datetime.now().strftime("%H")
# hora_atual_int = int(hora_atual)
# print(f'hora coletada: {hora_atual_int}')

# if hora_atual_int >= 0 and hora_atual_int <= 11:
#     print(f'OLÁ "{nome}", BOM DIA!')
# elif hora_atual_int >= 12 and hora_atual_int <= 17:
#     print(f'OLÁ "{nome}", BOA TARDE!')
# elif hora_atual_int >= 18 and hora_atual_int <= 23:
#     print(f'OLÁ "{nome}", BOA NOITE!')

# ------------------ EXERCICIO 3 ----------------------
#faça um programa que peca o primeiro nome do usuario.
# Se o nome tiver 4 letras ou menos escreva "seu nome é curto”, 
# se tiver entre 5 e 6 letras "seu nome é normal” 
# se for mais que 6 letras escreva "seu nome é grande”

nome = input('digite seu nome: ')
tamanho_nome = len(nome)

if nome:
    if tamanho_nome <= 4:
        print('nome é pequeno')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('nome normal')
    elif tamanho_nome > 6:
        print('nome grande')

else:
    print('digite algo')
