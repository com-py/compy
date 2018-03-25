#
# Program 9.7: Quantum dot (qmdot.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np, pickle, fileio, fem
import matplotlib.pyplot as plt
from scipy.sparse.linalg import eigsh
from mpl_toolkits.mplot3d import Axes3D
 
nt, n = 12, 0       # nt = tot num of states, n=state to plot
meshfile, eigenfile = 'meshdata.txt', 'eigendata.dat'   # data files
node, elm, bp, ip = fileio.readmesh(meshfile)
print ('nodes/elements', len(bp), len(ip), len(elm))

try:
    file = open(eigenfile, 'r')          # if prev eigen data exists,
    E, u = pickle.load(file)             # read from file       
except IOError:
    Tm = 0.5*fem.A_mat(node, elm)        # no eigendata, recalculate
    B  = fem.B_mat(node, elm)
    Tm = np.delete(Tm, bp, axis=0)       # delete boundary rows
    Tm = np.delete(Tm, bp, axis=1)       # delete boundary cols
    B = np.delete(B, bp, axis=0)         
    B = np.delete(B, bp, axis=1)         
    E, u = eigsh(Tm, nt, B, which='SA')  # solve
    file = open(eigenfile, 'w')          # file overwritten     
    pickle.dump((E, u), file)            # 
file.close()

print (E)                                # print E, prep for wf
node, wf = np.asarray(node), u[:,n]
for i in bp: wf = np.insert(wf, i, 0.)   # add boundary values

plt.figure()                             # draw mesh
plt.subplot(111, aspect='equal')
plt.triplot(node[:,0], node[:,1], elm, 'o-', linewidth=1)
plt.xlabel('$x$', size=20), plt.ylabel('$y$', size=20)

fig = plt.figure()                       # plot wave function
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(node[:,0],node[:,1], wf, cmap=plt.cm.jet, linewidth=.2)
plt.axis('off')

plt.show()

