#
# Program 5.6: Poincar\'e map (poincare.py)
# J Wang, Computational modeling and visualization with Python
#

import matplotlib.pyplot as plt     # get matplotlib plot functions
import ode, math as ma              # get ODE, math functions 

def remap(x):        # remap theta to [-pi,pi]
    if (abs(x) > pi): x = (x - 2*pi if x>0 else x + 2*pi)
    return x

def pendulum(y, t):  # y = [theta, omega], omega_0 = 1
    return [y[1], -ma.sin(y[0]) - b*y[1] + fd*ma.cos(omega_d*t)]
    
def poincare(transient, n_periods):    # transient periods, n_periods
    bins = 40               # number of points per period 
    t, y, h = 0.0, [0.6, 0.0], 2*pi/(omega_d*bins)  # init values
    theta, omega = [], []
    for i in range(bins*transient):    # discard transients
        t, y = t+h, ode.RK4n(pendulum, y, t, h)
        y[0] = remap(y[0])
    for i in range(bins*n_periods):
        if (i%(bins//2) == 0):         # record every half a period 
            theta.append(y[0]), omega.append(y[1])
        t, y = t+h, ode.RK4n(pendulum, y, t, h)
        y[0] = remap(y[0])
        
    return theta, omega

b, omega_d = 0.5, 0.6       # damping coeff., driving frequency
subnum, pi = 1, ma.pi       # subplot number, pi
plt.figure()
for fd in [0.7, 1.1, 1.2]: 
    theta, omega = poincare(transient = 20, n_periods = 400)
    ax = plt.subplot(3, 1, subnum)     # 3x1 subplots
    ax.plot(theta, omega, '.'), ax.set_xlim(-pi, pi)
    if (subnum == 2): ax.set_ylabel('$\\omega$ (rad/s)')
    subnum, fdtxt = subnum + 1, '$F_d=$'+repr(fd)
    ax.text(-3, min(omega), fdtxt)
    
plt.xlabel('$\\theta$ (rad)')
plt.show()

