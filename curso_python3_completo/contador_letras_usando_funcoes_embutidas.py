# fazer um programa que conte qual letra apareceu mais vezes numa frase
# utilizando o laço while usando a função embutida count

#vamos usar a função count()

frase = """O Python é uma linguagem de programação
multiparadigma. Python foi criado por
Guido van Rossum."""

# frase = 'aaabbbbccccc'
frase = frase.replace(" ", "") # uma forma de retirar os espaços em brancos antes, no meio e depois da frase, iterando apenas em letras

tamanho_frase = len(frase)
maior_numero_letras = 0
letra_que_mais_apareceu = ''


contador = 0
while contador < tamanho_frase:
    letra_atual = frase[contador]

    # if letra_atual == " ": # posso usar essa verificação para pular os espaços, ou usar o replace na frase.
    #     contador += 1
    #     continue

    contagem_letras = frase.count(letra_atual) # armazena o numero de repetições da letra atual dentro da frase

    if contador == 0:
        maior_numero_letras = contagem_letras

    elif contagem_letras > maior_numero_letras:
        maior_numero_letras = contagem_letras
        letra_que_mais_apareceu = letra_atual
    
    else:
        contagem_letras = 0

    contador += 1

print(f'A letra que mais apareceu na frase foi "{letra_que_mais_apareceu}" com {maior_numero_letras} repetições.')

