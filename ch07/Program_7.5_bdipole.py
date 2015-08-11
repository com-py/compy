#
# Program 7.5: Magnetic dipole fields (bdipole.py)
# J Wang, Computational modeling and visualization with Python
#

import visual as vp, numpy as np
import matplotlib.pyplot as plt

def bdipole(r):                     # calc magnetic fields at $\vec{r}$
    b, rel = vp.vector(0,0,0), r-rs
    for i in range(len(ds)):        # sum over segments
        b += vp.cross(ds[i], rel[i])/vp.mag(rel[i])**3   # $\sum Id\vec{s}\times \vec{r}/r^3$
    return b
    
divs, m, n = 36, 21, 16             # circle divisions, space grid
phi = np.linspace(0., 2*np.pi, divs+1)[:-1]              # omit last pt
rs = np.column_stack((np.cos(phi), np.sin(phi), 0*phi))  # segments 
ds = np.column_stack((-np.sin(phi), np.cos(phi), 0*phi)) # tangents $d\vec{s}$
x, z = np.linspace(-2, 2, m), np.linspace(-1.5, 1.5, n)
x, z = np.meshgrid(x, z)

bx, bz, big = np.zeros((n,m)), np.zeros((n,m)), 100.
for i in range(n):
    for j in range(m):
        b = bdipole(vp.vector(x[i,j], 0., z[i,j]))
        if (vp.mag(b) < big):               # exclude large fields
            bx[i,j], bz[i,j] = b.x, b.z

plt.subplot(111, aspect='equal')
plt.quiver(x, z, bx, bz, width=0.004, minshaft=1.5, minlength=0)
plt.plot([-1],[0], 'bo', [1],[0], 'bx')     # eyes
plt.show()
   
