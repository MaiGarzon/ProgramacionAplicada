#Ejemplo 1, cambiamos el tipo de datos flotante a entero usando 'i' como valor de parametro

import numpy as np

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

#Ejemplo 2, cambiamos el tipo de datos flotante a entero usando 'int' como valor de parametro 

import numpy as np

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

#Ejemplo 3, cambiamos el tipo de datos de entero a booleano

import numpy as np

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)
