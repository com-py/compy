#
# Program 9.8: Triangle-mesh plotting of wave function (tripwf.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np, pickle, fileio
import matplotlib.pyplot as plt

meshfile, eigenfile = 'meshdata.txt', 'eigendata.dat'   # data files
node, elm, bp, ip = fileio.readmesh(meshfile)
file = open(eigenfile, 'rb')            # read pickled eigendata, rev. "rb" mode
E, u = pickle.load(file)
file.close()

node, st = np.asarray(node), range(12)  # change st for other states
fig = plt.figure()
for n in range(len(st)):
    wf = u[:, st[n]]
    for i in bp:                        # bp should be sorted
        wf = np.insert(wf, i, 0.)       # add boundary values, 
    ax = fig.add_subplot(4, 3, n+1, aspect='equal')     # 4x3 plots
    plt.tripcolor(node[:,0], node[:,1], wf, shading='gouraud')
    plt.title(repr(st[n]+1)), plt.axis('off')
    
plt.show()
