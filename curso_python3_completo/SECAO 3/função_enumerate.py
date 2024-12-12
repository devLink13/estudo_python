# estudo relativo a função enumerate
# É uma função que retora um iterável que permite enumerar os índices de um iterável como tuplas, listas, strings entre outros…

lista = ['ana', 'mario', 'lucas']
lista_enumerada = enumerate(lista)

#passando uma lista enumerada, que iremos obter uma tupla
for item in lista_enumerada:
	print(item)

#chamando a função diretamente no for
for indice, nome in enumerate(lista):
	print(indice, nome)
	
# ao inves de usar na chamada da função, podemos usar o desempacotamento
for item in enumerate(lista):
	indice, nome = item
	print(f'{indice=}, {nome=}')
	
#sabendo que item é uma tupla contendo indice valor, podemos aninhar for
for item in enumerate(lista):
	print('FOR EXTERNO: ')
	for valor in item:
		print(f'\t{valor}')
		
for indice, valor in enumerate(lista):
    print(f'{lista[indice]} = {valor}')