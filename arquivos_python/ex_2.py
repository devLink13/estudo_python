n = input('digite algo:')
print(type(n))  # verifica o tipo de variável

# método 'is' é usado para testar tipos e dados de variáveis, variável.is+algo()
print('ele é letra?', n.isalpha())
print('ele é número?', n.isnumeric())
print('ele é alfanumérico?', n.isalnum())
print('ele está em maiúsculo?', n.isupper())
print('ele está em minusculo?', n.islower())
print('ele é decimal?', n.isdecimal())
