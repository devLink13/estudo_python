# gerar uma tupla com 5 numeros inteiros aleatórios
# mostrar a tupla
# indicar o menor e maior valor

from random import randint
from time import sleep
import keyboard

while True:
    numeros = tuple(randint(1, 5) for _ in range(5))

    print(f'a tupla gerada foi {numeros}')
    print(f'o menor número da tupla é {min(numeros)}')
    print(f'o maior número da tupla é {max(numeros)}')
    print('-'*80)
    sleep(0.5)

    if keyboard.is_pressed('s'):
        print('interrupção por teclado.')
        break
