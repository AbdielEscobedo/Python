#Interpolación de NEVILLE
import numpy as np
import matplotlib.pyplot as plt

x=np.array([1,4,8,13,18])
y=np.array([1.1,1.5,12.8,15.3,15.5])
n=x.size  #Tomamos los valores que necesitamos de la tabla
G=np.zeros((n,n))
xi=3
yi=0

#Calcula las interpolaciones y compara los valores
G[:,0]=y
for i in range (1,n):
    for j in range(1,i+1):
        G[i,j]=((xi-x[i-j])*G[i,j-1]-(xi-x[i])*G[i-1,j-1])/(x[i]-x[i-j])
        yi=G[i,i]
        if abs (G[i,i]-G[i-1,i-1])<1e-5:
                exit
print(G)
print(yi)

plt.plot(x,y,'o')
plt.plot(xi,yi,'sr')
plt.text(xi+0.1,yi,'profundidad'+str(yi))
plt.legend(['Datos','Interpolacion'])
plt.grid(True)
plt.show()
    


