#
# Program 4.7: Restricted three-body (r3body.py)
# J Wang, Computational modeling and visualization with Python
#

import ode, numpy as np     # get ODE solvers, numpy
import visual as vp         # get VPython modules for animation

def r3body(y, t):   # equations of motion for restricted 3body
    r, v = y[0], y[1]
    r1, r2 = r - [-a,0], r - [b,0]  # rel pos vectors 
    acc = -GM*(b*r1/vp.mag(r1)**3 + a*r2/vp.mag(r2)**3) # 
    acc += omega**2*r + 2*omega*np.array([v[1], -v[0]]) # Coriolis term 
    return np.array([v, acc])

def set_scene(r):   # r = position of test body
    vp.display(title='Restricted 3body', background=(1,1,1))
    body = vp.sphere(pos=r, color=(0,0,1), radius=0.03, make_trail=1)
    sun = vp.sphere(pos=(-a,0), color=(1,0,0), radius=0.1)
    jupiter = vp.sphere(pos=(b, 0), color=(0,1,0), radius=0.05)
    circle = vp.ring(pos=(0,0), color=(0,0,0), thickness=0.005,
                     axis=(0,0,1), radius=1)      # unit circle
    return body
    
def restricted_3body(y):            # y = [r, v] expected
    testbody = set_scene(y[0])
    t, h = 0.0, 0.001
    while True:
        vp.rate(2000)
        y = ode.RK4(r3body, y, t, h)
        testbody.pos = y[0]

GM, omega = 4*np.pi**2, 2*np.pi     # G(M1+M2), omega, RTB units
alpha = 0.0009542                   # Sun-Jupiter system
a, b = alpha, 1.0-alpha
r, v = [0.509046,0.883346], [0.162719,-0.0937906]     # init pos, vel
restricted_3body(np.array([r, v]))
