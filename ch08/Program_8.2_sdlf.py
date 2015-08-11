#
# Program 8.2: Space discretized leapfrog method (sdlf.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np, visual as vp, ode, vpm

def sch_eqn(id, R, I, t):               # return dR/dt, dI/dt of Sch. eqn.
    b = 0.5/(h*h)   
    if (id == 0):                       # gen. velocity
        tmp = -b*I                      # 1st/3rd term in 
        dydt = (2*b + V)*I              # 2nd term
    else:                               # gen. acceleration
        tmp = b*R                       # 1st/3rd term in 
        dydt = (-2*b - V)*R             # 2nd term
        
    dydt[1:-1] += tmp[:-2] + tmp[2:]    # add $b \psi_{j-1}, b \psi_{j+1}$ to grid $j$
    dydt[0]  += tmp[-1] + tmp[1]        # 1st point, periodic BC 
    dydt[-1] += tmp[-2] + tmp[0]        # last point
    return dydt

def gaussian(s, x0, x):     # normalized Gaussian, s=width, x0=center
    c = 1.0/np.sqrt(s*np.sqrt(np.pi))
    return c*np.exp(-((x-x0)/s)**2/2)

def initialize(a, b, N):        # set parameters
    x = np.linspace(a, b, N+1)  # grid points
    V = 0.5*x*x                 # SHO potential
    s, x0  = 0.5, -5.0          # width (sigma), center of gaussian
    R, I = gaussian(s, x0, x), np.zeros(N+1)    # real, imag w.f.
    return x[1]-x[0], x,V,R,I   # grid size, h=x[1]-x[0]
    
a, b, N = -10., 10., 500        # space range [a,b], num. intervals
z, mag = np.zeros(N+1), 4       # zeros, magnifying factor

h, x, V, R, I = initialize(a, b, N)                 # initialization
scene = vp.display(background=(1,1,1), ambient=1)   # set scene
bars = vpm.bars(x, z, z, z, h, 0.05, (1,0,1))       # wave function
line = vpm.line(x, z, z, (1,0,1), 0.02)             
pot  = vpm.line(x, V*0.1, z, (0,0,0), 0.02)         # potential line

t, ic, cycle = 0.0, 0, 20       # t, animation cycle
dt = h*h*0.5                    # time step, dt < h*h
while True:
    R, I = ode.leapfrog(sch_eqn, R, I, t, dt)   # main work
    ic += 1
    if (ic % cycle == 0):       # animate
        pb = R*R + I*I          # probability
        line.move(x, mag*pb, z)
        bars.move(x, z, z, mag*pb)
    vp.rate(3000), vpm.wait(scene)

