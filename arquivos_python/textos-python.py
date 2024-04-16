# trabalhando com formatação de textos

# lista contendo uma string que vai de 0 a 27 onde cada caracter ocupada um lugar na lista
frase = 'link esta aprendendo python'
#      ---------------------------    28 caracteres dentro dessa string, indo de 0 a 27
#  len(variavel) mede o tamanho da variável
"""
print(len(frase))
print(len('link está aprendendo python'))
"""
print(frase[0])  # retorna L
print(frase[0:2])  # retorna l [1] e i[2]
# retorna do caracter 0 ao 09 (fim-1, ou seja, 10-1= 9), se eu quisesse do 0 ao 10, teria que 0:11:2
print(frase[0:10:2])
# printa do inicio ao 28
print(frase[:28])
# printa do zero ao fim
print(frase[0:])
# printa do zero ao fim pulando de 2 em 2
print(frase[0::2])
# conta quantas vezes aparece o caractere
print(frase.count('e'))
# joga todos os caracteres em maiúsculo
print(frase.upper())
# joga os caracteres para maisculo e depois conta quantos A maisculos tem, pode incluir um médo n'outro
print(frase.upper().count('A'))
# colocando espaços para retira-los
print(len('         link esta aprendendo python        '))
# strip retira os espaços antes e depois da string
print(len(frase.strip()))
# rstrip() retira espaços a direita e lstrip() retira espaços a esquerda
frase = '      link esta aprendendo python      '
print(frase.rstrip())
print(frase.lstrip())
# replace é usado para substituir
print(frase.replace('link', 'joão'))

# lembrar que uma lista é imutável, ou seja, replace não altera o valor da lista
# para mudar é necessário atribuir o valor de frase à replace, veja:

frase.replace('link', 'jão')
print(frase)  # ele printa 'link esta aprendendo python' em vez de joão

frase = frase.replace('link', 'joao')
print(frase)

# find retorna a posição de determinada busca
frase = 'link esta aprendendo python'
print(frase.find('link'))
print(frase.find('esta'))

frase = frase.upper()
print(frase)
# ao procurar 'link' ele retornará -1 (não encontrado), pois estamos procurando por link em minusculo
print(frase.find('link'))
# aqui ele retorna a posição de inicio pois é maisculo
print(frase.find('LINK'))
# passar para minusculo e procurar python sem mexer na frase
print(frase.lower().find('python'))

# o comando split() gera uma particão na frase, gerando listas da frase, sempre que houver um espaço há uma divisão
frase = frase.split()
print(frase)  # mostra uma nova lista
print(len(frase))
print(frase[1])  # escreve o que está na posição [1] da lista
print(frase[3])  # escreve o que está na posição [3] da lista
# escreve o que está na posição [1] e o seu caracter da posição [0]
print(frase[1][0])

# usando o método 'algo'.join(lista_x) podemos juntar as coisas
frase = '-'.join(frase)
print(frase)

# outro exemplo
carro = ['roda', 'motor', 'freios']
conjunto = []
conjunto = ' '.join(carro)
print(conjunto)
