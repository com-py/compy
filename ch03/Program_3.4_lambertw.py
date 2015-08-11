#
# Program 3.4: Lambert W function (lambertw.py)
# J Wang, Computational modeling and visualization with Python
#

import math as ma               # import math library
def lambertw(x, branch = 0):    # branch = 0 or -1
    if (x<-1.0/ma.e or branch<0 and x>=0.0): return None # bad arg
    w, nmax = x, 20
    if (x > 1.5 or branch == -1): w = ma.log(abs(x))
    
    for i in range(nmax):
        w, v = (w*w + x*ma.exp(-w))/(1.0+w), w  # 
        if (abs(w-v) <= 1.e-15*abs(w)): break   # to double precision
    return w
