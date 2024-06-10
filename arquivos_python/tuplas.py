"""
TUPLAS SÃO VARIÁVEIS COMPOSTAS --> MAIS DE UMA VÁRIAVEL SIMPLES DECLARADA COM MESMO NOME

DECLARAÇÃO DE TUPLA --> nome_variavel = (elem1, elem2, elem3, ...)

    1. TUPLAS SÃO SEMPRE DECLARADAS USANDO PARÊNTESES
    2. PARA CHAMAR UMA TUPLA BASTA CHAMAR SEU NOME, EX: print(nome_variavel) ou então especificar o índice, ex: print(nome_variavel[0])
    3. Há a possibilidade de fazer fatiamento de tuplas da mesma forma que é feito com strings e texto.

    OBS> TUPLAS SÃO IMUTÁVEIS, ISTO É, NÃO É POSSÍVEL MODIFICAR O VALOR DE UMA TUPLA APÓS SUA CRIAÇÃO
    


"""
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
#              0           1        2        3

# mostrará toda tupla
print(lanche)
print('#'*20)

# mostrará o conteúdo da tupla no índice definido
print(lanche[0])
print('#'*20)

# mostrará a tupla com fatiamento da primeira, de x até o fim da tupla, ex:
print(lanche[1:])
print('#'*20)

# mostrará a tupla com fatiamento usando índice negativo, note que a sequência fica inversa
# se a tuplas possuir 20 indices, o índice -1 será o último e o índice -20 o primeiro
print(lanche[-1])
print(lanche[-4])
print('#'*20)

# mostrar um dado intervalo de indices na tupla, lembrando que no python o indice final é exclusivo, isto é, não é contado
# logo o índice definido como final será ele -1, exemplo, tupla = (num1, num2, num3), se eu chamar print(tupla[0:3]), ele não indicará o último valor

# MUITA ATENÇÃO AO USAR O ':' O VALOR FINAL É EXCLUSIVO, ENTÃO SE EU QUERO IR DE X A Y, LEMBRAR DE CONSIDERAR QUE ELE VAI ATÉ Y-1, ISSO ACONTECE ABAIXO

# print será hamburguer, suco, pizza
print(lanche[0:3])
# print será suco
print(lanche[1:2])
# print será pizza, pudim
print(lanche[2:])
# print será hamburguer, suco
print(lanche[:2])
# print será suco, pizza, pudim
print(lanche[-3:])
# print será hamburguer, suco
print(lanche[:-2])
print('#'*20)

#  uso de laço for com uma tupla
for comida in lanche:
    print(f'Eu vou comer {comida}')
    print(f'iteração atual é "{comida}"')
print('#'*20)

# uso de laço for com tuplas usando contador e range
for cont in range(0, len(lanche)):
    print(f'o lanche na posição {cont} é {lanche[cont]}')
print('#'*20)

# uso de enumerate para saber a posição iterando sobre a lista diretamente
for pos, comida in enumerate(lanche):
    print(f'a comida na posição {pos} é {lanche[pos]}')
print("#"*20)

# visualizando o tamanho de uma tupla
print(f'o tamanho da tupla é {len(lanche)}')

# usando o método sorted com tuplas para colocá-la em ordem
print(sorted(lanche))
print(lanche)

# concatenar tuplas
# lembrando que tuplas são imutáveis ou seja, não estamos alterando o valor das tuplas
# a ordem da soma muda a ordem da tupla de saída
a = (0, 2, 3, 5)
b = (2, 4, 5, 3)

c = a + b

print(c)
print('#'*20)

# agora a ordem de soma da tupla foi alterada, a saída se alterará também.
c = b + a
print(c)

# é possível usando métodos dentro da tupla
# count procura quantas correspondencias de '2' possui na tupla
print(c.count(2))

# em qual psoição está o elemento x?
print(c.index(0))

# é possível utilizar diversos tipos de dados em uma tupla
dado = ('Murilo', 24, 'Altura', 1.70)
print(dado)

# é possível deletar uma tupla
del (dado)
