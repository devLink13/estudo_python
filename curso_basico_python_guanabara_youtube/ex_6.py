# desenvolverei uma calculadora de triângulos retângulos com todas informaços matemáticas pertinentes


# h²=ca²+co²
# preciso de sqrt
# preciso de cos
# preciso de sen
# preciso de tan
# preciso converter de rad para graus

import math

ca = float(input('digite o valor do cateto adjascente: '))
co = float(input('digite o valor do cateto oposto: '))

hip = math.pow(ca, 2)+math.pow(co, 2)
hip = math.sqrt(hip)

# print('o valor da hipotenusa é {}'.format(hip))

# cos ang =ca/hip
# sen ang =co/hip

cos_ang = ca/hip
sen_ang = co/hip
# print(cos_ang, sen_ang)

# fazemos os dois calculos de conversão, deve dar o mesmo ang. printamos o valor para confirmar
ang_rad = math.acos(cos_ang)
ang_grau = math.asin(sen_ang)
# print(ang_rad, ang_grau)

ang_grau = math.degrees(ang_rad)
# print(ang_rad, ang_grau)


print('O triângulo retângulo de cateto adjascente {} e de cateto oposto {} gera uma hipotenusa de valor {}\n cujo ângulo é {:.1f} em graus e {:.2f} em radianos \n e seu cosseno vale {} e o seu seno vale {}'.format(
    ca, co, hip, ang_grau, ang_rad, cos_ang, sen_ang))
