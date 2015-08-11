# Common library file to be placed in the Python path (e.g., C:\Python27)
#
# Program: ODE solvers library (ode.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np      # numpy

def Euler(diffeq, y0, t, h): # uses docstring """..."""
    """ Euler's method for n ODEs:
        Given y0 at t, returns y1 at t+h """
    dydt = diffeq(y0, t)     # get {dy/dt} at t
    return y0 + h*dydt       # Euler method on a vector  @\lbl{line:vecop}@
 
def RK2(diffeq, y0, t, h):
    """ RK2 method for ODEs:
        Given y0 at t, returns y1 at t+h """
    k1 = h*diffeq(y0, t)                # get dy/dt at t first
    k2 = h*diffeq(y0+0.5*k1, t + h/2)   # get dy/dt at t+h/2,
    return y0 + k2                      # calc. y1 = y(t+h)
    
def RK4(diffeq, y0, t, h):
    """ RK4 method for ODEs:
        Given y0 at t, returns y1 at t+h """
    k1 = h*diffeq(y0, t)                    # dy/dt at t
    k2 = h*diffeq(y0+0.5*k1, t + h/2.)      # dy/dt at t+h/2
    k3 = h*diffeq(y0+0.5*k2, t + h/2.)      # dy/dt at t+h/2
    k4 = h*diffeq(y0+k3, t + h)             # dy/dt at t+h
    return y0 + (k1+k4)/6.0 + (k2+k3)/3.0
    
def RK4n(diffeq, y0, t, h):     # non-vectorized with lists
    """ RK4 method for n ODEs: 
        Given y0 at t, returns y1 at t+h """
    n, y1 = len(y0), [0.0]*len(y0)        
    k1 = diffeq(y0, t)                   # dy/dt at t
    for i in range(n):                   # loop thru n ODEs
        y1[i] = y0[i] + 0.5*h*k1[i]      # prep for k2[]
    k2 = diffeq(y1, t + h/2.)            # dy/dt at t+h/2
    for i in range(n):
        y1[i] = y0[i] + 0.5*h*k2[i]
    k3 = diffeq(y1, t + h/2.)            # dy/dt at t+h/2
    for i in range(n):
        y1[i] = y0[i] + h*k3[i]
    k4 = diffeq(y1, t + h)               # dy/dt at t+h
    for i in range(n):              
        y1[i] = y0[i] + h*(k1[i]+2*k2[i]+2*k3[i]+k4[i])/6.0
    return y1

def RK45(diffeq, y0, t, h):      # RK45 method
    a2, a3, a4, a5, a6 = 0.2, 0.3, 0.6, 1.0, 0.875
    b21, b31, b32, b41, b42, b43 = 0.2, 3./40., 9./40., 0.3, -0.9, 1.2
    b51, b52, b53, b54 = -11./54., 2.5,  -70./27., 35./27.
    b61, b62, b63, b64, b65 = [1631./55296., 175./512., 575./13824.,
                               44275./110592., 253./4096.]
    c1, c3, c4, c6 = 37./378., 250./621., 125./594., 512./1771.
    
    k1 = h*diffeq(y0, t)
    k2 = h*diffeq(y0 + b21*k1, t + a2*h)
    k3 = h*diffeq(y0 + b31*k1 + b32*k2, t + a3*h)
    k4 = h*diffeq(y0 + b41*k1 + b42*k2 + b43*k3, t + a4*h)
    k5 = h*diffeq(y0 + b51*k1 + b52*k2 + b53*k3 + b54*k4, t + a5*h)
    k6 = h*diffeq(y0 + b61*k1 + b62*k2 + b63*k3 + b64*k4 
                                                + b65*k5, t + a6*h)
    return y0 + c1*k1 + c3*k3 + c4*k4 + c6*k6
    
def RK45n(diffeq, y0, t, h):      # RK45 method, based on NR, Press
    a2, a3, a4, a5, a6 = 0.2, 0.3, 0.6, 1.0, 0.875
    b21, b31, b32, b41, b42, b43 = 0.2, 3./40., 9./40., 0.3, -0.9, 1.2
    b51, b52, b53, b54 = -11./54., 2.5,  -70./27., 35./27.
    b61, b62, b63, b64, b65 = [1631./55296., 175./512., 575./13824.,
                               44275./110592., 253./4096.]
    c1, c3, c4, c6 = 37./378., 250./621., 125./594., 512./1771.
    
    n, y1 = len(y0), [0.0]*len(y0)
    k1 = diffeq(y0, t)
    for i in range(n):
        y1[i] = y0[i] + h*b21*k1[i]
    k2 = diffeq(y1, t + a2*h)
    for i in range(n):             
        y1[i] = y0[i] + h*(b31*k1[i] + b32*k2[i])
    k3 = diffeq(y1, t + a3*h)
    for i in range(n):             
        y1[i] = y0[i] + h*(b41*k1[i] + b42*k2[i] + b43*k3[i])
    k4 = diffeq(y1, t + a4*h)
    for i in range(n):             
        y1[i] = y0[i] + h*(b51*k1[i] + b52*k2[i] + b53*k3[i] + b54*k4[i])
    k5 = diffeq(y1, t + a5*h)
    for i in range(n):             
        y1[i] = y0[i] + h*(b61*k1[i] + b62*k2[i] + b63*k3[i] + b64*k4[i]
                         + b65*k5[i])
    k6 = diffeq(y1, t + a6*h)
    for i in range(n): 
        y1[i] = y0[i] + h*(c1*k1[i] + c3*k3[i] + c4*k4[i] + c6*k6[i])
    return y1


