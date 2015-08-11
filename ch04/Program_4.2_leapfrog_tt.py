#
# Program 4.2: Leapfrog with time transformation (leapfrog_tt.py)
# J Wang, Computational modeling and visualization with Python
#

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
