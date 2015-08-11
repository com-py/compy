#
# Program 3.2: Linear drag (projectile.py)
# J Wang, Computational modeling and visualization with Python
#

import ode, numpy as np           # ODE solvers, numpy
import matplotlib.pyplot as plt     # plot functions

def Lin_drag(Y, t):         # projectile motion with linear drag
    # returns RHS of 
    return np.array([Y[2], Y[3], -b1*Y[2]/m, -g - b1*Y[3]/m])
   
def go(vx=5., vy=5.):               # default velocity=(5,5)
    Y = [0., 0., vx, vy]            # initial values, [x,y,vx,vy]
    t, h, x, y = 0., .01, [], []    # time, step size, temp arrays
    while Y[1] >= 0.0:              # loop as long as y>=0
        x.append(Y[0]), y.append(Y[1])              # record pos.
        Y, t = ode.RK4(Lin_drag, Y, t, h), t+h    # update Y, t
        
    plt.figure()                    # open fig, plot, label, show fig
    plt.plot(x, y), plt.xlabel('x (m)'), plt.ylabel('y (m)')
    plt.show()                  
    
g, b1, m = 9.8, 0.2, 0.5            # g, linear coeff., mass
go(vx=10.0, vy=10.0)
