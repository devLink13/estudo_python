# introdução ao sqlite usando python e SQL
# é uma base de dados local que usa um arquivo

'''
    O SQLITE não é usado para receber muitas conexões ao mesmo tempo
    logo não deve-se usar o SQLITE para aplicações com várias conexões

'''

import sqlite3
from pathlib import Path

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = "CLIENTES"

connection = sqlite3.connect(DB_FILE)#
cursor = connection.cursor()

# CUIDADO: fazendo delete sem WHERE
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
connection.commit()


# limpar a primary key id, isso não é uma boa prática mas pode ser necessário
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)

# cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()  # sempre commitar após um comando

# registrar valores nas colunas
# se colocarmos input's direto no values podemos abrir chance pra tomar uma injeção de sql
cursor.execute(  # registrando um valor -> execute()
    f'INSERT INTO {TABLE_NAME} (id, name, weight) '
    'VALUES (NULL, "WESLEY LINK", 78.5), (NULL, "LAURA SMANIOTTO", 60.5)'
)
connection.commit()

# forma mais 'correta de inserir valores'
sql = (
    # "?"-> são chamados de bindings ou placeholders
    f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)'
)
# passar os valores de (?, ?) no comando execute OBS: pode ser tupla, lista ou qualquer iterável
cursor.execute(sql, ('LUCAS', 60))
connection.commit()

# usando o executemany
'''
    o executemany permite executar mais de um valor, passando um iterável com mais de um item dentro
'''
cursor.executemany(sql, [('CAMILA LUIZA', 55.6),
                   ('ALBERTO ROSA', 120.0), ('VAGNER AMARAL', 78.5)])
connection.commit()

# usando dicionários para passar os valores dos bindings
sql = (
    # precisa ser o mesmo nome da chave do dicionário
    f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (:nome, :peso)'
)

cursor.execute(sql, {'nome': "JOSÉ ALENCAR", 'peso': 200.45})
connection.commit()

#  usando executemany com dicionários, podemos usar um iterável com dicionários, como por exemplo uma lista de dicionários
cursor.executemany(sql, (
    {'nome': "maria amada", 'peso': 500},
    {'nome': "maria madalena", 'peso': 500},
    {'nome': "maria de jesus", 'peso': 500},
    {'nome': "maria betania", 'peso': 500}
))
connection.commit()

cursor.close()
connection.close()
