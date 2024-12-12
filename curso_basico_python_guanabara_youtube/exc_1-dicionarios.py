# Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.


info = dict()
cor_verde = '\033[32m'
cor_vermelho = '\033[31m'
cor_reset = '\033[m'

info['nome'] = str(input('NOME DO ALUNO: ')).strip().upper()
info['media'] = float(input('INFORME A MÉDIA DO ALUNO: '))


print(f'O ALUNO {info["nome"]}, POSSUI MÉDIA {
      info["media"]}, logo está: ', end='')

if info['media'] >= 6:
    info['situacao'] = 'APROVADO'
    print(f'{cor_verde}APROVADO !{cor_reset}')

else:
    info['situacao'] = 'REPROVADO'
    print(f'{cor_vermelho}REPROVADO !{cor_reset}')

print(info)
