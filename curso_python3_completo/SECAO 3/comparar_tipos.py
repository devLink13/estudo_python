# RETIRANDO UMA DUVIDA: É POSSÍVEL COMPARAR TIPOS?

inteiro = 123
flutuante = 12.3
booleano = True
string = 'frase'

# percebe-se que funciona a comparação direta usando is
print(type(inteiro) is int) # true
print(type(inteiro) is not  float) # true
print(type(inteiro) is float) # false

# usando o operador de comparação também funciona
print(type(booleano) == bool) #true
print(type(string) == str) # true

# se não usar a função type antes de comparar o programa não retorna true, veja
print(flutuante == float) #retornará false erroneamente
print(type(flutuante) == float) # true