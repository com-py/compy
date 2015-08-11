#
# Program 11.7: N-body molecular dynamics (md.py)
# J Wang, Computational modeling and visualization with Python
#

import ode, vpm, random as rnd
import numpy as np, visual as vp

def nbody(id, r, v, t):                     # N-body MD
    if (id == 0):                           # velocity
        return v
    a = np.zeros((N,3))                     # acceleration
    for i in range(N):
        rij = r[i]-r[i+1:]                  # rij for all j>i 
        rij[rij > HL]  -= L                 # periodic bc
        rij[rij < -HL] += L
        r2 = np.sum(rij*rij, axis=1)        # |rij|^2
        r6 = r2*r2*r2
        for k in [0,1,2]:                   # L-J force in x,y,z
            fij = 12.*(1. - r6)*rij[:,k]/(r6*r6*r2)
            a[i,k] += np.sum(fij)
            a[i+1:,k] -= fij                # 3rd law
    return a
    
L, N = 10.0, 32                             # cube size, num. atoms
atoms, HL, t, h = [], L/2., 0., 0.002
r, v =  np.zeros((N,3)), np.zeros((N,3))

scene = vp.display(background=(.2,.5,1), center=(L/2, L/3, L/2))
vp.box(pos=(HL,HL,HL), length=L, height=L, width=L, opacity=0.3)
for i in range(N):                          # initial pos, vel
    for k in range(3):
        r[i,k] = L*rnd.random()
        v[i,k] = 1-2*rnd.random()
    atoms.append(vp.sphere(pos=r[i], radius=0.04*L, color=(1,0,1)))
v -= np.sum(v, axis=0)/N                    # center of mass frame 

while (1):
    vpm.wait(scene), vp.rate(1000)
    r, v = ode.leapfrog(nbody, r, v, t, h)
    r[r > L]  -= L                          # periodic bc
    r[r < 0.] += L
    for i in range(N): atoms[i].pos = r[i]  # move atoms
