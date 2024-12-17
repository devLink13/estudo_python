# função globals() retorna um dicionário com as variáveis globais

b = 20

def calcular(x,y):
    soma = x + y
    print(soma)
    c = soma
    print(globals()) # retorna um dicionário com as variáveis globais onde só teremos o b = 20

dicionario_globals = dict(globals())
for chave, valor in dicionario_globals.items():
    print(f'{chave} = {valor}')