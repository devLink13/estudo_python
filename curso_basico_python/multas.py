# programa que calcula uma multa de transito levando em consideração uma rodovia com velocidade de 80km/h
# R$07,00 de multa por km/h acima da velocidade

from random import randint

vel = randint(1, 200)
print(vel)
taxa = 7.00
valor_multa = 0.00


if vel > 80:
    print('você foi multado, calculando multa.')
    valor_multa = (vel-80)*taxa
    print('você foi multado em R${:.2f}'.format(valor_multa))
else:
    print('você está dentro do limite de velocidade!')
