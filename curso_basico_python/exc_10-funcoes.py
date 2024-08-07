# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

from time import sleep

cores = {'fundo_verde': '\033[0;30;42m',
         'fundo_azul': '\033[44m',
         'fundo_branco': '\033[47m',
         'remove_fundo': '\033[0m'
         }


# def ajuda(cmd):
#     print(f'{cores["fundo_azul"]}BUSCANDO A AJUDA DO COMANDO {
#           cmd}...{cores["remove_fundo"]}')
#     sleep(1)
#     print(cores['fundo_branco'])
#     help(cmd)
#     print(cores['remove_fundo'])

# # programa principal:


# while True:
#     print(f'{cores["fundo_verde"]}SISTEMA DE AJUDA PYHELP{
#           cores["remove_fundo"]}')
#     cmd = str(input('FUNÇÃO OU BIBLIOTECA: '))

#     if cmd.upper().strip() == 'SAIR':
#         break
#     else:
#         ajuda(cmd)

print(cores['fundo_verde'])
print('olá mundo')
