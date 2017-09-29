#
# Program 2.5: Free fall with modular Euler (freefall_euler.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np              # get numpy functions
import matplotlib.pyplot as plt # get matplotlib plot functions
g = 9.8                         # gravitational constant

def Euler(diffeq, y0, t, h): # uses docstring """..."""
    """ Euler's method for n ODEs:
        Given y0 at t, returns y1 at t+h """
    dydt = diffeq(y0, t)     # get {dy/dt} at t
    return y0 + h*dydt       # Euler method on a vector  
    
def freefall(y, t):          # returns {dy/dt}, the RHS of ODEs
    dydt = np.zeros(2)       # initialize 2-element numpy array 
    dydt[0] = y[1]           # f1(), 
    dydt[1] = -g             # f2(), 
    return dydt              # note: returns whole array dydt[]
     
def go(v0):                  # main program, v0=initial velocity
    y0 = [0.0, v0]           # initial values
    t, h = 0.0, 0.02         # init time, step size
    ta,ya,yb = [],[],[]      # declare arrays for plotting
    while t<1.0:             # loop for one second
        ta.append(t)         # record time and position
        ya.append(y0[0])
        yb.append(v0*t-g*t*t/2.0)
        y1 = Euler(freefall, y0, t, h)   # Euler's method
        for i in range(len(y0)):         # reseed y0
            y0[i] = y1[i]
        t = t + h

    plt.figure()                # start a figure
    plt.plot(ta,ya, ta,yb,'--') # draw 2nd curve as dashed
    plt.xlabel('t (s)')         # add labels
    plt.ylabel('y (m)')
    plt.show()                  # show figure
    
go(5.0)                     # run the program
