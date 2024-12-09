# tentando entender e trabalhar com os métodos __iter()__ e next

texto = iter('Luiz') # ou 'luiz'.__iter__
# texto = 'luiz'.__iter__()
print(f'{texto=}, {texto.__next__()=}') # veja que o iterator é um método da string e que next é o método do iterator
print(f'{texto=}, {texto.__next__()=}')
print(f'{texto=}, {texto.__next__()=}')
print(f'{texto=}, {texto.__next__()=}')