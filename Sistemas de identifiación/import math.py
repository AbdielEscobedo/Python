import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2-2

x=np.linspace(-2,2,100)
y=f(x)

fig=plt.figure()
ax=plt.gca()
ax.set_xlabel('x')
ax.set_ylabel('y')
plt.plot(x,y)
plt.title('$f(X)=x**2-2$')
plt.grid()
ax.spines('left').set_position('zero')
ax.spines('rigth').set_color('none')
ax.spines('bottom').set_position('zero')
ax.spines('top').set_color('none')
plt.show()

