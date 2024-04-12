# comentários em python se usa o 'hashtag'


nome = 'wesley'
print('olá', nome)
print('----------------------')

nome2 = input('qual seu nome?')
# os {} permitem fazer uma formatação de um espaço dentro de um print, usando o .format(o que quiser formatar)
print('olá {} seja bem vindo ao python'.format(nome2))

print('------------------')
print('agora vamos fazer uma calculadora')


# antes de um input é necessário definir o tipo de várial que irá ser recebido em num1, por exemplo do tipo inteira
# pois caso contrário, irá apenas armazenar um tipo string, que na hora da soma irá apenas concatenar as variáveis.

# exemplo: usando type, podemos verificar o tipo da variável
num1 = input('digite um número: ')
print(type(num1))
# verificando no terminal, percebemos que o tipo primitivo da variável é 'STR' --> string
num1 = int(input('digite um número: '))
print(type(num1))
# verificando no terminal agora podemos notar que o tipo é inteiro, pois forçamos a isso definindo o tipo de variável anteriormente
# essa é uma forma de forçar a conversão de tipos de variáveis, colocando o tipo da variável antes do input, nos forçamos a conversão dessa variável


num1 = int(input('digite um número: '))
num2 = int(input('digite outro número: '))
soma = num1+num2
print('você digitou {} e {}, vamos somar.'.format(num1, num2))
print('a soma entre os números vale {}'.format(soma))
