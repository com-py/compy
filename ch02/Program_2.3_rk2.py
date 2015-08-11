#
# Program 2.3: RK2 method (rk2.py)
# J Wang, Computational modeling and visualization with Python
#

def RK2(diffeq, y0, t, h):
    """ RK2 method for ODEs:
        Given y0 at t, returns y1 at t+h """
    k1 = h*diffeq(y0, t)                # get dy/dt at t first
    k2 = h*diffeq(y0+0.5*k1, t + h/2.)  # get dy/dt at t+h/2,
    return y0 + k2                      # calc. y1 = y(t+h)
   
