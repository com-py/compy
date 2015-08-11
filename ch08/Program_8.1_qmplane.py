#
# Program 8.1: A quantum plane wave (qmplane.py)
# J Wang, Computational modeling and visualization with Python
#

import matplotlib.pyplot as plt, numpy as np
import matplotlib.animation as am

def updatefig(*args):                       # args[0] = frame
    wf = np.exp(1j*(x-0.1*args[0]))         # traveling plane wave
    w = [prob, wf.real, wf.imag]
    for i in range(len(w)):
        plot[i].set_data(x, w[i])           # update data 

x = np.linspace(-2*np.pi, 2*np.pi, 101)
wf, prob = np.exp(1j*x), [1]*len(x)
fig = plt.figure()
plot = plt.plot(x,prob, x,wf.real, x,wf.imag)           # plot object 
ani = am.FuncAnimation(fig, updatefig, interval=10)     # animate 
plt.ylim(-1.2, 1.2),  plt.show()
