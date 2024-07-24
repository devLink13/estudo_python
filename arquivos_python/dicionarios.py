"""
    RESUMÃO DE DICIONÁRIOS EM PYTHON
        curso em video, aula 19
        21/07/2024

        
1) dicionários são uma "espécie" de listas, ou ainda, são estruturas compostas que permitem o par chave-valor.

    - Os dicionários em Python são estruturas de dados que armazenam pares de chave-valor. Aqui estão alguns pontos principais:

        - Definição: Um dicionário é definido usando chaves {} com pares de chave-valor separados por dois pontos :. Por exemplo:
            meu_dicionario = {"nome": "João", "idade": 25, "cidade": "São Paulo"}

            Chaves (keys):
        As chaves são os identificadores únicos em um dicionário.
        Elas são usadas para acessar os valores correspondentes.
        As chaves devem ser imutáveis (por exemplo, strings, números, tuplas).
        Exemplo:
        
        meu_dicionario = {"nome": "João", "idade": 25}
        # "nome" e "idade" são as chaves.
        Código gerado por IA. Examine e use com cuidado. Mais informações em perguntas frequentes.
        Valores (values):
        Os valores são os dados associados às chaves.
        Eles podem ser de qualquer tipo de dado (strings, números, listas, outros dicionários, etc.).
        Exemplo:

        meu_dicionario = {"nome": "João", "idade": 25}
        # "João" e 25 são os valores.
        Código gerado por IA. Examine e use com cuidado. Mais informações em perguntas frequentes.
        Itens (items):
        Os itens são os pares chave-valor no dicionário.
        Cada item é uma combinação de uma chave e seu valor correspondente.
        Você pode obter todos os itens de um dicionário usando o método items(), que retorna uma lista de tuplas.
        Exemplo:

        meu_dicionario = {"nome": "João", "idade": 25}
        itens = meu_dicionario.items()
        # itens será dict_items([('nome', 'João'), ('idade', 25)])
        Código gerado por IA. Examine e use com cuidado. Mais informações em perguntas frequentes.
        Diferenças:

        Chaves são os identificadores únicos que você usa para acessar os valores.
        Valores são os dados armazenados no dicionário.
        Itens são os pares chave-valor combinados.
        Aqui está um exemplo prático para ilustrar:

        meu_dicionario = {"nome": "João", "idade": 25}

        # Acessando chaves
        chaves = meu_dicionario.keys()  # dict_keys(['nome', 'idade'])

        # Acessando valores
        valores = meu_dicionario.values()  # dict_values(['João', 25])

        # Acessando itens
        itens = meu_dicionario.items()  # dict_items([('nome', 'João'), ('idade', 25)])

2) Acesso aos valores: Você pode acessar os valores usando as chaves correspondentes
    print(meu_dicionario["nome"])  # Saída: João

3) Modificação: É possível adicionar, modificar ou remover pares de chave-valor:
    meu_dicionario["idade"] = 26  # Modifica o valor da chave "idade"
    meu_dicionario["profissão"] = "Engenheiro"  # Adiciona um novo par chave-valor
    del meu_dicionario["cidade"]  # Remove o par chave-valor com a chave "cidade"       

4) Métodos úteis: Dicionários possuem vários métodos úteis, como keys(), values(), e items():
    chaves = meu_dicionario.keys()  # Retorna todas as chaves
    valores = meu_dicionario.values()  # Retorna todos os valores
    itens = meu_dicionario.items()  # Retorna todos os pares chave-valor
5) Iteração: Você pode iterar sobre os pares chave-valor usando um loop for
    for chave, valor in meu_dicionario.items():
    print(f"{chave}: {valor}")

    enumerate com dicionários em Python, mas o comportamento pode não ser o que você espera. 
    A função enumerate é projetada para funcionar com sequências (como listas e tuplas), fornecendo um contador automático para cada item da sequência. Quando usada com dicionários, enumerate irá iterar sobre as chaves do dicionário, não sobre os pares chave-valor.

        Exemplo
        Python

        meu_dicionario = {'a': 1, 'b': 2, 'c': 3}

        # Usando enumerate com dicionário
        for indice, chave in enumerate(meu_dicionario):
            print(indice, chave, meu_dicionario[chave])
        Código gerado por IA. Examine e use com cuidado. Mais informações em perguntas frequentes.
        Saída
        0 a 1
        1 b 2
        2 c 3

        Explicação
        enumerate(meu_dicionario): Itera sobre as chaves do dicionário, não sobre os pares chave-valor.
        indice: O índice gerado pelo enumerate.
        chave: A chave do dicionário.
        Alternativa para Iterar sobre Pares Chave-Valor
        Se você quiser iterar sobre os pares chave-valor com índices, pode combinar enumerate com o método items() do dicionário:

        Python

        meu_dicionario = {'a': 1, 'b': 2, 'c': 3}

        # Usando enumerate com items() para iterar sobre pares chave-valor
        for indice, (chave, valor) in enumerate(meu_dicionario.items()):
            print(indice, chave, valor)
        Código gerado por IA. Examine e use com cuidado. Mais informações em perguntas frequentes.
        Saída
        0 a 1
        1 b 2
        2 c 3

        Explicação
        meu_dicionario.items(): Retorna uma visão dos pares chave-valor do dicionário.
        enumerate(meu_dicionario.items()): Itera sobre os pares chave-valor com índices.
        Dessa forma, você pode acessar tanto o índice quanto os pares chave-valor do dicionário1.
"""

