#conversaõ de tipos de dados, também chamado de coerção

'''
--> tipos imutáveis e primitivos:
    str, int, float e bool


'''

# polimorfismo usando o operador +
print(1+1) #soma usando +
print('a' + 'b') #concatenação de strings usando o operador +

# print('a' + 1) # isso gera um erro, pois estamos tentando concatenar tipos diferentes de dados
print(1 + int('1'))
print(11)

#converter um inteiro para um float
print(type(float(1)+1)) #repare que irá ocorrer a soma e o resultado final será do tipo float
print(float('2.25') + 2) #str para float

#int para str
print(str(11) + 'b')


