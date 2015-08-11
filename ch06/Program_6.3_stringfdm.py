#
# Program 6.3: String under external forces (stringfdm.py)
# J Wang, Computational modeling and visualization with Python
#

from scipy.linalg import solve       # SciPy linear eqn solver
import numpy as np, matplotlib.pyplot as plt

N, u0, uN= 20, 0., 0.           # number of intervals, boundary values
x = np.linspace(0., 1., N+1)    # grid
h, T, f = x[1]-x[0], 1.0, -1.0  # bin size, tension, load

A = np.diag([-2.]*(N-1))        # diagonal 
A += np.diag([1.]*(N-2),1) + np.diag([1.]*(N-2),-1) # off diagonals
    
B = np.array([-h*h*f/T]*(N-1))          # B matrix
B[0], B[-1] = B[0]-u0, B[-1]-uN         # boundary values, just in case

u = solve(A, B)                         # solve     
u = np.insert(u, [0, N-1], [u0, uN])    # insert BV at 1st and last pos 

plt.plot(x, u, label='$f=-1$'),  plt.legend(loc='center')   # legend 
plt.xlabel('$x$'), plt.ylabel('$u$'), plt.show()