def leapfrog(lfdiffeq, r0, v0, t, h):       # vectorized leapfrog
    """ vector leapfrog method using numpy arrays.
        It solves general (r,v) ODEs as: 
        dr[i]/dt = f[i](v), and dv[i]/dt = g[i](r).
        User supplied lfdiffeq(id, r, v, t) returns
        f[i](r) if id=0, or g[i](v) if id=1.
        It must return a numpy array if i>1 """
    hh = h/2.0
    r1 = r0 + hh*lfdiffeq(0, r0, v0, t)     # 1st: r at h/2 using v0    @\lbl{line:lf1}@
    v1 = v0 +  h*lfdiffeq(1, r1, v0, t+hh)  # 2nd: v1 using a(r) at h/2 @\lbl{line:lf2}@
    r1 = r1 + hh*lfdiffeq(0, r0, v1, t+h)   # 3rd: r1 at h using v1     @\lbl{line:lf3}@
    return r1, v1
  
def leapfrog_tt(lfdiffeq, r0, v0, t0, w0, h):
    """ vectorized leapfrog_tt with time transformation, 
        Omega=1/r, that solves general (r,v) ODEs as: 
        dr[i]/dt = f[i](v), and dv[i]/dt = g[i](r).
        User supplied lfdiffeq(id, r, v, t) returns
        f[i](r) if id=0, or g[i](v) if id=1 """
    # 1st step: calc r at h/2
    hw = h/(2.0*w0)                         # half h/2w0
    t1 = t0 + hw                       
    r1 = r0 + hw*lfdiffeq(0, r0, v0, t0)    # id=0, get $\vec{r}_{1/2}$
    r2 = np.dot(r1, r1)                     # get r^2=x*x+y*y+z*z
    r12 = np.sqrt(r2)                       # $r_{1/2}$
    
    # 2nd step: calc v1 using r at h/2
    v1 = v0 + h*r12*lfdiffeq(1, r1, v0, t1) # id=1 for g(r) at h/2 
    rdotv = np.dot(r1, v0+v1)/2.            # $\vec{r}\cdot\vec{v}_{1/2}$
    w1 = w0 - rdotv*h/r2                    # $ w_0 - \vec{r}\cdot\vec{v}_{1/2} h /r^2$
       
    # 3rd step: calc r by another 1/2 step using v1
    hw = h/(2.0*w1)
    t1 = t1 + hw
    r1 = r1 + hw*lfdiffeq(0, r1, v1, t1)    # get $\vec{r}_{1}$ at t+h 
    return r1, v1, t1, w1

def leapfrog_ttN(lfdiffeq, r, v, t, w, h):
    """ N-body leapfrog with time transformation, 
        Omega= \sum 1/r_{ij} """
    hw = h/(2.0*w)                  # 1st step: calc r at h/2
    r += v*hw
    t += hw                       
    
    a, Omega, Gamma = lfdiffeq(1, r, v, t)      # calc. a, $\Omega, \nabla \Omega$
    hw = h/Omega                    # 2nd step, 
    v1 = v + a*hw
    w += np.sum(Gamma*(v+v1))*hw*0.5            # calc. $\sum \Gamma \cdot v$
    
    hw = h/(2.0*w)                  # 3rd step: calc r at h
    t += hw
    r += v1*hw
    return r, v1, t, w
     
     
def numerov(f, u, n, x, h):     # Numerov integrator for $u''+f(x)u=0$
    nodes, c = 0, h*h/12.       # given $[u_0,u_1]$, return $[u_0,u_1,...,u_{n+1}]$
    f0, f1 = 0., f(x+h)
    for i in range(n):
        x += h
        f2 = f(x+h)             # Numerov method below, @\eqn{numerov}@d
        u.append((2*(1-5*c*f1)*u[i+1] - (1+c*f0)*u[i])/(1+c*f2))  
        f0, f1 = f1, f2
        if (u[-1]*u[-2] < 0.0): nodes += 1
    return u, nodes
