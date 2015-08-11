#
# Program 9.4: Eigenenergies by BEM (bem.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np, integral as itg
from scipy.sparse.linalg import eigsh
from scipy.special import eval_hermite, gamma, ai_zeros

def V(x):                       # potential
    return beta*abs(x)

def uVu(x):                     # integrand $u_m V u_n$
    y, c = x/a0, a0*np.sqrt(np.pi*gamma(m+1)*gamma(n+1)*2**(m+n))
    return V(x)*eval_hermite(m,y)*eval_hermite(n,y)*np.exp(-y*y)/c

beta, omega, N = 1., 1., 20     # pot slope, nat freq, num. basis states
a0, x0 = 1/np.sqrt(omega), 1/(2*beta)**(1./3)   # length scale, x0

m, Vm = np.arange(N-2), np.zeros((N,N))
mm = np.sqrt((m+1)*(m+2))                       # calc T matrix
Tm = np.diag(np.arange(1, N+N, 2,float))        # diagonal
Tm -= np.diag(mm, 2) + np.diag(mm, -2)          # off diagonal by +/-2
for m in range(N):                       # calc V matrix
    for n in range(m, N, 2):             # m+n is even every 2 steps
        Vm[m, n] = 2*itg.gauss(uVu, 0., 10*a0)  # use symm.
        if (m != n): Vm[n,m] = Vm[m,n]
Tm = Tm*omega/4.
E, u = eigsh(Tm + Vm, 6, which='SA')     # get lowest 6 states

zn, zpn, zbn, zbpn = ai_zeros(3)         # find exact values
Ex = - beta*x0*np.insert(zpn, range(1, 4), zn)    # combine even/odd 
print (E, E/Ex)
   
