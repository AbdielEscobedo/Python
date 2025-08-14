import numpy as np
A = np.matrix([[2, 3],[1, -2]])
b = np.matrix([[8],[-10]])
x = (A**-1)*b
if np.linalg.det(A) == 0:
    x = None
    print("No se puede resolver")
else:
    print(x)
