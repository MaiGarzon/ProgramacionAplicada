#Ejemplo 1, crear una matriz tipo String

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

#Ejemplo 2, crear una matriz tipo entero de 4 bytes

import numpy as np

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)
