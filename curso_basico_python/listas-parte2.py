# SEGUNDA PARTE DA AULA SOBRE LISTAS EM PYTHON

"""
    SERÁ ABORDADA A CRIAÇÃO DE LISTAS DENTRO DE LISTAS, CRIANDO UMA ESPÉCIE DE MATRIZ



"""

# PRIMEIRA FORMA: fazendo o trecho de código abaixo, encontramos um erro: criamos uma ligação de listas e não uma cópia.
#                   desta maneira, ao modificarmos a lista teste e darmos o append na lista galera, nós modificamos todo o conteúdo.
#                   Para resolver isso precisamos criar uma cópia usando o método '[:]', mostrado na segunda parte

teste = list()
teste.append('gustavo')
teste.append(40)

galera = list()
galera.append(teste)

teste[0] = 'MARIA'
teste[1] = 22
galera.append(teste)

print(galera)

# SEGUNDA PARTE: criando uma cópia ao invés de uma ligação:

teste = list()
teste.append('gustavo')
teste.append(40)

galera = list()
galera.append(teste[:])

teste[0] = 'MARIA'
teste[1] = 22
galera.append(teste[:])


print(galera)


# criando listas compostas e explorando suas possibilidades

dados = [['wesley', 24], ['laura', 24], ['eva', 60], ['vagner', 37]]

print(dados[0])
print(dados[0][0])
print(dados[0][1])

print(dados[1])
print(dados[1][0])
print(dados[1][1])

for pessoa in dados:
    print(pessoa[0])

for pessoa in dados:
    print(pessoa[1])

for pessoa in dados:
    print(f'o(a) {pessoa[0]} tem {pessoa[1]} anos.')



# usando cópia em lista temporária e lista de armazenamento
dado = list()
lista = list()
for c in range(0, 5):
    dado.append(str(input('digite seu nome: ')))
    dado.append(int(input('digite sua idade: ')))
    lista.append(dado[:])
    #usar a função clear() para limpar a lista temporária
    dado.clear()
print(lista)
