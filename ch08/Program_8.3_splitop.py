#
# Program 8.3: Quantum free fall (splitop.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np, visual as vp, vpm
from scipy.linalg import solve_banded
import matplotlib.pyplot as plt

def gaussian(s, x0, x):     # normalized Gaussian, s=width, x0=center
    c = 1.0/np.sqrt(s*np.sqrt(np.pi))
    return c*np.exp(-((x-x0)/s)**2/2)

def initialize(a, b, N):        # set parameters
    x = np.linspace(a, b, N+1)  # grid points
    V = 2*x                     # linear potential
    s, x0  = 0.5, 5.0           # width (sigma), center of gaussian
    R, I = gaussian(s, x0, x), np.zeros(N+1)    # real, imag w.f.
    return x[1]-x[0], x,V,R,I   # grid size, h=x[1]-x[0]
    
a, b, N = -10., 10., 500        # space range [a,b], num. intervals
z, mag = np.zeros(N+1), 6       # zeros, magnifying factor

h, x, V, R, I = initialize(a, b, N)                 # initialization
scene = vp.display(background=(1,1,1), ambient=1)   # set scene
bars = vpm.bars(x, z, z, z, h, 0.05, (1,0,1))       # wave function
line = vpm.line(x, z, z, (1,0,1), 0.02)             
pot  = vpm.line(x, V*0.05, z, (0,0,0), 0.02)        # potential line

t, ic, cycle = 0.0, 0, 10               # t, animation cycle
dt, psi = 0.001, R + 1j*I               # initialize dt, complex psi
ta, pba = [], []                        # time, prob. arrays
A = np.ones((3, N+1), dtype=complex)    # prepare band matrix A, B  
A[1,:] = 2*(2j*h*h/dt - 1 - h*h*V)
dB = - np.conjugate(A[1,:])             # diagonal of B
while(t<=3):
    C = dB*psi                          # prepare RHS 
    C[1:-1] -= (psi[:-2] + psi[2:])    
    psi = solve_banded((1,1), A, C)     # band matrix solver 
    t, ic = t+dt, ic+1
    if (ic % cycle == 0):
        pb = psi.real**2 + psi.imag**2  # probability   
        ta.append(t), pba.append(pb)    # store data
        line.move(x, mag*pb, z)
        bars.move(x, z, z, mag*pb)
    vp.rate(1200), vpm.wait(scene)

(X, Y), ta = np.meshgrid(x, ta), np.array(ta)
plt.figure()
plt.contour(Y, X, pba, 36, linewidths=1)
plt.plot(ta, 5 - ta*ta, 'r--')          # classical free fall
plt.xlabel('t (a.u.)'), plt.ylabel('x (a.u.)')
plt.show()
