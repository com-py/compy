#
# Program 7.6: Magnetic fields of a current-carrying wire (longwire.py)
# J Wang, Computational modeling and visualization with Python
#

import visual as vp, numpy as np

m, n = 6, 30                                # r, phi intervals
r = np.linspace(0.15, 0.4, m)
phi = np.linspace(0., 2*np.pi, n+1)
r, phi = np.meshgrid(r, phi)                # n x m grid

x, y = r*np.cos(phi), r*np.sin(phi)         # pos and dirs of B-fields
ax, ay = -np.sin(phi), np.cos(phi)          # tangential vectors 

scene = vp.display(title='Magnetic fields', background=(.2,.5,1))
wire = vp.curve(pos=[(0,0,.6), (0,0,-.6)], radius = 0.01)

scale, q = 0.008, 1.0
for z in np.linspace(.5, -.5, 6):
    for i in range(n):
        for j in range(m):
            vp.arrow(pos=(x[i,j], y[i,j], z), axis=(ax[i,j], ay[i,j]),
                     length=scale/r[i,j], color=(q, q, 0))
    q = q - .05

    
    
    
    
    
    
    
    
    
    
   
