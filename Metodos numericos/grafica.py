import numpy as np
from scipy import interpolate
#from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

x=np.array([4.1,12.2,20.3,28.2,38.1,45.2])
y=np.array([1.0276,1.1013,1.1801,1.2652,1.348,1.412])

xfino=np.linspace(4.1,45.2,100)
yi=interpolate.interp1d(x,y,kind='linear')

xi=25
yii=yi(xi)

plt.plot(x,y,'o',xfino,yi(xfino),'-',xi,yii,'sr')
#x,y,'o' solamente grafica los puntos
#x,y,'-' grafica la linea que los une
#x,y,'--' graficara una linea punteada

plt.legend(['Datos','interpolacion lineal', 'regresion lineal'])
plt.title('interpolacion')
plt.grid(True)
plt.show()
