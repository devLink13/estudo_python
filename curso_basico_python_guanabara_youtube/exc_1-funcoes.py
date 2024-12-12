# Exercício Python 096: Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def calc_area(largura, comprimento):
    area = float()

    area = largura * comprimento
    print(f'UM TERRENO DE {largura}m x {comprimento}m posui área de {area}m².')


while True:

    print(f'{' CONTROLE DE TERRENO ':*^50}')

    largura = float(input('LARGURA DO TERRENO (m): '))
    comprimento = float(input('COMPRIMENTO DO TERRENO (m): '))

    calc_area(largura, comprimento)

    if str(input('DESEJA CONTINUAR? [S/N] ')) in 'nN':
        print(f'{' ENCERRANDO PROGRAMA ':*^50}')
        break
        
