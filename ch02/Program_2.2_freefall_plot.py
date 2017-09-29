#
# Program 2.2: Free fall with Euler's method (freefall_plot.py)
# J Wang, Computational modeling and visualization with Python
#

import matplotlib.pyplot as plt # get matplotlib plot functions

g, h = 9.8, 0.02    # $g$, step size. Multiple assignments in one line
y, v0 = 0.0, 5.0    # initial position, velocity
ta, ya = [], []     # time and position arrays for plotting
t, yb = 0.0, []     # yb[] holds analytic solution

while t<1.0:        # loop for one second
    ta.append(t)    # record time and position
    ya.append(y)
    yb.append(v0*t-g*t*t/2.0)   # analytic solution
    v = v0 - g*t                # calc v(t)
    y = y + v*h                 # Euler's method
    t = t + h

plt.figure()                    # start a figure
plt.plot(ta,ya, ta,yb,'--')     # draw 2nd curve as dashed
plt.xlabel('t (s)')             # add labels
plt.ylabel('y (m)')
plt.show()                      # show figure
