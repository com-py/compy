#
# Program 3.3: Range vs. angle (range.py)
# J Wang, Computational modeling and visualization with Python
#

import rootfinder as rtf, math as ma   # get root finders, math
import matplotlib.pyplot as plt # get matplotlib plot functions

def f(R):                       # range function, 
    return R*(vy+g/b)/vx + g*ma.log(1.-b*R/vx)/(b*b)

g, b, v0 = 9.8, 1.0, 100.       # g, linear coeff., firing speed
x, y, dtr = [], [], ma.pi/180.  # temp arrays, deg-to-rad conv

for theta in range(1,90):
    vx, vy = v0*ma.cos(theta*dtr), v0*ma.sin(theta*dtr) # init vel
    R = rtf.bisect(f, 0.01, vx/b-1.e-5, 1.e-6)       # solve 
    if (R != None): x.append(theta), y.append(R)
    
plt.figure()                    # open fig, plot, label, show fig
plt.plot(x, y), plt.xlabel('angle (deg)'), plt.ylabel('R (m)')
plt.show()
