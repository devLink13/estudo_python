# imput é uma função que permite solicitar a um usuário uma inserção de dados via teclado.

# nome = input('digite seu nome: ')
# print(f'O nome do usuário é {nome}.')

# a inserção de dados é um ponto e elemento crucial para um software, pois é neste momento que podem ocorrer
# diversas vulnerabilidades e erros, veja:

# numero1 = input('digite um numero: ')
# numero2 = input('digite um numero: ')
# #irei forcar um erro de concatenação:
# print(f'a soma dos numeros é {numero1 + numero2}') #ocorrerá a concatenação dos valores e não a soma

# uma forma de acabar com o problema da concatenação é a conversão do valor de str para int logo na verificação
# porém isso pode gerar um erro caso o usuário não digite um numero.
# numero1 = int(input('digite um numero: '))
# numero2 = int(input('digite um numero: '))

# soma = numero1 + numero2

# print(f'a soma vale {soma}.')

#verificação simples

while True:

    numero1 = input('digite um numero: ')
    numero2 = input('digite um numero: ')

    if numero1.isnumeric() and numero2.isnumeric():
        numero1_int = int(numero1)
        numero2_int = int(numero2)

        print(f'a soma dos numeros vale: {numero1_int + numero2_int}')
        break

    else:
        print('digite apenas numeros.')
        
