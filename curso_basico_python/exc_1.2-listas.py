# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. ok
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = list()
min = max = 0
ind_min = 0
ind_max = 0

# solicitar 5 entradas
for _ in range(0, 5):
    numeros.append(int(input(f'Digite o {_+1}° número:')))
# printar as 5 entradas
print(numeros)

# identificar o maior e o menor valor
for c in range(0, len(numeros)):
    if numeros[c] < min:
        min = numeros[c]
        ind_min = c
    if numeros[c] > max:
        max = numeros[c]
        ind_max = c

# printar as saídas
print(f'o maior foi {max} e está na posição {ind_max}')
print(f'o menor foi {min} e está na posição {ind_min}')
