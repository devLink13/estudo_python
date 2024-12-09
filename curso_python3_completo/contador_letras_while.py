# fazer um programa que conte qual letra apareceu mais vezes numa frase
# utilizando o laço while e sem usar funções embutidas


frase = """O Python é uma linguagem de programação
multiparadigma. Python foi criado por
Guido van Rossum."""


tamanho_frase = len(frase)
contagem_letras = 0
maior_numero_letras = 0
letra_mais_apareceu = ''
nova_frase = frase


contador = 0
while contador < tamanho_frase:
    letra_atual = frase[contador]

    if letra_atual == ' ':
        #print('achei um espaço')
        contador += 1
        continue

    while letra_atual in nova_frase:
        contagem_letras += 1
        #print(letra_atual, contagem_letras)
        # remove a letra atual da frase na primeira aparição dela
        nova_frase = nova_frase.replace(letra_atual, '', 1)
        #print(nova_frase)

    if contagem_letras > maior_numero_letras:
        letra_mais_apareceu = letra_atual
        maior_numero_letras = contagem_letras

        contagem_letras = 0

    else:
        contagem_letras = 0

    contador += 1


print(f'A LETRA QUE MAIS APARECEU NA FRASE FOI: {
      letra_mais_apareceu}, COM NÚMERO DE REPETIÇÕES IGUAL A: {maior_numero_letras}')
