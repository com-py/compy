#
# Program 5.3: Initial value dependence of logistic map (logisdiff.py)
# J Wang, Computational modeling and visualization with Python
#

import matplotlib.pyplot as plt     # get matplotlib plot functions
import sys

if (sys.version_info[0] < 3):
    x1, r = input('enter x1, r; eg .4, .7 : ')
else:
    x1, r = eval(input('enter x1, r; eg .4, .7 : '))
x2 = x1 + 0.01              # initial difference
n, xn1, xn2, diff = 20, [], [], []                 # buffers
for i in range(n):
    xn1.append(x1), xn2.append(x2), diff.append(abs(x1-x2))
    x1, x2 = 4*r*x1*(1.0-x1), 4*r*x2*(1.0-x2)      # parallel iterates
    
plt.figure()                # plot the series
plt.plot(range(n), xn1, 's-', range(n), xn2,'o-')  # squares & circles
plt.xlabel('$n$'), plt.ylabel('$x_n$')
plt.text(3, .01+min(xn1),'$r=$' + repr(r))

plt.figure()                # plot the difference
plt.plot(range(n), diff)
plt.semilogy()              # semilog scale
plt.xlabel('$n$'),  plt.ylabel('$\Delta x$')
plt.show()
