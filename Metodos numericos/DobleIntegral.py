import numpy as np
from scipy.integrate import dblquad
import matplotlib.pyplot as plt
from matplotlib import cm

def f (y , x ) :

    return np.sin(np.sqrt(x**2 + y**2))

def grafica (f , x1 , x2 , y1 , y2 ) :
    x = np.linspace( x1 , x2 )
    y = np.linspace( y1 , y2 )

    X , Y = np.meshgrid(x , y )
    Z = f(X , Y )
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    surf = ax.plot_surface(X , Y , Z , cmap = cm.coolwarm,linewidth=0 , antialiased = False )
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.view_init(60 , 35)
    fig.colorbar( surf , shrink =0.5 , aspect =5)
    plt.show()
    fig.savefig(" int_cuadratura2d .pdf", bbox_inches ='tight ')


x1 = -5
x2 =5
y1 = -5
y2 =5

# llamada a la funcion dblquad de scipy
area ,_= dblquad(f , x1 , x2 ,lambda y:y1 , lambda y:y2)

print ('quadrature = ', area )
grafica (f , x1 , x2 , y1 , y2)


