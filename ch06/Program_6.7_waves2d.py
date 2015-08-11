#
# Program 6.7: Waves on a membrane (waves2d.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np, visual as vp, vpm

def wave2d(u0, u1):
    u2 = 2*(1-b-b)*u1 - u0
    u2[1:-1,1:-1] += b*( u1[1:-1,0:-2] + u1[1:-1,2:]     # left, right
                       + u1[0:-2,1:-1] + u1[2:,1:-1] )   # top, bottom
    return u2
    
def gaussian(x):
    return np.exp(-(x-5)**2)

L, N = 10.0, 40            # length of square, number of intervals
b = 0.25                   # beta^2

x = np.linspace(0., L, N+1)                       # mesh grid 
x, y = np.meshgrid(x, x)
u0, u1 = gaussian(x)*gaussian(y), gaussian(x)*gaussian(y)

scene = vp.display(title='2D waves', background=(.2,.5,1), 
                   center=(L/2,L/2,0), up=(0,0,1), forward=(1,2,-1))
mesh = vpm.mesh(x, y, 2*u0, (.9,.8,0), (1,0,0))   # mesh 

while(True):
    vp.rate(40), vpm.wait(scene)                  # pause if key press
    u2 = wave2d(u0, u1)
    u0, u1 = u1, u2                               # swap u's
    mesh.move(x, y, 2*u0)                         # redraw mesh 
    
   
