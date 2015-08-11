#
# Program 12.1: Deflection function (deflect.py)
# J Wang, Computational modeling and visualization with Python
#

import matplotlib.pyplot as plt
import numpy as np, rootfinder as rtf, integral as itg

def V(r):           # plum potential
    return Z*(3-r*r/(R*R))/(R+R) if (r<R) else Z/r

def fu(u):          # f(u), turning point eqn
    return 1 - V(1./u)/E - b*b*u*u
   
def fx(x):          # integrand, called by gauss
    u = umin - x*x
    return 2*x*b/np.sqrt(fu(u))

def xection(theta, ba, da):     # cross section
    cs = 0.0                    # ba=impact para, da=deflection angle
    for i in range(len(ba)-1):
        if ((theta-da[i])*(theta-da[i+1]) < 0.):   # theta bracketed 
            db = ba[i+1] - ba[i]
            cs += (ba[i] + db/2.)*abs(db/(da[i+1]-da[i]))
    return cs/np.sin(theta)
    
Z, R = 1.0, 1.0     # nuclear charge Z,  radius of plum potential
E, b, bmax = 1.2, 0.01, 20.             # energy, initial b, bmax
eps, tiny =1.E-14, 1.E-5                # rel error, u-limit
ba, theta = [], []                      # impact para, deflection
while (b <= bmax):
    umin = rtf.bisect(fu, tiny, 1./b, eps)   # find turning pt
    alpha = itg.gauss(fx, 0., np.sqrt(umin))
    ba.append(b), theta.append(np.pi - 2*alpha)
    b *= 1.02
    
plt.figure(), plt.plot(ba, theta)       # plot deflection function
plt.xlabel('$b$ (a.u.)'), plt.ylabel('$\Theta$', rotation=0)
plt.yticks([0, np.pi/2, np.pi], ['$0$','$\pi/2$', '$\pi$'])
plt.xlim(0,3)

cs, sa = [], np.linspace(0.01, np.pi-.01, 500)  # scattering angle
for x in sa:                            # calc, plot cross section
    cs.append(xection(x, ba, theta))
plt.figure(), plt.plot(sa, cs)
plt.xlabel(r'$\theta$'), plt.ylabel(r'$\sigma(\theta)$')
plt.xticks([0, np.pi/2, np.pi], ['$0$','$\pi/2$', '$\pi$'])
plt.xlim(0, np.pi),  plt.semilogy()

plt.show()
