#
# Program 7.8: Angular distribution of dipole radiation (dipole.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

theta = np.linspace(0, np.pi, 21)
phi   = np.linspace(0, 2*np.pi, 41)
theta, phi = np.meshgrid(phi, theta)
x = np.sin(theta)*np.cos(phi)
y = np.sin(theta)*np.sin(phi)
z = np.sin(theta)*np.cos(theta)     # z=radial times cos(theta) 

plt.figure()
ax = plt.subplot(111, projection='3d', aspect=.5)
ax.plot_surface(x, y, z,  rstride=1, cstride=1, color='w')
plt.axis('off')
plt.show()
