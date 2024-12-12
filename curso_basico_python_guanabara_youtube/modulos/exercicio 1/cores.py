"""
    CRIAR UMA FUNÇAO QUE AUXILIE NO USO DE CORES NO PYTHON, CORES BASEADAS NO CODIGO ANSI

  
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



vermelho = '\033[31m'
verde = '\033[32m'
azul = '\033[34m'

ciano = '\033[36m'
magenta = '\033[35m'
amarelo = '\033[33m'
preto = '\033[30m'

branco = '\033[37m'

restaura cor original = '\033[m'
negrito = '\033[1m'
reverso = '\033[2m'

fundo preto = '\033[40m'
fundo vermelho = '\033[41m'
fundo verde = '\033[42m'
fundo amarelo = '\033[43m'
fundo azul = '\033[44m'
fundo magenta = '\033[45m'
fundo ciano = '\033[46m'
fundo branco = '\033[47m'

"""


def cores(nome=None, negrito=False, sublinhado=False):
    """
        FUNÇÃO PARA USO DE CORES NO TERMINAL PYTHON UTILIZANDO-SE DO PADRÃO ANSI

        INSTRUÇÕES:
            #param nome: recebe a cor do texto, ex: 'amarelo', 'azul', 'verde' e etc.#
                'vermelho'
                'verde'
                'azul'
                'ciano'
                'magenta'
                'amarelo'
                'preto':
                'branco'
                'padrao'
            #param negrito: pode receber true ou false, por padrão é false, serve para colocar o texto em negrito#
            #param sublinado: pode receber true ou false, por padrão é false, serve para colocar o texto em sublinado.#
            #return: retorna o código da cor, que modificará o texto no print.

    """
    cor = nome.lower().strip()
    cod = str
    estilo = '0;'

    if negrito == False or sublinhado == False:
        estilo = '0;'

    if negrito == True or sublinhado == True:
        if negrito == True:
            estilo = '1;'
        elif sublinhado == True:
            estilo = '4;'
    if negrito == True and sublinhado == True:
        estilo = '1;4;'

    cores = {
        'vermelho': '31',
        'verde': '32',
        'azul': '34',
        'ciano': '36',
        'magenta': '35',
        'amarelo': '33',
        'preto': '30',
        'branco': '37',
        'padrao': ''
    }

    if cor in cores.keys():
        cod = cores[cor]

        if estilo == '0;':
            cod = '\033['+cod+'m'

        elif estilo == '1;':
            cod = '\033['+estilo+cod+'m'

        elif estilo == '4;':
            cod = '\033['+estilo+cod+'m'

        elif estilo == '1;4;':
            cod = '\033['+estilo+cod+'m'

        return cod

    else:
        return '\033[31mERROR_cor_not_found\033[m'
