#
# Program 7.2: Self-consistent method for parallel plates (laplace.py)
# J Wang, Computational modeling and visualization with Python
#

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import visual as vp, numpy as np, copy

def relax(V, imax=200):         # find self-consistent soln
    for i in range(imax):
        V[1:-1,1:-1] = ( V[1:-1,:-2] + V[1:-1,2:]       # left, right 
                       + V[:-2,1:-1] + V[2:,1:-1] )/4   # top, bottom
        V = set_boundary(V)     # enforce boundary condition
        draw_pot(V), vp.rate(1000)
    return V
    
def set_boundary(V):            # set interior BC values
    V[w:2*w, top], V[w:2*w, bot] = 1., -1.  # plates voltage
    return V

def draw_pot(V):                # refresh potential, slow version
    for i in range(M):
        for j in range(N):
            q = abs(V[i,j])     # graduated color mix
            if (V[i,j] >0): grid.color[N*i + j] = (q, .5*q, .2*q)
            else:           grid.color[N*i + j] = (.2*q, .5*q, q)

def draw_efield(V, scale):      # draw electric field
    Ex, Ey = np.gradient(-V)
    Emag = np.sqrt(Ex*Ex + Ey*Ey)
    for i in range(2, M-1, 2):
        for j in range(2, N-1, 2):
            vp.arrow(pos=(i,j), axis=(Ex[i,j], Ey[i,j]), 
                     length=Emag[i,j]*scale)
        vp.rate(100)
    return Ex, Ey
        
M, N, s = 61, 61, 10            # M x N = grid dim, s = point size
w, d, h = M//3, N//6, N//2      # plates width, separation, half N
bot, top = h - d//2, h + d//2   # bottom and top plates

scene = vp.display(width=M*s, height=N*s, center=(M//2,N//2))
grid = vp.points(pos=[(i,j) for i in range(M) for j in range(N)], # grid 
                 color=[(0,0,0)]*(M*N), size=s, shape='square') 

V = np.zeros((M,N))             # initialze V on grid, apply BC
V = set_boundary(V)
V = relax(V)                    # solve by relaxation

Ex, Ey = draw_efield(V, scale = 16)
V, Ex, Ey = np.transpose(V), np.transpose(Ex), np.transpose(Ey)
X, Y = np.meshgrid(range(M), range(N))

plt.figure()                    # Fig.1, contour plot
plt.contour(V, 14)
plt.quiver(X[::2,], Y[::2,], Ex[::2,], Ey[::2,],    # stride 2 in y dir
           width=0.004, minshaft=1.5, minlength=0, scale=10.)
plt.xlabel('x'), plt.ylabel('y')

plt.figure()                    # Fig.2, surface plot
ax = plt.subplot(111, projection='3d')      
ax.plot_surface(X, Y, V, rstride=1, cstride=1, cmap=plt.cm.jet, lw=0)
ax.set_xlabel('x'), ax.set_ylabel('y'), ax.set_zlabel('V')
plt.show()
