# Escreva um programa que crie uma matriz aleatória de 3x3 utilizando a biblioteca NumPy
# e, em seguida, imprima a matriz transposta.

import numpy as np

matriz = np.random.randint(0, 50, size=(3, 3))
print(matriz)

print()

matriz_transposta = np.transpose(matriz)
print(matriz_transposta)
