# RESUMO DE FUNÇÕES NO PYHTON

"""
Funções são usadas para tratar o uso de trechos repetitivos de códigos, ou seja, de rotinas de escrita,
por exemplo: toda hora precisamos printar algo na tela para que possamos visualizar um resultado ou então 
testar o código, porém, o comando print que realizamos é uma função. uma função nativa do python.

todo comando que tiver no seu final '()' é uma função, exemplos:

- print(), len(), int(), list(), e muito mais.

- podemos ter funções próprias criadas por nós mesmos, para tal usamos o comando 'def', isto é, def de definição
de função

def minha_função():
    faça isso e aquilo

- lembramos que: todas as def's criadas não executadas por padrão caso não sejam chamadas, existem áreas de código que chamamos de programa principal
e existe a área destinada ao programa da def, somente é executado uma def quando a mesma for chamada no programa principal, realizar-se-á um desvio condicional
no programa principal.


"""

# trecho repetitivo dem código, percebemos que o print das linhas ocorrem varias vezes.

print('-'*30)
print('HOLA, ESTOU TESTANDO DEFS')
print('-'*30)

print('-'*30)
print('outro titulo')
print('-'*30)

print('-'*30)
print('MAIS UM TITULO')
print('-'*30)


def linha():
    print('-'*30)

# todo vez que chamarmos a função linha, haverá um desvio condicional que executará a def linha()


# repare também que há uma estrutura repetida, ou seja, linha, depois o print com o titulo, depois linha de novo
# ou seja, podemos realizar uma função novamente para simplificar isso ainda mais.
linha()
print('HOLA, ESTOU TESTANDO DEFS')
linha()

linha()
print('outro titulo')
linha()

linha()
print('MAIS UM TITULO')
linha()


# função titulo
# todo conteúdo entre parenteses de def chama-se 'parâmetros', eles são utilizados pela função
# lêmos: a função titulo recebe o parametro 'titulo', para usar a função titulos, devemos 'passar' o parametro de titulo

def titulo(titulo):
    print('-'*30)
    print(titulo)
    print('-'*30)


titulo('TITULO FORMATADO')
titulo('MAIS UM TITULO AUTOMÁTICO')
titulo('oi')


# funções podem receber mais de um parâmetro

def somar(a, b):
    soma = a + b
    print(soma)


# some 2 e 4 para mim e print.
somar(2, 4)
# some 8 e 8 e print
somar(8, 8)

# posso explicitar o 'a' e o 'b'
# se eu explicitar os parametros, preciso explicitar todos os parâmetros
# não posso usar assim: somar(a=9, 8) ou então, somar(9, b=9)
somar(a=80, b=85)

# nunca posso passar mais parâmetros do que a função aceita
# não posso: somar(2,4,5)


# DESEMPACOTAMENTO --> USADO QUANDO QUEREMOS PASSAR VARIOS VALORES, OU SEJA, NÃO CONHECEMOS A QUANTIDADE

'''
    para usar o desempacotamento usamos o '*' dentro dos parametros

        def contador (*num):
            faca coisas

'''

# função para somar todos os numeros passados como parâmetros


def somar_tudo(*num):
    soma = 0
    for n in num:
        soma = soma + n
    print(soma)


somar_tudo(0, 1, 2, 3)
somar_tudo(5, 10, 15)

# função que conta quantos parâmetros foram passados


def contador(*num):
    print(len(num))


contador(0, 3, 5, 6)


# função que recebe uma lista e dobra os valores  indice por indice:

def dobra_lista(lista):
    for i, v in enumerate(lista):
        lista[i] = v*2
    print(f'lista dobrada ficou {lista}')


lista_antiga = [2, 4, 5, 6]
dobra_lista(lista_antiga)
# repare que a lista_antiga fica agregada a lista, para que não tenha essa ligação precisamos passar apenas uma cópia
print(lista_antiga)

# passar uma cópia
lista_antiga2 = [3, 6, 9, 12]
dobra_lista(lista_antiga2[:])
print(lista_antiga2)
