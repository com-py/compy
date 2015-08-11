#
# Program 3.5: Shooting method (shoot.py)
# J Wang, Computational modeling and visualization with Python
#

from __future__ import print_function       # use print() as function
import ode, rootfinder as rtf, numpy as np   # ode, root solvers, numpy

def proj(Y, t):                 # ideal projectile motion
    return np.array([Y[2],Y[3], 0.0,-g])   # [vx,vy,ax,ay]
   
def fy(theta):                  # return f as a func of theta
    Y = [0., 0., v0*np.cos(theta), v0*np.sin(theta)]    # [x,y,vx,vy]
    t = xb / Y[2]               # Step 1: time to xb    
    h = t / nsteps
    for i in range(nsteps):
        Y = ode.RK2(proj, Y, t, h)            # no need to update t
        
    return Y[1] - yb                            # Step 2: $y(\theta) - y_b$

# number of steps, g, init speed, x and y boundary values
nsteps, g, v0, xb, yb = 100, 9.8, 22., 40., 3.  # para. 

theta = rtf.bisect(fy, 0.6, 1.2, 1.e-6)      # Step 3: shoot for $\theta$
if (theta != None): print('theta(deg)=',theta*180/np.pi)   # result
