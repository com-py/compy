#
# Program 12.2: Partial wave method (qmscatt.py)
# J Wang, Computational modeling and visualization with Python
#

import scipy
if scipy.__version__[0] < '1':  # sph. Bessel func changed after ver 1.0.0
    from scipy.special import sph_jn, sph_yn, lpn
else:
    from scipy.special import spherical_jn as sph_jn, spherical_yn as sph_yn, lpn
import matplotlib.pyplot as plt, numpy as np, ode

def V(r):                       # Yukawa potential
    Z, sa = 2., 1.0             # nuclear charge, screening length
    return -Z*np.exp(-r/sa)/r
    
def f(r):                       # Sch eqn in Numerov form
    return 2*(E - V(r)) - L*(L+1)/(r*r)

def wf(M, xm):                  # find w.f. and deriv at xm
    c = (h*h)/6.
    wfup, nup = ode.numerov(f, [0,.1], M, xL, h)    # 1 step past xm
    dup = ((1+c*f(xm+h))*wfup[-1] - (1+c*f(xm-h))*wfup[-3])/(h+h)
    return wfup, dup/wfup[-2]

xL, a, M = 0., 10., 200                 # limits, matching point
h, Lmax, E =(a-xL)/M, 15, 2.            # step size, max L, energy

k, ps = np.sqrt(2*E), np.zeros(Lmax+1)  # wave vector, phase shift
if scipy.__version__[0] < '1':
    jl, dj = sph_jn(Lmax, k*a)          # (j_l, j_l') tuple     
    nl, dn = sph_yn(Lmax, k*a)          # (n_l, n_l')
else:
    Lrange = range(Lmax + 1)
    jl, dj = sph_jn(Lrange, k*a, False), sph_jn(Lrange, k*a, True) # (j_l, j_l')
    nl, dn = sph_yn(Lrange, k*a, False), sph_yn(Lrange, k*a, True) # (n_l, n_l')

for L in range(Lmax+1):
    u, g = wf(M, a)                     # g= u'/u
    x = np.arctan(((g*a-1)*jl[L] - k*a*dj[L])/    # phase shift 
                  ((g*a-1)*nl[L] - k*a*dn[L]))
    while (x < 0.0): x += np.pi         # handle jumps by pi 
    ps[L] = x

theta, sigma = np.linspace(0., np.pi, 100), []
cos, La = np.cos(theta), np.arange(1,2*Lmax+2,2)
for x in cos:                               # calc cross section
    pl = lpn(Lmax, x)[0]                    # Legendre polynomial 
    fl = La*np.exp(1j*ps)*np.sin(ps)*pl     # amplitude 
    sigma.append(np.abs(np.sum(fl))**2/(k*k))
        
plt.figure()                                # plot phase shift vs L
plt.plot(range(Lmax+1), ps, '-o')
plt.xlabel('$l$'), plt.ylabel(r'$\delta_l$', fontsize=16)

plt.figure()        
plt.plot(theta*180/np.pi, sigma)            # plot cross sections   
xtck = [0, 30, 60, 90, 120, 150, 180]
plt.xticks(xtck, [repr(i) for i in xtck])   # custom ticks 
plt.xlabel(r'$\theta$ (deg)')
plt.ylabel(r'$\sigma(\theta)$ (a.u.)'), plt.semilogy()

plt.show()
