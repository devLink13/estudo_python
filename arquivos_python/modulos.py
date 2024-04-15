'''
PARA IMPORTAR BIBLIOTECAS OU MODULOS EM PYTHON USAR OS SEGUINTES PROCEDIMENTOS

import biblioteca  -> aqui ele importa tudo da biblioteca
from biblioteca import funcionalidade -> importa apenas a funcionalidade da biblioteca

ex.: 
import math             -> toda biblioteca math
from math import sqrt   -> somente a funcão sqrt da biblioteca math

ou ainda, 

import math from sqrt, floor


'''
import math  # importamos a biblioteca math, vamos usar as funções obtidas nas referencias do python

pi = math.pi  # valor de pi
rad = 1
grau = 57.29
rad_graus = math.degrees(rad)
grau_rad = math.radians(grau)
print(rad_graus, grau_rad)
print(pi)
