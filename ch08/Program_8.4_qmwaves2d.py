#
# Program 8.4: Quantum waves in 2D (qmwaves2d.py)
# J Wang, Computational modeling and visualization with Python
#

import matplotlib.pyplot as plt
import numpy as np, visual as vp, vpm

def initialize(a=10., N=12, nx=40, ny=40):  # size, max QM num, grid
    s, x0, y0 = 1.9, a/2, a/2               # width, center of wavepacket
    na, pi = np.arange(1, N+1), np.pi       # QM numbers
    En = pi*pi*na**2/(2*a*a)                # all eigenenergies
    x, y = np.linspace(0,a,nx), np.linspace(0,a,ny)     # grid
    X, Y = np.meshgrid(x, y)
    umx, uny = np.zeros((N,ny,nx)), np.zeros((N,ny,nx))
    for n in range(N):                      # compute basis functions
        umx[n] = np.sqrt(2/a)*np.sin((n+1)*pi*X/a)
        uny[n] = np.sqrt(2/a)*np.sin((n+1)*pi*Y/a)
    amn0 = expansion(a, na, s, x0, y0)      # expansion coeff.
    return a, N, En, amn0, X, Y, umx, uny
    
def expansion(a, n, s, x0, y0):     # calc expansion coefficients
    r, q, pi = s/a, n*s/a, np.pi    # warning: 'a/s' must not be integer
    cm = np.cos(q*pi/2)*np.sin(n*pi*x0/a)/((1-q)*(1+q))
    cn = np.cos(q*pi/2)*np.sin(n*pi*y0/a)/((1-q)*(1+q))
    return 16*r*np.outer(cm, cn)/(pi*pi)    # amn(0) 

def psi(amn0, t):                   # calc wavefunction at time t
    wf, phase = 0.0, np.exp(-1j*En*t)
    amnt = amn0*np.outer(phase, phase)      # $a_{mn}(t)=a_{mn}(0)e^{-i E_{mn} t}$
    for m in range(N):
        s = 0.0
        for n in range(N): s += amnt[m,n]*uny[n]    # vector operation
        wf += s*umx[m]                      # $\sum a_{mn} u_m(x) u_n(y)$
    return wf
    
t, num, plot = 0., 1, False         # set plot=False to animate forever
time = [0.0, 0.5, 0.9, 1.4, 2.0, 3.0, 40, 63.7, 64.2]   # snapshots
a, N, En, amn0, X, Y, umx, uny = initialize()
    
scene = vp.display(background=(.2,.5,1), center=(a/2,a/2,-0.5),
                   up=(0,0,1), forward=(1,2,-1))
mesh = vpm.mesh(X, Y, 0*X, vp.color.yellow, vp.color.red)
info = vp.label(pos=(a/4, .8*a,1), height=20)
while True:
    wf = psi(amn0, t)
    mesh.move(X, Y, wf.real*3)      # show real part, times 3
    info.text='%5.2f' %(t)
    vpm.wait(scene), vp.rate(40)
    if (plot):
        plt.subplot(3, 3, num)
        plt.imshow(np.abs(wf)**2, cmap=plt.cm.jet)  # try contourf()
        plt.xticks([],[]), plt.yticks([],[])        # omit ticks 
        plt.xlabel('t=%s' %(t))
        if (num > len(time)-1): break
        t, num = time[num], num+1
    else:
        t = t + 0.05
if (plot): plt.show()
