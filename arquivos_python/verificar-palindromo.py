# desenvolver um verificador de palíndromo


# solicitar uma entrada de texto e aplicar o tratamento de strings
frase = str(input('digite uma frase: ')).upper().strip()
frase_dividida = frase.split()
# print(frase_dividida)
frase_juntada = ''.join(frase_dividida)
# print(frase_juntada)

# iterar cada uma das letras da frase de trás para frente
# quantidade de iterações depende do tamanho da string, ou seja, do len(variave)
# print(len(frase_juntada))

inverso = ''
for c in range(len(frase_juntada) - 1, -1, -1):
    inverso = inverso + frase_juntada[c]

if inverso == frase_juntada:
    print('{} é igual a {}, logo isso é um palíndromo!'.format(
        frase_juntada, inverso))
else:
    print('{} é diferente de {}, logo não é palíndromo.'.format(
        frase_juntada, inverso))
