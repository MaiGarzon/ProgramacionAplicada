#Convertimos una matriz 1D con 8 elementos en una matriz 3D con elementos 2x2

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)
