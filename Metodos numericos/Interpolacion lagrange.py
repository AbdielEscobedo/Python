#Interpolación de Lagrange
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x=np.array([1,4,8,13,18])
y=np.array([1.1,1.5,12.8,15.3,15.5])
n=2
xi=3
yi=0

for i in range (0,n):
    producto=y[i]
    for j in range(0,n):
        if i!=j:
            producto=producto*(xi-x[j])/(x[i]-x[j]);
    yi=yi+producto
    
print(yi)
f=interpolate.lagrange(x,y)
print(f(xi))

plt.plot(x,y,'o')
plt.plot(xi,yi,'sr')
plt.text(xi+0.1,yi,'profundidad'+str(yi))
plt.legend(['Datos','Interpolacion'])
plt.grid(True)
plt.show()
    


