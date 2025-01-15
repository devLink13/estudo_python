import sqlite3
from primeiro_arquivo_sqlite import DB_FILE, TABLE_NAME


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')
for row in cursor.fetchall():
    print(row) # printa cada linha
    name = row[1]
    print(name)

# limitando a seleção a 2 registros
cursor.execute(f'SELECT * FROM {TABLE_NAME} LIMIT 2')
for row in cursor.fetchall():
    print(row)

cursor.execute(f'SELECT * FROM {TABLE_NAME} WHERE id = 5')
row = cursor.fetchone()
print(row)

# CRUD --> CREATE READ   UPDATE DELETE
# SQL -->  INSERT SELECT UPDATE DELETE

# delete
cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"')
connection.commit()

cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = 5')
connection.commit()

print()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')
for linha in cursor.fetchall():
    print(linha)
connection.commit()

print()

cursor.execute(f'UPDATE {TABLE_NAME} SET weight = 60, name = "CAMILA LUIZA SOUZA" WHERE id = 4')
connection.commit()

cursor.close()
connection.close()