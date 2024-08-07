# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

from time import sleep

produtos = ('PLACA MÃE', 350.50,
            'MEMÓRIA RAM', 150.89,
            'MOUSE', 55.00,
            'TECLADO', 89.90)

cond = str

# # forma de printar a tupla ordenada usando for
# for p in range(0, len(produtos)):
#     print(produtos[p])


# # segunda forma de printar a tupla ordenada usando for
# for _ in produtos:
#     print(_)

print('-'*60)
print(f'{"LISTA DE PREÇOS":^60}')
print('-'*60)

for p in range(0, len(produtos)):
    if (p % 2) == 0:
        print(f'{produtos[p]:.<50}', end='')
    else:
        print(f'R${produtos[p]:>8.2f}')

print('-'*60)


while True:
    # PERGUNTA GERAL PARA INICIAR BUSCA POR PRODUTO E PREÇO
    cond = str(input(
        'VOCÊ GOSTARIA DE PESQUISAR O PREÇO DE ALGUM PRODUTO? [y/n]')).strip().upper()

    # CONDIÇÃO PARA FINALIZAR PROGRAMA
    if cond == 'N':
        print(f'\033[33mOBRIGADO, FINALIZANDO TAREFA.\033[m')
        break

    # LÓGICA DE BUSCA DE PREÇO E PRODUTO.
    if cond == 'Y':
        produto = str(input('QUAL PRODUTO VOCÊ PRECISA?')).upper()

        # pesquisar primeiro se existe o produto na tupla.
        if produto in produtos:
            print('PROCURANDO, AGUARDE...')
            indice = produtos.index(produto) + 1
            sleep(1)
            print(f'R${produtos[indice]}')
        else:
            print('produto inexistente')
