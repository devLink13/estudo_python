pessoa = {
    'nome': 'wesley',
    'sobrenome': 'link',
    'idade': 24,
    'peso': 80.00,
}
for item in pessoa:
    print(item, pessoa[item])

print()

for item, valor in pessoa.items():
    print(item, valor)
print()    

pessoa_2 = {**pessoa, 'nome':'maria'}
print(pessoa_2)