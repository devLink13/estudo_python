# criar um programa que analisa uma frase digitada no teclado
# que conte quantas letras 'a' foram digitadas e em quais posições
# ela apareceu a primeira vez e a ultima vez

dgt = str(input('digite uma frase: ')).strip().lower()
print('a letra "a" aparece {} vezes'.format(dgt.count('a')))
print('o "a" aparece a primeira vez na posição {} e a ultima vez na posição {}'.format(
    # o método .rfind('x') procura pela direita
    dgt.find('a'), dgt.rfind('a')))
