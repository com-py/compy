#
# Program 5.1: Logistic map (logisticmap.py)
# J Wang, Computational modeling and visualization with Python
#

from __future__ import print_function       # use print() as function
import matplotlib.pyplot as plt     # get matplotlib plot functions
import sys

if (sys.version_info[0] < 3):
    x, r = input('enter x0, r: ')
else:
    x, r = eval(input('enter x0, r: '))
n, xn = 40, []
for i in range(n):
    xn.append(x)                    # new line every 4 steps
    print('%8f' %x, end='\n' if len(xn)%4==0 else ' ') # inline if 
    x = 4*r*x*(1.0-x)               # next iteration, logistic map
    
plt.figure()
plt.plot(range(n), xn, '--o')       # plot dashed line with 'o' symbol
plt.xlabel('$n$'), plt.ylabel('$x_n$')
plt.ylim(0,1), plt.text(33, .1, 'r='+ repr(r))   # add text 
plt.show()
