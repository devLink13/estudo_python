# treinando e testando o uso de marcadores em python
"""
    embora os marcadores estejam em desuso ainda podem ser encontrados em códigos antigos 
    ou em códigos que se deseje compatibilidade, uma vez que funcionam em todas versões do python

"""

x = 50	
txt = "Joao tem %d anos" % x
print(txt)

nome = "wesley"
txt = "meu nome é %s" % nome
print(txt)

num = 5.5
txt = "o número vale %f" % num
print(txt)


# PODEMOS FORMATAR OS MARCADORES
numero = 12
txt = "o número é: [%04d]" % numero
print(txt)

#sem zeros à esquerda
txt = "o numero é: [%4d]" % numero
print(txt)

valor = 50.5
txt = "o custo é de R$%4.2f" % valor #primeiro numero representa a quantidade de digitos e o numero após o ponto significa quantia de casas decimais
print(txt)

valor = 50
txt = "o custo é de R$%6.2f" % valor 
print(txt)

valor = 50.5
txt = "o custo é de R$ %8.4f" % valor
print(txt)

#combinação de várias composições em uma 

nome = "wesley"
idade = 24
saldo = 230.58

txt = "O nome do indivíduo é %s, que possui %d anos de idade e no seu saldo é R$%4.2f" % (nome, idade, saldo)
print(txt)
