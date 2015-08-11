#
# Program 9.3: Eigenenergies by FEM (qmfem.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np
from scipy.sparse.linalg import eigsh

def V(x):                   # potential
    return 0. if (abs(x) >= a/2.) else -V0

def TB_mat(n):                           # fill in T and and B matrices
    Tm, B = np.diag([2.]*n), np.diag([4.]*n)
    Tm += np.diag([-1.]*(n-1),1) + np.diag([-1.]*(n-1),-1) # off diag
    B += np.diag([1.]*(n-1),1) + np.diag([1.]*(n-1),-1)     
    return Tm/(2.*h), B*h/6.
    
def Vij(i, j):      # pot. matrix Vij over $[x_i,x_{i+1}]$ by order-4 Gaussian
    x=np.array([0.3399810435848564, 0.8611363115940525])    # abscissa
    w=np.array([0.6521451548625463, 0.3478548451374545])    # weight
    phi = lambda i, x: 1.0 - abs(x-xa[i])/h       # tent function
    vV, hh = np.vectorize(V), h/2.0               # vectorize V
    x1, x2 = xa[i] + hh - hh*x, xa[i] + hh + hh*x
    return hh*np.sum(w * (vV(x1) * phi(i, x1) * phi(j, x1) +
                          vV(x2) * phi(i, x2) * phi(j, x2)) )
                        
def V_mat():        # fill potential matrix
    Vm = np.zeros((N-1,N-1))
    for i in range(N):      # for each element    # contribution to:
        if (i>0):   Vm[i-1,i-1] += Vij(i, i)      #     left node
        if (i < N-1): Vm[i,i] += Vij(i+1, i+1)    #     right node
        if (i>0 and i< N-1):
            Vm[i-1,i] += Vij(i, i+1)              #     off diagonals
            Vm[i,i-1] = Vm[i-1,i]                 #     symmetry
    return Vm

a, V0 = 4.0, 4.0                    # well width, depth
xL, xR, N = -4*a, 4*a, 600          # boundaries, num. of elements
xa = np.linspace(xL, xR, N+1)       # nodes
h = xa[1]-xa[0]                     # size of element

Tm, B = TB_mat(N-1)                 # obtain T, B, V matrices
Vm = V_mat()
    
E, u = eigsh(Tm + Vm, 10, B, which='SA')    # get lowest 10 states 
print (E)
