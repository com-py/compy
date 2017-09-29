#
# Program 2.7: Oscillator with leapfrog method (sho_lf.py)
# J Wang, Computational modeling and visualization with Python
#

import ode                      # get ODE solvers
import math as ma               # get math functions
import matplotlib.pyplot as plt # get matplotlib plot functions
    
def oscillator(id, x, v, t):    # return dx/dt or dv/dt
    if (id==0):             # calc velocity
        return v        
    else:                   # calc acceleration
        return -x           # $-\omega^2 x, \omega=1$,
        
def go():                   # main program
    x, v = 1.0, 0.0         # initial values
    t, h = 0.0, 0.1         # init time, step size
    xa, va = [],[]          # declare arrays for plotting
    while t<4*ma.pi:        # loop for two periods  
        xa.append(x)        # record position and velocity
        va.append(v)
        x, v = ode.leapfrog(oscillator, x, v, t, h) # solve it 
        t = t + h

    plt.figure()            # start a figure    
    plt.plot(xa,va)         # plot vel-pos
    plt.xlabel('x (m)')     # add labels
    plt.ylabel('v (m/s)')
    plt.show()              # show figure       
    
go()                        # run the program
