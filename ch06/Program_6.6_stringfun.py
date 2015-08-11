#
# Program 6.6: Standing waves on a string (stringfun.py)
# J Wang, Computational modeling and visualization with Python
#

from scipy.linalg import eigh       # Hermitian eigenvalue solver
import numpy as np, matplotlib.pyplot as plt

N = 20                      # number of intervals
h, s = 1./N, 5              # bin size, skip

A = np.diag([-2.]*(N-1))                            # diagonal
A += np.diag([1.]*(N-2),1) + np.diag([1.]*(N-2),-1) # off diagonals

A = -A/(h*h)                # solve $-h^{-2} A X = k^2 X$
lamb, u = eigh(A)           # so eigenvalues lamb = k^2

x, sty = np.linspace(0.,1., s*N + 1), ['o','^','s','v']
fig, f, pi = plt.figure(), np.sin, np.pi          # some aliases
print (2*pi/np.sqrt(lamb[:len(sty)]))             # wavelength 

for i in range(1, len(sty)+1):
    ui = np.insert(u[:,i-1], [0, N-1], [0., 0.])  # insert BV
    plt.plot(x, f(i*pi*x)*ui[1]/f(i*pi*x[s]))     # normalize soln
    plt.plot(x[::s], ui, sty[i-1], label=repr(i))
    
plt.xlabel('$x$'), plt.ylabel('$u$')
plt.legend(loc='lower right'), plt.show()
