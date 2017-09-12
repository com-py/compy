#
# Program 7.1: Electric field hockey (hockey.py)
# J Wang, Computational modeling and visualization with Python
#

import visual as vp, numpy as np, ode
import sys

def hockey(Y, t):               # return eqn of motion
    accel = 0.
    for i in range(len(loc)):
        accel += Q[i]*(Y[0]-loc[i])/(vp.mag(Y[0]-loc[i]))**3
    return [Y[1], q*accel]      # list for non-vectorized solver

a, b, w = 1., 0.5, 0.125                  # rink size, goal width
q, qcor, qmid, qcen = -1.0, 1.0, -2., 2.  # Qs: puck, cor., mid, cen.
Q = [qcor, qmid, qcor, qcor, qmid, qcor, qcen]  # charges, locations
loc = [[-a, b], [0, b], [a, b], [a,-b], [0,-b], [-a,-b], [0,0]]

scene = vp.display(title='Electric hockey', background=(.2,.5,1))
puck  = vp.sphere(pos=(-a,0,0), radius = 0.05, make_trail=True) # trail 
rink  = vp.curve(pos=loc[:-1]+[loc[0]], radius=0.01)    # closed curve
goalL = vp.curve(pos=[(-a,w,0),(-a,-w,0)], color=(0,1,0), radius=.02)
goalR = vp.curve(pos=[( a,w,0),( a,-w,0)], color=(0,1,0), radius=.02)
for i in range(len(loc)):       # charges, red if Q>0, blue if Q<0
    color = (1,0,0) if Q[i]>0 else (0,0,1)  
    vp.sphere(pos=loc[i], radius = 0.05, color=color)

if (sys.version_info[0] < 3):
    v, theta = input('enter speed, theta; eg, 2.2, 19:')   # try 2.2, 18.5
else:
    v, theta = eval(input('enter speed, theta; eg, 2.2, 19:'))
v, theta = min(4, v), max(1,theta)*np.pi/180.      # check valid input
Y = np.array([[-a,0], [v*np.cos(theta), v*np.sin(theta)]])
while True:
    vp.rate(200)
    Y = ode.RK45n(hockey, Y, t=0., h=0.002)
    x, y = Y[0][0], Y[0][1]
    if (abs(x) > a or abs(y) >b): 
        txt = 'Goal!' if (x > 0 and abs(y) < w) else 'Miss!'
        vp.label(pos=(x, y+.2), text=txt, box=False)
        break
    puck.pos = Y[0]
