# desenvolver um programa que faça uma análise de crédito para financiamento imobiliário

"""
solicitações:

-solicitar o nome completo
-cpf
-salário atual
-valor do imóvel desejado
-quantidade de anos para financiamento

requisitos:

1. converter anos para meses
2. informar se o crédito está ou disponível (valor da parcela não pode exceder 30% do salário)
3. informar valor de parcela
4. informar quantas parcelas


"""
# dados de entrada

nome = str(input('digite seu nome completo: ')).strip().upper()
cpf = int(input('digite seu cpf: '))
# verificar validade do cpf
# o cpf precisa ter 11 digitos
cpf = str(cpf)
if len(cpf) < 11:
    print('CPF INVÁLIDO, digite novamente seu cpf.')
    # print(type(cpf))
    # print(len(cpf)+1)

salario = float(input('digite sua renda mensal: '))
valor_imovel = int(input('digite o valor do imóvel: '))
anos = int(input('você deseja pagar em quantos anos? '))


# cálculos
meses = anos*12
parcela = valor_imovel/meses
margem = salario*0.3
print(parcela, margem)

if margem >= parcela:
    print('\033[1;32;40mseu crédito foi aprovado\033[m')
else:
    print('\033[1;31mcrédito negado\033[m')
