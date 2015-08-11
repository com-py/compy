#
# Program 9.5: Hydrogen atom by Numerov's method (hydrogen.py)
# J Wang, Computational modeling and visualization with Python
#

import matplotlib.pyplot as plt
import numpy as np, rootfinder as rtf

def Veff(r):                    # effective potential
    return (L*(L+1)/(2*mass*r)-1)/r
    
def f(r):                       # Sch eqn in Numerov form
    return 2*mass*(E-Veff(r))
    
def numerov(f, u, n, x, h):     # Numerov integrator for $u''+f(x)u=0$
    nodes, c = 0, h*h/12.       # given $[u_0,u_1]$, return $[u_0,u_1,...,u_{n+1}]$
    f0, f1 = 0., f(x+h)
    for i in range(n):
        x += h
        f2 = f(x+h)             # Numerov method below, 
        u.append((2*(1-5*c*f1)*u[i+1] - (1+c*f0)*u[i])/(1+c*f2))  
        f0, f1 = f1, f2
        if (u[-1]*u[-2] < 0.0): nodes += 1
    return u, nodes             # return u, nodes
    
def shoot(En):
    global E                    # E needed in f(r)
    E, c, xm = En, (h*h)/6., xL + M*h
    wfup, nup = numerov(f, [0,.1], M, xL, h)
    wfdn, ndn = numerov(f, [0,.1], N-M, xR, -h)     # $f'$ from 
    dup = ((1+c*f(xm+h))*wfup[-1] - (1+c*f(xm-h))*wfup[-3])/(h+h)
    ddn = ((1+c*f(xm+h))*wfdn[-3] - (1+c*f(xm-h))*wfdn[-1])/(h+h)
    return dup*wfdn[-2] - wfup[-2]*ddn

xL, xR, N = 0., 120., 2200          # limits, intervals
h, mass = (xR-xL)/N, 1.0            # step size, mass
Lmax, EL, M = 4, [], 100            # M = matching point

Estart, dE = -.5/np.arange(1, Lmax+1)**2-.1, 0.001      # $\sim -1/2n^2$
for L in range(Lmax):
    n, E1, Ea = L+1, Estart[L], []
    while (E1 < -4*dE):             # sweep E range for each L
        E1 += dE
        if (shoot(E1)*shoot(E1 + dE) > 0): continue
        E = rtf.bisect(shoot, E1, E1 + dE, 1.e-8)
        Ea.append(E)
        wfup, nup = numerov(f, [0,.1], M-1, xL, h)      # calc wf
        wfdn, ndn = numerov(f, [0,.1], N-M-1, xR, -h)
        psix = np.concatenate((wfup[:-1], wfdn[::-1]))
        psix[M:] *= wfup[-1]/wfdn[-1]                   # match
        print ('nodes, n,l,E=', nup+ndn, n, L, E)
        n += 1
    EL.append(Ea)
    
plt.figure()                        # plot energy levels
for L in range(Lmax):
    for i in range(len(EL[L])):
        plt.plot([L-.3, L+.3], [EL[L][i]]*2, 'k-')
    plt.xlabel('$l$'), plt.ylabel('$E$')
    plt.ylim(-.51, 0), plt.xticks(range(Lmax))
plt.show()
