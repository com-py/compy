#
# Program 10.1: Random walk in 2D (walk2d.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np, random as rnd
import matplotlib.pyplot as plt

def walknsteps(n):                          # walk n steps
    x, y = np.zeros(n+1), np.zeros(n+1)
    for i in range(n):
        phi = rnd.random()*2*np.pi          # random in $[0,2\pi]$
        x[i+1] = x[i] + np.cos(phi)
        y[i+1] = y[i] + np.sin(phi)
    return x, y
    
nstep, N = 20, 4                            # steps, num of walkers
col = ['k', 'r', 'g', 'b', 'c', 'm']        # color codes
plt.subplot(111, aspect='equal')
for i in range(N):
    x, y = walknsteps(nstep)
    plt.quiver(x[:-1], y[:-1], x[1:]-x[:-1], y[1:]-y[:-1], scale=1,
            scale_units='xy', angles='xy', color=col[i%len(col)])
plt.plot([0],[0],'y*', markersize=16)
plt.xlabel('$x$'), plt.ylabel('$y$')
plt.show()
