#
# Program 2.8: RK4 nonvector method (rk4n.py)
# J Wang, Computational modeling and visualization with Python
#

def RK4n(diffeq, y0, t, h):     # non-vectorized with lists
    """ RK4 method for n ODEs:
        Given y0 at t, returns y1 at t+h """
    n, y1 = len(y0), [0.0]*len(y0)        
    k1 = diffeq(y0, t)                   # dy/dt at t
    for i in range(n):                   # loop thru n ODEs
        y1[i] = y0[i] + 0.5*h*k1[i]      # prep for k2[]
    k2 = diffeq(y1, t + h/2.)            # dy/dt at t+h/2
    for i in range(n):
        y1[i] = y0[i] + 0.5*h*k2[i]
    k3 = diffeq(y1, t + h/2.)            # dy/dt at t+h/2
    for i in range(n):
        y1[i] = y0[i] + h*k3[i]
    k4 = diffeq(y1, t + h)               # dy/dt at t+h
    for i in range(n):              
        y1[i] = y0[i] + h*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6.0
    return y1
