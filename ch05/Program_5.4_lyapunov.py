#
# Program 5.4: Lyapunov exponent of logistic map (lyapunov.py)
# J Wang, Computational modeling and visualization with Python
#

import matplotlib.pyplot as plt     # get matplotlib plot functions
import math as ma                   # get math functions 

def lyapunov(r):                    # compute Lyapunov exponent
    sum, x, ntrans, nsteps = 0.0, 0.5, 2000, 2000     # try diff num.
    for i in range(ntrans):         # let transients pass
        x = 4*r*x*(1-x)     
    for i in range(nsteps):         # sum up next n steps
        x = 4*r*x*(1-x) 
        dfdx = 4.0*r*(1.0-x-x)      # 
        sum += ma.log(abs(dfdx))
    return sum/float(nsteps)        # lambda 
    
ra, lyap, r, dr = [], [], 0.7, 0.0001
while r < 1.0: 
    r = r + dr
    ra.append(r), lyap.append(lyapunov(r))
    
plt.figure()
plt.plot(ra, lyap, ',')             # ','=pixels
plt.axhline(0.), plt.ylim(-2, 1)    # draw horiz. line, set y limits
plt.xlabel('$r$'), plt.ylabel('$\lambda$')
plt.show()
   
