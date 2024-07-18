# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = list()
caract = list()
par_abertos = list()
par_fechados = list()

expressao = input('digite uma expressão para conferir sua validade: ')

exp = list(expressao)

pos = 0
while pos < len(exp):
    if exp[pos] == '(':
        par_abertos.append(exp[pos])
    elif exp[pos] == ')':
        par_fechados.append(exp[pos])
    else:
        caract.append(exp[pos])
    pos = pos + 1

if len(par_abertos) == len(par_fechados):
    print('expressão válida')

else:
    print('expressão inválida')
