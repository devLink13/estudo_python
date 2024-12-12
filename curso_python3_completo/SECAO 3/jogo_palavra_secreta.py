#Faça um jogo para o usuário adivinhar qual a palavra secreta. 
# Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra. 
# Quando o usuário digitar uma letra, você deve conferir se a letra está na palavra secreta. 
# Se a letra  estiver na palavra então exiba a letra, se não estiver exiba um *. Faça a contagem de tentativas do usuário.

import os

def limpar_terminal():
    os.system('cls')

palavra_secreta = 'perfume'.lower()
tamanho_palavra = len(palavra_secreta)
palavra_secreta_oculta = ''
n_tentativas = 1


for letra in palavra_secreta:
    letra = '*'
    palavra_secreta_oculta += letra


print(f'BEM VINDO AO JOGO DA PALAVRA SECRETA.')
print(f'A PALAVRA SECRETA POSSUI {tamanho_palavra} LETRAS, VEJA: {palavra_secreta_oculta}')

while True:
    letra_digitada = input(f'{n_tentativas}° tentativa, digite uma letra: ').lower()

    if len(letra_digitada) > 1:
        print('digite apenas uma letra.')
        continue
 
    if letra_digitada in palavra_secreta: # verifica se a letra digitada está na palavra secreta

        for c in range(tamanho_palavra): # preciso saber em qual indice está esta letra
            if letra_digitada == palavra_secreta[c]:
                indice_letra = c
                
                palavra_secreta_oculta = palavra_secreta_oculta[: indice_letra] + letra_digitada + palavra_secreta_oculta[indice_letra + 1 :]
                # print(palavra_secreta_oculta)
            
            else:
                continue
        
        print(f'PALAVRA SECRETA: {palavra_secreta_oculta}')
    
    else:
        print(f'A LETRA "{letra_digitada}" NÃO FAZ PARTE DA PALAVRA SECRETA')
    
    if palavra_secreta_oculta == palavra_secreta:
        limpar_terminal()
        print(f'PARABÉNS, VOCÊ ADVINHOU A PALAVRA SECRETA, ELA É: {palavra_secreta_oculta}')
        print(f'VOCÊ PRECISOU DE {n_tentativas} TENTATIVAS PARA ADVINHAR')
        break
    
    n_tentativas += 1
