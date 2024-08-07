# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    
    """
    fat = 1

    if show == False:
        for n in range(num, 0, -1):
            fat = n * fat
        return fat

    elif show == True:
        for n in range(num, 0, -1):
            if n != 0 and n != num:
                print(' x ', end='')
            fat = n * fat
            print(n, end='')

            if n == 1:
                print(f' = {fat}')


print(fatorial(3, show=True))
