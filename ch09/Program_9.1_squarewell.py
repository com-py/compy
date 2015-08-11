#
# Program 9.1: Visual eigenstates in the square well (squarewell.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np, visual as vp, ode, vpm

def V(x):               # potential
    return 0. if abs(x) > a/2. else -V0
    
def sch(psi, x):        # Schrodinger eqn
    return [psi[1], 2*(V(x)-E)*psi[0]]
          
# initialization and animation setup 
a, V0 = 4.0, 4.                     # well width, depth
R, N = 4*a, 200                     # limit, intervals
xa = np.linspace(-R, R, 2*N+1)      # grid
h, z = xa[1]-xa[0], np.zeros(2*N+1) # step size
E, dE, dpsi, psix = -V0, 0.001, 1.0, np.zeros(2*N+1)

scene = vp.display(background=(.2,.5,1), range=1.5*a)
wf = vpm.line(xa, psix, z, vp.color.red, .05)
pot = vpm.line(xa, .5*np.vectorize(V)(xa), z, (1,1,1), .04) # pot. V 
info = vp.label(pos=(0, -0.6*a, 0), box=False, height=20)

while (E < 0.0):
    psi, x = [.0, .1], -R
    for i in range(N):              # WF for x <=0
        psi = ode.RK45n(sch, psi, x, h)
        x += h
        psix[i+1] = psi[0]          
    psix[N+1:] = psix[N-1::-1]      # WF for x > 0 by reflection 
    if (dpsi*psi[1] < 0.):          # dpsi/dx changes sign
        info.text='Energy found, E=%5.4f' %(E-dE/2)
        vpm.pause(scene)            # any key to continue
    else:
        info.text='E=%5.3f' %(E)
    wf.move(xa, 2*psix/max(psix), z), vpm.wait(scene), vp.rate(2000)
    dpsi = psi[1]                   # old dpsi/dx at E
    E += dE
    
