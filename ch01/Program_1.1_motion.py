#
# Program 1.1: Motion with constant acceleration (motion.py)
# J Wang, Computational modeling and visualization with Python
#

import matplotlib.pyplot as plt # get matplotlib plot functions 
import sys

if (sys.version_info[0] < 3):
    a, v0 = input('enter a, v0 (eg 1.0, 0.0) : ')   # read input 2.xx 
else:
    a, v0 = eval(input('enter a, v0 (eg 1.0, 0.0) : '))   # 3.xx
t, h, n = 0.0, 0.1, 20          # init time, step size, number of steps
ta, xa = [], []                 # time and position arrays for plotting 

for i in range(n):              # loop for n steps  
    ta.append(t)                # record time and position
    xa.append(v0*t + a*t*t/2.0)
    t = t + h                   # update time 

plt.figure()                    # start a figure; no indent->end of loop    
plt.plot(ta, xa, '-o')          # plot data
plt.xlabel('t (s)')             # add labels
plt.ylabel('x (m)')
plt.show()                      # show figure
