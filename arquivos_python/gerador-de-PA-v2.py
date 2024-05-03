"""
Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

"""

"""
1. ler o primeiro termo da PA OK
2. ler a razão da PA    OK
3. imprimir os 10 primeiros termos da PA


--> formula do enésimo termo da PA: An=A1 + (n-1)*r

"""
primeiro = int(input('DIGITE O PRIMEIRO TERMO DA PA: '))
razao = int(input('DIGITE A RAZÃO DA PA: '))
num_termos = int(input('quantos termos você gostaria? '))

enesimo = primeiro + (num_termos - 1)*razao
print(enesimo)

cont_laco = 0
cont_pa = 1
pa = 0

while cont_laco < num_termos:
    pa = primeiro + (cont_pa - 1)*razao
    cont_laco = cont_laco + 1
    cont_pa = cont_pa + 1
    print(pa, '--> ', end='')

print('FIM')
