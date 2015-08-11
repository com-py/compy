#
# Program 7.7: Electric dipole fields (edipole.py)
# J Wang, Computational modeling and visualization with Python
#

import visual as vp, numpy as np
                               
r, scale, m, n = 0.5, 0.05, 11, 19         # parameters
scene = vp.display(title='Electric dipole', background=(.2,.5,1), 
                   forward=(0,-1,-.5), up=(0,0,1))
zaxis = vp.curve(pos=[(0,0,-r),(0,0,r)])                    
qpos = vp.sphere(pos=(0,0,.02), radius=0.01, color=(1,0,0))
qneg = vp.sphere(pos=(0,0,-.02), radius=0.01, color=(0,0,1))
c1 = vp.ring(pos=(0,0,0), radius=r, axis=(0,0,1), thickness=0.002)
c2 = vp.ring(pos=(0,0,0), radius=r, axis=(0,1,0), thickness=0.002)

theta, phi = np.linspace(0, np.pi, m), np.linspace(0, 2*np.pi, n) # grid 
phi, theta = vp.meshgrid(phi, theta)
rs = r*np.sin(theta)
x, y, z = rs*np.cos(phi), rs*np.sin(phi), r*np.cos(theta)   # coord. 
for i in range(m):
    for j in range(n):
        rvec = vp.vector(x[i,j], y[i,j], z[i,j])
        B = scale*vp.cross(rvec, vp.vector(0,0,1))/(r*r)    # $\vec{r}\times \hat z/r^2$
        E = vp.cross(B, rvec)/r                             # $\vec{B}\times \vec{r}/r$
        vp.arrow(pos=rvec, axis=E, length=vp.mag(E), color=(1,1,0))
        vp.arrow(pos=rvec, axis=B, length=vp.mag(B), color=(0,1,1))
    
    
    
    
    
    
    
    
    
    
   
