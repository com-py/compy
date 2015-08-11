#
# Program 10.3: Electrostatic energy (mcint.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np, random as rnd

def sample(r):     # return a random point inside a sphere
    while True:
        x, y, z = rnd.random(), rnd.random(), rnd.random()
        x, y, z = r*(x+x-1), r*(y+y-1), r*(z+z-1)   # map to [-r, r]
        if (x*x + y*y + z*z <= r*r): break
    return x, y, z

r1, r2, d = 1.0, 2.0, 4.0           # radii and separation, d>r1+r2

f, V, N = 0., (4*np.pi/3.)**2*(r1*r2)**3, 100
for i in range(N):
    x1, y1, z1 = sample(r1)
    x2, y2, z2 = sample(r2)
    f += 1./np.sqrt((x1-x2-d)**2+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2))
    
print ('MC=', V*f/N, 'exact=', V/d)

