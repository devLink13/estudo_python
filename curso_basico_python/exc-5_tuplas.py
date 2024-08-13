# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
#  No final, mostre a lista ordenada na tela.

lista = list()
b = 0
lista_ordenada = [0, 0, 0, 0, 0]
num_ant = num_post = int
# print(lista_ordenada[b+4])

for _ in range(0, 5):
    lista.append(int(input(f"Digite o {_+1}º numero: ")))

for c in range(0, len(lista)-1):
    if (lista[c]) > lista[c+1]:
        lista_ordenada[c] = lista[c+1]
    else:
        lista_ordenada[c] = lista[c]

"""
1º ite lista[0] -> 0
       lista[0+1] -> 1

       em ordem não mexe

2º ite lista[1] -> 1
        lista [1+1=2] -> 3

        em ordem não mexe

 3º ite lista[2] -> 3
        lista[2+1=3] -> 2
        
                     



"""        

print(lista)
print(lista_ordenada)
