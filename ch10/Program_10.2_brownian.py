#
# Program 10.2: Brownian motion (brownian.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np, random as rnd
import matplotlib.pyplot as plt
import matplotlib.animation as am

class BrownianMotion:               # Brownian motion class
    def __init__(self, N=400, F=0.005, b=0.1, tau=2., h = 0.5):
        self.N, self.F, self.b, self.tau, self.h = N, F, b, tau, h
        self.r, self.v = np.zeros((N, 2)), np.zeros((N, 2))
        self.t = -np.log(np.random.rand(N))*tau     # initial kick times

    def move(self, r, v, dt):       # move between kicks
        edt = np.exp(-self.b*dt)
        return r + v*(1-edt)/self.b, v*edt

    def iterate(self):              # advance one step
        r, v, t, h, F = self.r, self.v, self.t, self.h, self.F  # alias
        for i in range(self.N):
            if t[i] > h:            # no kick within current step
                dt = h              # dt= time to end of step
            else:                   # suffers kicks before end of step
                tot, dt = 0., t[i]  # tot=time to last kick
                while t[i] <= h:
                    r[i], v[i] = self.move(r[i], v[i], dt)
                    phi = rnd.random()*2*np.pi              # apply kick
                    v[i] += [F*np.cos(phi), F*np.sin(phi)] 
                    tot += dt
                    dt = -np.log(rnd.random())*self.tau     # sample dt
                    t[i] += dt      # next kick
                dt = h - tot        # dt= to end of current step
            r[i], v[i] = self.move(r[i], v[i], dt)  # no kick, just move
            t[i] -= h
 
def updatefig(*args):                       # update figure data
    bm.iterate()
    plot.set_data(bm.r[:,0], bm.r[:,1])     # update data
    return [plot]                           # return plot object
 
bm = BrownianMotion()                       # create Brownian model
fig = plt.figure()
plt.subplot(111, aspect='equal')
plot = plt.plot(bm.r[:,0], bm.r[:,1], 'o')[0]     # create plot object
ani = am.FuncAnimation(fig, updatefig, interval=10, blit=True) # animate 
plt.xlim(-1., 1.), plt.ylim(-1., 1.), plt.show()
