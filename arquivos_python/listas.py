# AULA SOBRE LISTAS EM PYTHON

'''
    LISTAS E TUPLAS SÃO VARIÁVEIS COMPOSTAS
        -> LISTAS SÃO MUTÁVEIS E USAM '[]' PARA SER CRIADAS

        -> TUPLAS SÃO IMUTÁVEIS E USAM '()' PARA SER CRIADAS


A) adicionar itens à lista        

listas.append[item a adiconar]
listas.insert[indice, item a adicionar]

B) deletar lista

del lista[indice]
lista.pop[indice]                           #para eliminar pelo indice
lista.remove['valor a ser eliminado']       #para eliminar pelo valor

C) if 'valor' in lista: faça tal coisa

D) declarar uma lista a partir de um range

lista = list(range(4,11)) # saida: lista [4,5,6,7,8,9,10]

E) ordenar valores dentro de uma lista

lista.sort()
ou
lista.sort(reverse = True)

F) tamanho da lista

len(lista)


'''


# exemplos práticos com listas


# lista são mutáveis, veja abaixo:
lista = [0, 7, 4, 6]
print(lista)
lista[0] = 1
print(lista)

# não é possivel adicionar valores à lista da maneira acima
# erro de excesso de tamanho
# lista[4] = 3
# print(lista)

# para adicionar mais valores a lista usa-se o append
lista.append(7)
print(lista)

# para ordenar a lista utiliza-se o método sort
lista.sort()
print(lista)

# pode-se ordenar em forma inversa
lista.sort(reverse=True)
print(lista)

# numeros de elementos da lista
print(len(lista))

# adicionar elemento em um determinado lugar
lista.insert(2, 7)
print(lista)
print(len(lista))

# removendo elemento
lista.pop()  # remove o [último elemento se não passar nenhum parâmetro
print(lista)

lista.pop(2)  # remove o segundo indice da lista
print(lista)

lista.append(10)
lista.insert(3, 10)
print(lista)
lista.remove(10)  # remove o valor 10, e não o indice 10
print(lista)

# # exemplo de erro usando o remove, se usar o método remove e passar como parâmetro um valor inexistente acontece o seguinte erro:
# lista.remove(20)
# print(lista) #saida: list.remove(x): x not in list

# verificar valor em lista para remove

if 20 in lista:
    lista.remove(20)
else:
    print('não há 20 na lista')

# formas de declarar uma lista

lista2 = list()
# ou
lista2 = []


lista2.append(1)
lista2.append(3)
lista2.append(4)
lista2.append(7)

print(lista2)

# como iterar sobre o for
for p, v in enumerate(lista2):
    print(f'na posição {p} está guardado o valor {v}')

for v in lista2:
    print(v)

for c in range(0, len(lista2)):
    print(f'na posição {c} está guardado o valor {lista2[c]}')


# ATENÇÃO AO IGUALAR LISTAS EM PYTHON, ELAS CRIAM CONEXÕES SE NÃO FOREM DEVIDAMENTE DECLARADAS EM SUA IGUALDADE
# EXEMPLO:

a = [0, 2, 4, 6]
b = a
print(f'lista A: {a}')
print(f'lista B: {b}')

# agora veja
b[2] = 5  # alterar somente o segundo indice da lista b também altera a lista A pois elas estão ligadas
print(f'lista A: {a}')
print(f'lista B: {b}')

# como desconectar listas
a = [0, 2, 4, 6]
b = a[:]                    # dessa forma dizemos que b recebe a como cópia
b[2] = 5
print(f'lista A: {a}')
print(f'lista B: {b}')


