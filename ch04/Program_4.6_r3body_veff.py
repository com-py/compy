#
# Program 4.6: Plotting the effective potential (r3body_veff.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np                  # get numpy functions
import matplotlib.pyplot as plt     # get matplotlib plot functions
from mpl_toolkits.mplot3d import Axes3D     # for surface plots

def potential(x, y):    # returns effective potential, without 4pi^2 
    r1 = np.sqrt((x+a)*(x+a)+y*y)   # use np.sqrt for array operations 
    r2 = np.sqrt((x-b)*(x-b)+y*y)
    V = -(1.0-a)/r1 - a/r2 - 0.5*(x*x+y*y)
    return np.maximum(V, -4.0)      # low cutoff value 

def makeplot(): 
    n, s = 201, 5                       # grid points and stride
    x = np.linspace(-1.5, 1.5, n)       # same x,y grids
    x, y = np.meshgrid(x, x)            # make meshgrid, ie, 1D -> 2D 
    
    V = potential(x, y)                 # compute V, -grad(V)   
    Fy, Fx = np.gradient(-V)            # swap Fx, Fy since V[i,j]=V[x,y] 
    big = Fx*Fx + Fy*Fy > 0.003         # truth array for A[i,j] >.003 
    Fx[big], Fy[big] = 0, 0             # cut off large values 
    
    fig = plt.figure()   # add surface plot with strides and color map 
    axis=fig.add_subplot(111, projection='3d')  # add subplot
    axis.plot_surface(x, y, V, rstride=3, cstride=3,
                      linewidth=0, cmap=plt.cm.spectral)
    axis.set_xlabel('x'), axis.set_ylabel('y'), axis.set_zlabel('V')
    
    plt.figure()                            # draw contours and arrows 
    plt.subplot(111, aspect='equal')        # square picture
    plt.contour(x, y, V, 26)                # 26 contour lines
    plt.xticks([],[]), plt.yticks([],[])    # omit ticks
    
    # draw arrows on strided grid to space them out, via array slicing
    plt.quiver(x[::s,::s], y[::s,::s], Fx[::s,::s], Fy[::s,::s],
               width=0.005, minshaft=2, minlength=0)     # arrow shape 
    txt = ['$L_1$', '$L_2$', '$L_3$', '$L_4$', '$L_5$']  # Lag. pts label 
    loc = [(-1.1,-.07),(.5,-.07),(1.2,-.07),(.3,.8),(.3,-1)] # label pos
    for i in range(len(txt)):
        plt.text(loc[i][0], loc[i][1], txt[i], fontsize=16)

    plt.show()

alpha = 0.121           # globals
a, b = alpha, 1.0-alpha
makeplot()
