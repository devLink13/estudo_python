# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. ok
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = list()

for _ in range(0, 5):
    numeros.append(int(input(f'Digite o {_+1}° número: ')))

# mostrar a lista
print('você digitou os valores ', numeros)
# printar o valor máximo
print(f'O maior valor digitado foi {
      max(numeros)} e está na posição {numeros.index(max(numeros))}')

# printar o menor valor lido
print(f'O menor valor digitado foi {
      min(numeros)} e está na posição {numeros.index(min(numeros))}')
