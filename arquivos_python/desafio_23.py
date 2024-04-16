# ler um numero entre 0 e 9999 e mostrar a unidade, dezena, centena e milhar.
'''
1. armazenar o numero
2. obter unidade
3. obter dezena
4. obter centena
5. obter milhar

'''


num = int(input('digite qualquer número inteiro entre 0 e 9999: '))
num_str = str(num)
print('''o número digitado é {} \n
         seu milhar é {} \n
         sua centena é {} \n
         sua dezena é {} \n
         sua unidade é {}'''.format(num, num_str[0], num_str[1], num_str[2], num_str[3]))
