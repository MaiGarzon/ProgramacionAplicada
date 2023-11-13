#Ejemplo 1, desde el segundo elemento, corte los elementos del indice 1 al 4 sin incluirlo

import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

#Ejemplo 2, desde ambos elementos, devuelve el indice 2

import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])

#Ejemplo 3, de ambos elementos divide el indice 1 al 4 sin incluirlo

import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])
