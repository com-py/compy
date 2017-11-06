#
# Program 5.7: Mandelbrot fractal (fractal.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np, matplotlib.pyplot as plt
from numba import jit               # comment out if jit not available
@jit                                # just-in-time compiling
def mandelbrot(c, maxi):
    z = c
    for m in range(maxi):           # maxi=max iterations
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag >=4.0): break
    return m
    
xl, xr, yb, yt = -2.2, 0.8, -1.2, 1.2           # box size
nx, ny, maxi = 600, 481, 100
x, y = np.linspace(xl,xr,nx), np.linspace(yb,yt,ny)
fractal = np.zeros((ny, nx, 3))                 # fractal RGB image
for i in range(nx):
    for k in range(ny):
        m = mandelbrot(x[i] + 1j*y[k], maxi)    # point in complex plane
        fractal[k, i] = [m, 2*m, 3*m]           # RGB color mix
plt.imshow(fractal/maxi, extent=[xl,xr,yb,yt])  # plot as image
plt.show()
