"""
Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 

    ALGORITMO:
    1. LER O NOME OK 
    2. LER O PREÇO OK 
    3. PERGUNTAR SE QUER CADASTRAR MAIS PRODUTOS OU NÃO ok
    4. TOTAL GASTO NA COMPRA ok 
    5. QUANTOS PRODUTOS CUSTAM MAIS DE 1000 ok
    6. PRODUTO MAIS CARO


"""
cont_produtos = 1
total = 0.0
maior_mil = 0
mais_caro = 0
nome_mais_caro = ''

while True:
    print('-'*20, f'CADASTRO DO PRODUTO N°{cont_produtos}', '-'*20)

    nome_produto = str(input('PRODUTO: ')).upper()

    preco_produto = float(input('PREÇO: R$ '))
    total = total + preco_produto
    if preco_produto >= 1000:
        maior_mil += 1
    if preco_produto > mais_caro:
        nome_mais_caro = nome_produto
        mais_caro = preco_produto

    if input('CONTINUAR CADASTRO [S - SIM / N - NÃO]: ').upper() == 'N':
        break

    cont_produtos += 1

print('-'*20, 'ESTATISTICAS DOS PRODUTOSM', '-'*20)
print(f'TOTAL GASTO NA COMPRA: R${total:.2f}')
print(f'N° DE PRODUTOS QUE CUSTAM MAIS DE R$ 1.000,00: {maior_mil}')
print(f'O PRODUTO MAIS CARO FOI O(A) {nome_mais_caro} E O SEU CUSTO FOI DE R${mais_caro:.2f}.')
