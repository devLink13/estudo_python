# FUNÇÃO ISISTANCE() ÚTIL PARA VERIFICAR TIPOS

# Lista com 10 índices de diferentes tipos
lista = [1, 2.0, True, [1, 2], (3, 4), "string", 5, 6.7, False, ["a", "b"]]

for item in lista:
    print(item)

    if isinstance(item, bool):
        print(item, 'booleano')
    elif isinstance(item, int):
        print(item, 'inteiro')
    elif isinstance(item, float):
        print(item, 'float')
    elif isinstance(item, str):
        print(item, 'string')
    elif isinstance(item, list):
        print(item, 'lista')
    elif isinstance(item, tuple):
        print(item, 'tupla')
    
    print()

# ATENÇÃO: 
'''
    EM PYTHON OS BOOLEANOS SÃO UMA SUBCLASSE DOS INTEIROS
    LOGO, SE TESTARMOS UM BOOLEANO COMO INTEIRO ELE IRÁ RETORNAR TRUE
    CUIDADO AO USAR ESSAS VERIFICAÇÕES...
'''

# essa é uma forma muito válida de verificar o tipo do dado
print(type(5) == int)
print(type(5.5) == int or type(5.5) == float) # verificar se o dado é numero
