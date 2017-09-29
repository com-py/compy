#
# Program 9.2: Shooting method for double well (qmshoot.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np, rootfinder as rtf, ode
import matplotlib.pyplot as plt

def V(x):                   # potential
    return 0 if (abs(x) > a/2. or abs(x) < b/2.) else -V0
    
def sch(psi, x):            # Schrodinger eqn
    return [psi[1], 2*(V(x)-E)*psi[0]]
    
def intsch(psi, n, x, h):   # integrate Sch eqn for n steps
    psix = [psi[0]]
    for i in range(n):
        psi = ode.RK45n(sch, psi, x, h)
        x += h
        psix.append(psi[0])
    return psix, psi        # return WF and last point
    
def shoot(En):              # calc diff of derivatives at given E
    global E                # global E, needed in sch()
    E = En
    wfup, psiup = intsch([0., .1], N, xL, h)      # march upward 
    wfdn, psidn = intsch([0., .1], N, xR, -h)     # march downward
    return psidn[0]*psiup[1] - psiup[0]*psidn[1]

a, b, V0 = 4.0, 1.0, 6.             # double well widths, depth
xL, xR, N = -4*a, 4*a, 500          # limits, intervals
xa = np.linspace(xL, xR, 2*N+1)     # grid
h, M = xa[1]-xa[0], 2               # step size, M=matching point
E1, dE, j = -V0, 0.01, 1

plt.figure()
while (E1 < 0):     # find E, calc and plot wave function
    if (shoot(E1) * shoot(E1 + dE) < 0):        # bracket E
        E = rtf.bisect(shoot, E1, E1 + dE, 1.e-8)
        print ('Energy found: %.3f' %(E))
        wfup, psiup = intsch([0., .1], N+M, xL, h)      # compute WF
        wfdn, psidn = intsch([0., .1], N-M, xR, -h)
        psix = np.concatenate((wfup[:-1], wfdn[::-1]))  # combine WF
        scale = psiup[0]/psidn[0]
        psix[N+M:] *= scale                             # match WF
        ax = plt.subplot(2,2,j)
        ax.plot(xa, psix/max(psix))                     # plot WF
        ax.plot(xa, np.vectorize(V)(xa)/(2*V0))         # overlay V
        ax.set_xlim(-a,a)
        ax.text(2.2,0.7, '%.3f' %(E))
        if (j == 1 or j == 3): ax.set_ylabel(r'$\psi$')
        if (j == 3 or j == 4): ax.set_xlabel('$x$')
        if (j<4): j += 1            # 4 plots max
    E1 += dE
plt.show()
