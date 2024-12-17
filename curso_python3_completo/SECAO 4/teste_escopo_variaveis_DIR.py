# a função dir() é usada para tentar retornar uma lista de atributos válidos para um objeto. 
# Se nenhum argumento for passado, ela retorna a lista de nomes no escopo local atual.
# Aqui está um exemplo de como usá-la:

x = 10
y = 20

soma = x + y
print(soma)

# Usando dir() para listar os nomes no escopo local
nomes_locais = dir()
print(nomes_locais) # retorna os nomes no escopo local
print('-'*50)

# para listar nomes, dir() é melhor que var
for item in dir():
    print(item)
print('-'*50)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.sexo = 'masculino'

# criando um objeto da classe pessoa chamado wesley
wesley = Pessoa('wesley', 24)

# Usando dir() para listar os atributos do objeto wesley
# DIFERENTE DO VARS() dir() me retorna apenas os atributos sem os valores
# no caso de objetos, para listar atributos, o uso de var é melhor
atributos_wesley = dir(wesley)
print(f'{atributos_wesley=}')