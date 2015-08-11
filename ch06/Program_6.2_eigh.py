#
# Program 6.2: Diagonalization of triatomic systems (eigh.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np
from scipy.linalg import eigh       # Hermitian eigenvalue solver

k = 1.0
m1, m2, m3 = 1./4., 2./5., 1./4.
A = np.array([[k, -k, 0], [-k, 2*k, -k], [0, -k, k]])
B = np.array([[m1, 0, 0], [0, m2, 0], [0, 0, m3]])

lamb, u = eigh(A, B)        # eigenvalues and eigenvectors  
print (np.sqrt(lamb))       # print omega
