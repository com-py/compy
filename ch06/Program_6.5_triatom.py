#
# Program 6.5: Triatomic vibrations (triatom.py)
# J Wang, Computational modeling and visualization with Python
#

import visual as vp, numpy as np

def accel(u):
    return -k*np.array([u[0]-u[1], 2*u[1]-u[0]-u[2], u[2]-u[1]])/m

col = [(1,0,0), (0,1,0), (0,0,1)]           # RGB colors
x0, atom, r = np.array([-3., 0., 3.]), [0]*3, 1.0
for i in range(3):
    atom[i] = vp.sphere(pos=(x0[i],0,0), radius=r, color=col[i]) # atoms
floor = vp.box(pos=(0,-1.1,0), length=8, height=0.2, width=4)    # floor 
s1 = vp.helix(pos=(x0[0],0,0), thickness=0.1, radius=0.5)        # spring
s2 = vp.helix(pos=(x0[1],0,0), thickness=0.1, radius=0.5)

h, k, m = 0.1, 1.0, np.array([1./4, 2./5, 1./4])
u, v = np.array([-1.,0.,1.]), np.zeros(3)   # symmetric init cond
while True:
    vp.rate(50)
    u = u + v*h                             # Euler-Cromer method
    v = v + accel(u)*h
    x = x0 + u
    for i in range(3):                      # animation
        atom[i].pos = (x[i],0,0)
    s1.axis, s1.pos, s1.length= (1,0,0), x[0]+r, x[1]-x[0]-2*r   # move 
    s2.axis, s2.pos, s2.length= (1,0,0), x[1]+r, x[2]-x[1]-2*r
       
