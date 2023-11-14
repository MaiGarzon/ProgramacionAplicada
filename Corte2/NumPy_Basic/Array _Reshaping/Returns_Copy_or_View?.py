#comprobamos si la matriz devielta es copia o vista:

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)

#Como devuelve la matriz original es una vista
