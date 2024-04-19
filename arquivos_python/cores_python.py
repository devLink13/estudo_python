# como utilizar cores na formatação de textos do terminal do python
# usando a tabela ansi

"""

estrutura de codigo -> \033[x; yy ;zz m

x -> style (formatação do texto) 0,1,4 ou 7
yy -> cor do texto vai do 30 ao 37
zz -> fundo do texto vai de 40 a 47k

    text                background
 

30      black       preto          40
31      red         vermelho       41
32      green       verde          42
33      yellow      amarelo        43
34      blue        azul           44
35      Magenta     Magenta        45
36      cyan        ciano          46
37      grey        cinza          47
97      white       branco         107


style

0 none
1 bold
4 underline
7 negative


"""

# usar o \033[m no final para finalizar a formatação
# print('\033[4;31;43m estou aprendendo a formartar o texto\033[m \ngostaram?')

print('\033[7;34;45m-=\033[m'*30)
print('---------bem vindos ao programa de edição de cores!---------')

nome = str(input('digite seu nome completo:')).strip()
print('seu nome completo é: \033[4;35m{}\033[m'.format(nome))

cpf = int(input('digite seu cpf: '))
print('seu cpf é: \033[4;35m{}\033[m'.format(cpf))

cep = int(input('digite seu cep:'))
print('seu cep é: \033[4;35m{}\033[m'.format(cep))
