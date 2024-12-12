"""
Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 

    ALGORITMO:
    1. LER IDADE ok
    2. LER SEXO ok
    3. PERGUNTAR SE QUER CONTINUAR O CADASTRO, [S - SIM / N - NÃO] ok
    4. EXIBIR QUANTAS PESSOAS TEM MAIS DE 18 ANOS ok
    5. EXIBIR QUANTOS HOMENS FORAM CADASTRADOS ok
    6. QUANTAS MULHERES TEM MENOS DE 20 ANOS OK


"""
cont_pessoas = 1
cont_maiores = 0
cont_homens = 0
cont_mulheres = 0

while True:
    print('='*20, f'CADASTRO DA PESSOA N°{cont_pessoas}', '='*20)

    idade = int(input('IDADE: '))
    if idade > 18:
        cont_maiores += 1

    sexo = str(input('SEXO [M - MASC. / F - FEM.]: ')).upper()
    if sexo == 'M':
        cont_homens += 1
    if sexo == 'F' and idade < 20:
        cont_mulheres += 1

    if input('CONTINUAR CADASTRO [S - SIM / N - NÃO]: ').upper() == 'N':
        break

    cont_pessoas += 1


print('='*20, 'ESTATISTICAS DO CADASTRO', '='*20)
print(f'N° DE PESSOAS COM MAIS DE 20 ANOS: {cont_maiores}')
print(f'HOMENS CADASTRADOS: {cont_homens}')
print(f'N° DE MULHERES COM MENOS DE 20 ANOS: {cont_mulheres}')