# reisão rápida:

'''
    como iniciar estruturas compostas:
        1- tupla:
            tupla = tuple() ou tupla = ()
        2- listas:
            lista = list() ou lista = []
        3- dicionário:
            dicionario = dict() ou dicionario = {}


'''
'''
    ONDE APLICAR CADA UMA DAS LISTAS COMPOSTAS APRENDIDAS ATÉ O MOMENTO?
        SEGUE EM RESPOSTA:
            Vamos ver alguns exemplos práticos de como tuplas, listas e dicionários podem ser usados em Python:
            Tuplas
            Tuplas são usadas quando você tem um conjunto de valores que não devem ser alterados. Elas são imutáveis.

            Exemplo 1: Coordenadas Geográficas


            coordenadas = (23.5505, 46.6333)  # Latitude e Longitude de São Paulo
            print(f"Latitude: {coordenadas[0]}, Longitude: {coordenadas[1]}")
            Código gerado por IA. Examine e use com cuidado. Mais informações em perguntas frequentes.
            Exemplo 2: Dados de um Produto

            Python

            produto = ("Notebook", 1500.00, "Eletrônicos")
            print(f"Produto: {produto[0]}, Preço: R${produto[1]}, Categoria: {produto[2]}")
            Código gerado por IA. Examine e use com cuidado. Mais informações em perguntas frequentes.
            Listas
            Listas são usadas para armazenar uma coleção de itens que podem ser modificados. Elas são mutáveis.

            Exemplo 1: Lista de Compras

            Python

            lista_compras = ["maçã", "banana", "leite"]
            lista_compras.append("pão")  # Adiciona "pão" à lista
            print(lista_compras)
            Código gerado por IA. Examine e use com cuidado. Mais informações em perguntas frequentes.
            Exemplo 2: Notas dos Alunos

            Python

            notas = [7.5, 8.0, 9.2, 6.8]
            media = sum(notas) / len(notas)
            print(f"Média das notas: {media}")
            Código gerado por IA. Examine e use com cuidado. Mais informações em perguntas frequentes.
            Dicionários
            Dicionários são usados para armazenar pares de chave-valor. Eles são mutáveis e permitem acesso rápido aos valores através das chaves.

            Exemplo 1: Informações de um Aluno

            Python

            aluno = {"nome": "Ana", "idade": 22, "curso": "Engenharia"}
            print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Curso: {aluno['curso']}")
            Código gerado por IA. Examine e use com cuidado. Mais informações em perguntas frequentes.
            Exemplo 2: Contagem de Palavras em um Texto

            Python

            texto = "Python é uma linguagem de programação. Python é popular."
            palavras = texto.split()
            contagem = {}

            for palavra in palavras:
                if palavra in contagem:
                    contagem[palavra] += 1
                else:
                    contagem[palavra] = 1

            print(contagem)


'''


# exemplos de uso:

# pessoas = dict()
pessoas = {'nome': 'gustavo', 'sexo': 'M', 'idade': 22}
# printando o dicionário todo, ou seja, todos os itens(chaves-valor)
print(pessoas)
# printando apenas o par chave valor da idade
print(pessoas['idade'])
# printando apenas o valor da chave sexo
print(pessoas['sexo'])
# repare que para não dar erro precisei colocar nomes e idade entre aspas duplas, isto porque estamos dentro de um print.
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
# printando as chaves do dicionário
print(pessoas.keys())
# printando os valores do dicionário
print(pessoas.values())
# printando os itens do dicionário
print(pessoas.items())
# iterando sobre os itens do dicionário
for chave, valor in pessoas.items():
    print(f'{chave}:{valor}')

# apagando o elemento 'sexo'
del pessoas['sexo']
print('=-'*20)
# alterando o valor do elemento
pessoas['nome'] = 'LEANDRO'
pessoas['peso'] = 98.5


for chave, valor in pessoas.items():
    print(f'{chave}:{valor}')

# dicionário dentro de uma lista
brasil = []
estado1 = {'uf': 'rio de janeiro', 'sigla': 'rj'}
estado2 = {'uf': 'são paulo', 'sigla': 'sp'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0]['uf'])
print(brasil[0]['sigla'])


estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('UNIDADE FEDERATIVA: '))
    estado['sigla'] = str(input(f'SIGLA DO {estado["uf"]}: '))

    # em listas para quefizemos uma cópia de um conteúdo fazíamos assim > brasil.append(estado[:]), porém em python não é possível.
    brasil.append(estado.copy())

# printa a lista toda
print(brasil)

# printa cada item da lista brasil, ou seja, cada dicionário
for estado in brasil:
    print(estado)

for estado in brasil:
    for key, values in estado.items():
        print(f'O campo {key} tem valor {values}.')

for estado in brasil:
    for k in estado.values():
        print(k)
