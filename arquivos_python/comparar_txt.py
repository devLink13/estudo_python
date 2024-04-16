# comparar um texto de entrada com algo prévio
# comparar nome de cidade que comece com "santo"

""" exerccicio 1

# usar o .strip() para retirar espaços
cidade = str(input('digite sua cidade: ')).strip()
# passar tudo para minúsculo
cidade = cidade.lower()
# definir o range da lista entre [0:5] pois é o tamanho para digitação de 'santo'
print(cidade[0:5] == "santo")

"""

# verificar se a pessoa tem "souza" no nome, não importa onde

nome = str(input('digite seu nome completo:')).strip()
print(nome.lower().find('silva') != -1)
