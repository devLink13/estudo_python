# LER NOME COMPLETO DE UMA PESSOA
'''
1. mostrar tudo em maiusculo
2. mostrar tudo em minusculo
3. contar quantas letras tem desconsiderando os espaços
4. mostrar só o primeiro nome

'''

# usando o strip ele elimina os espaços desnecessários
nome_completo = str(input('digite seu nome completo: ')).strip()
print('nome em maiúsuclo: {}'.format(nome_completo.upper()))
print('nome em minúsculo: {}'.format(nome_completo.lower()))

# gerar uma nova lista split somente com os nomes e sem os espaços
nome_completo = nome_completo.split()
# print(len(nome_completo))
ultimo = nome_completo[len(nome_completo) - 1]
#print(ultimo)
primeiro = nome_completo[0]
# print(primeiro)
# juntar os nomes sem espaços para conseguir contar as letras
nome_completo = ''.join(nome_completo)
# print(nome_completo)
print('o seu nome possui {} letras'.format(len(primeiro)))
print('o seu primeiro nome é {}'.format(primeiro))
print('o seu ultimo nome é: {}'.format(ultimo))
