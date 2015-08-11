#
# Program 11.4: Equilibrium energy sharing (equishare.py)
# J Wang, Computational modeling and visualization with Python
#

from einsteinsolid import EinsteinSolid
import matplotlib.pyplot as plt, numpy as np
import matplotlib.animation as am

def updateimg(*args):                   # args[0] = frame
    L = 20 if args[0]<400 else 200      # slower init rate
    solid.exchange(L)
    plot.set_data(np.reshape(solid.cell, (K,K)))  # update image
    return [plot]                       # return line object in a list
    
K = 20                                  # grid dimension
solid = EinsteinSolid(N = K*K, q=10)    # 10 units of energy/cell
fig = plt.figure()
img = np.reshape(solid.cell, (K,K))     # shape to KxK image
plot = plt.imshow(img, interpolation='none', vmin=0, vmax=50)
plt.colorbar(plot)

anim = am.FuncAnimation(fig, updateimg, interval=1, blit=True)  # animate
plt.show()
