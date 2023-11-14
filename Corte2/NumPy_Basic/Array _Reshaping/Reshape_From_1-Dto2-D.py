#Convertimos la matriz de 1D a 2D, la dimensión más externa tendrá 4 matrices, cada una con 3 elementos

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
