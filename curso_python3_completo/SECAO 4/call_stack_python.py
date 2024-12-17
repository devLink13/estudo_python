# entendo as chamadas de funções e a pilha do python
# chamada de callstack

"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
'''
    ordem da pilha de chamadas:

    #terceiro ponto de parada é 'outra_funcao'                      -> morre primeiro
    #segundo ponto de parada é o 'escopo'                           -> morre após
    #primeiro ponto de parada é o <module> call_stack_python.py     -> volta ao modulo
    

'''

x = 1


def escopo():
    #global x
    x = 10

    def outra_funcao():
        #global x
        x = 11 # no atual escopo
        y = 2 # no atual escopo
        print(x, y)

    outra_funcao()
    print(x) # 10 -> x do escopo atual


print(x) #printará 1 (escopo global)
escopo()
print(x)