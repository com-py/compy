#
# Program 7.4: Laplace equation by RBF (laplacerbf.py)
# J Wang, Computational modeling and visualization with Python
#

from scipy.linalg import solve
import matplotlib.pyplot as plt, numpy as np

def initialize(L, R, N=22):         # calc nodes and boundary values
    inode, bnode, b = [], [], []    # intnl, bndry nodes, bndry values
    x, y = np.linspace(0,L,N+1), np.linspace(0,L,N+1)   # same x,y grids
    for j in range(N+1):
        for i in range(N+1):
            r2 = (x[i]-L/2.)**2 + (y[j]-L/2.)**2
            if (i==0 or i==N or j==0 or j==N or r2<=R*R):
                bnode.append([x[i], y[j]])          # bndry node 
                b.append(1. if r2<=R*R else 0.)
            else:   
                inode.append([x[i], y[j]])
    ni, node = len(inode), inode+bnode              # combine nodes 
    return np.array(node), [0.]*ni+b, ni, len(node)
    
def phi(i, r):              # Gaussian $\phi_i$ and $\nabla^2 \phi_i$
    r2, e2 = (node[i,0]-r[0])**2 + (node[i,1]-r[1])**2, eps*eps
    f = np.exp(-e2*r2)
    return f, 4*e2*f*(e2*r2-1)    

def rbf_mat(ni, nt):        # fills matrix $A_{ij} = \nabla^2_j \phi_i$ or $\phi_{ij}$
    A = np.zeros((nt, nt))
    for j in range(nt):
        f, df = phi(np.arange(nt), node[j])  # vector operation 
        A[j,:] = df if j < ni else f
    return A    

def usum(a, x, y):          # calc u at (x,y)
    u = 0.
    for i in range(len(a)):
        u += a[i]*phi(i, [x, y])[0]     # [0]= first return value 
    return u
        
L, R, eps = 1.0, 0.25, 20.  # sizes of square, disk; shape parameter

node, b, ni, nt = initialize(L, R)      # ni, nt = num. intrnl/tot nodes
A = rbf_mat(ni, nt)
ai = solve(A, b)            # solve 

x = np.linspace(0, L, 41)   # same x,y plotting grids
x, y = np.meshgrid(x, x)
u = usum(ai, x, y)

plt.figure()
img = plt.imshow(u, cmap=plt.cm.jet)    # plot as image     
plt.colorbar(img), plt.axis('off')
plt.show()   
   
