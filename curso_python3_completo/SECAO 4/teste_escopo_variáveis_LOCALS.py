# função locals() retorna um dicionário com todas as variáveis locais

x = 10
y = 20

def printar():
    w = 1
    z = 2
    print(f'variáveis do escopo da função printar() : {locals()=}') # imprime um dicionário com todas as variáveis locais que seriam w e z

printar()
print('-'*100)
print(f'variáveis do escopo local que é o escopo global : {locals()=}') # imprime um dicionário com todas as variáveis locais que seriam x e y

if 'x' or 'y' in locals():
    print(locals()['x'], locals()['y']) # imprime o valor de x e y
else:
    print('x ou y não estão no escopo local')
