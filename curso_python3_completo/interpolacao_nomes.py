# INTERPOLAR O NOME COM '*'

nome = input("digite seu nome: ")
digito_interpolacao = input("digite o digito de interpolacao: ")
tamanho_nome = len(nome)
nome_interpolado = ''

contador = 0
while contador < tamanho_nome:
	if nome[contador] == " ":
		nome_interpolado += nome[contador]
		contador += 1
		continue
	
	if contador < (tamanho_nome - 1):
		nome_interpolado += nome[contador] + digito_interpolacao
	elif contador == (tamanho_nome - 1):
		nome_interpolado += nome[contador]
		
	contador += 1
	
print(f"seu nome interpolado com o dígito '{digito_interpolacao}' fica: {nome_interpolado}.")
