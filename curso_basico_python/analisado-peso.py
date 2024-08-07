# criar um programa que leia 5 entradas de peso e mostre qual o menor e qual o maior peso lido

peso_menor = 0.0
peso_maior = 0.0

for c in range(0, 5):
    pesoDigitado = float(input('digite um peso em Kg: '))
    if peso_menor == 0.0 and peso_maior == 0.0:
        peso_menor = pesoDigitado
        peso_maior = pesoDigitado
    elif pesoDigitado < peso_menor:
        peso_menor = pesoDigitado
    elif pesoDigitado > peso_maior:
        peso_maior = pesoDigitado
print('o menor peso digitado foi {0:.2f} e o maior peso digitado foi {1:.2f}'.format(
    peso_menor, peso_maior))
