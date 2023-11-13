#Ejemplo 1, cortar elementos del indice 1 al indice 5

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

#Ejemplo 2, cortar elementos del indice 4 hasta el final

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

#Ejemplo 3, cortar elementos desde el principio hasta el indice 4 sin incluirlo

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])
