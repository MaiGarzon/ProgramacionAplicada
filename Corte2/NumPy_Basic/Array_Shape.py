#Obtener la forma, o el numero de elementos de cada dimension

#Ejemplo 1, imprimir la forma de una matriz 2D

import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

#Ejemplo 2, Crear una matriz con 5 dimensiones usando ndmin un vector con valores 1,2,3,4 y verificar que la ultima dimensión dea 4

import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)
