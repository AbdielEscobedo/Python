import numpy as np
from scipy.interpolate import lagrange
from scipy.integrate import simps
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def regla_simpson13 (f ,a ,b , n ) :
    h =( b - a ) / n
    xs = np . linspace (a ,b , n +1)
    ys = f ( xs )
    r = h *( ys [0]+4* sum ( ys [1: n :2]) +2* sum( ys [2: n -1:2]) + ys [ n ]) /3
    return r

def regla_simpson38 (f,a,b,n):
    h =( b - a ) / n
    xs = np . linspace (a ,b , n +1)
    ys = f ( xs )
    r =3* h *( ys [0]+3* sum ( ys [1: n -1:3]) +3* sum( ys [2: n :3]) +2* sum ( ys [3: n-2:3]) + ys [ n ]) /8
    return r

def regla_trapecios (f ,a ,b , n ) :
    h =( b - a ) / n
    xs = np . linspace (a ,b , n +1)
    ys = f ( xs )
    r = h *( ys [0]+2* sum ( ys [1: n ]) + ys [ n ]) /2
    return r

def cuadratura2 (f ,a , b ) :
    x1 =( b - a ) /2*( -1/ np . sqrt (3) ) +( a + b ) /2
    x2 =( b - a ) /2*(1/ np . sqrt (3) ) +( a + b ) /2
    r =( b - a ) /2*( f ( x1 ) + f ( x2 ) )
    return r

def f ( x ) :
    return (9+4* np . cos (0.4* x ) **2) *(5* np . exp ( -0.5* x ) +2* np . exp (0.15*x ) )

a=2
b=8
n=6
area=regla_simpson13(f,a,b,n)
print(area)

