# tirando uma dúvida de como poderia retirar espaços de dentro de uma string sem usar métodos

frase = 'testando a retirada de espaços da frase'
nova_frase = ''
for item in frase:
    if ' ' not in item:
        nova_frase += item

print(nova_frase)