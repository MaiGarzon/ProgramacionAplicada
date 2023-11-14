#Convertir la matriz de 1D a 3D, la dimesion externa tiene 2
#matrices que contienen 3 matrices, cada una con 2 elementos

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)
