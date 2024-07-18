# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]

for c in range(0, 7):
    num = int(input(f'digite o {c+1}° valor: '))

    if num % 2 == 0:
        lista[0].append(num)

    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print(f'\033[35mOS VALORES PARES DIGITADOS FORAM: {
      lista[0]}\033[m \n\033[32mOS VALORES IMPARES DIGITADOS FORAM {lista[1]}\033[m')
