#
# Program 6.4: Waves on a string (waves.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np, visual as vp, vpm

def wavemotion(u0, u1):
    u2 = 2*(1-b)*u1 - u0                     # unshifted terms 
    u2[1:-1] += b*( u1[0:-2] + u1[2:] )      # left, right 
    return u2

def gaussian(x):
    return np.exp(-(x-5)**2)

L, N = 10.0, 100           # length of string, number of intervals
b = 1.0                    # beta^2

x, z = np.linspace(0., L, N+1), np.zeros(N+1)
u0, u1 = gaussian(x), gaussian(x)

scene = vp.display(title='Waves',background=(.2,.5,1),center=(L/2,0,0))
string = vpm.line(x, u0, z, (1,1,1), 0.05)   # string 

while(True):
    vp.rate(100), vpm.wait(scene)            # pause if key press 
    u2 = wavemotion(u0, u1)
    u0, u1 = u1, u2                          # swap u's
    string.move(x, 2*u0, z)                  # redraw string 
