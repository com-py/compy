#
# Program 5.5: Nonlindro: Nonlinear driven oscillator (nonlindro.py)
# J Wang, Computational modeling and visualization with Python
#

import matplotlib.pyplot as plt     # get matplotlib plot functions
import ode, math as ma              # get ODE, math functions 

def pendulum(y, t):  # y = [theta, omega], omega_0 = 1
    return [y[1], -ma.sin(y[0]) - b*y[1] + fd*ma.cos(omega_d*t)]

def solution(n_periods):    # find solutions for n_periods
    bins = 40               # number of points per period         
    t, y, h = 0.0, [1.0, 0.0], 2*pi/(omega_d*bins)  # init values 
    ta, theta, omega = [], [], []
    for i in range(n_periods*bins):
        ta.append(t), theta.append(y[0]), omega.append(y[1])
        t, y = t+h, ode.RK4n(pendulum, y, t, h)
    return ta, theta, omega

b, omega_d = 0.5, 0.6       # damping coeff., driving frequency
subnum, pi = 1, ma.pi       # subplot number, pi
plt.figure()
for fd in [0.7, 1.1]: 
    ax1 = plt.subplot(2, 2, subnum)        # 2x2 subplots 
    ax2 = plt.subplot(2, 2, subnum+2)
    ta, theta, omega = solution(n_periods = 5)
    ax1.plot(ta, theta), ax2.plot(ta, omega)
    if (subnum == 1):                      # subplot specific label
        ax1.set_ylabel('$\\theta$ (rad)')
        ax2.set_ylabel('$\\omega$ (rad/s)')
    subnum, fdtxt = subnum + 1, '$F_d=$'+repr(fd)
    ax1.text(17, max(theta), fdtxt),  ax2.text(17, max(omega), fdtxt)
    plt.xlabel('t (s)')
plt.show()





