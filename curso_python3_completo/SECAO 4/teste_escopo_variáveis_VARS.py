# exemplo de uso da função vars (), usada para sada para retornar o dicionário de atributos de um objeto. 
# Se nenhum argumento for passado, ela retorna o dicionário de variáveis locais no escopo atual.

x = 10
y = 20

soma = x + y
print(soma)
print(vars()) # retorna as variaveis do escopo local
print('-'*50)

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.sexo = 'masculino'

# criando um objeto da classe pessoa chamado wesley
wesley = Pessoa('wesley', 24)
atributos_wesley = vars(wesley)

print(atributos_wesley)