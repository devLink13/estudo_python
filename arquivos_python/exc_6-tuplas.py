# # Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9. ok
# B) Em que posição foi digitado o primeiro valor 3. ok
# C) Quais foram os números pares.


numeros = (int(input('digite um número: ')),
           int(input('digite um número: ')),
           int(input('digite um número: ')),
           int(input('digite um número: ')))

print(numeros)

print(f'o número 9 apareceu {numeros.count(9)} vezes na listagem')

if 3 in numeros:
    print(f'o número 3 apareçou primeiro na posição {numeros.index(3)}')
else:
    print('o numero 3 não está presente na tupla')

print('os numeros pares digitados são: ', end='')
for c in range(0, len(numeros)):
    if (numeros[c] % 2) == 0:
        print(numeros[c], end='-')
