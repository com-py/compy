#
# Program 4.5: Three-body motion (3body.py)
# J Wang, Computational modeling and visualization with Python
#

import ode, rootfinder as rtf       # ode, root solvers
import visual as vp, numpy as np    # VPython, numpy
import sys
    
def threebody(id, r, v, t):         # Eqns of motion for 3-body
    if (id==0): return v            # return velocity array
    else:                           # calc acceleration
        r12, r13, r23 = r[0]-r[1], r[0]-r[2], r[1]-r[2]
        s12, s13, s23 = vp.mag(r12), vp.mag(r13), vp.mag(r23)
        a = [-m2*r12/s12**3 - m3*r13/s13**3,        # $\frac{d\vec{v}_i}{dt}$, 
              m1*r12/s12**3 - m3*r23/s23**3,
              m1*r13/s13**3 + m2*r23/s23**3]
        return np.array(a)          # return accel array
    
def quintic(x):     # Euler's quintic equation, 
    return -m1-m2 + x*(-3*m1-2*m2 + x*(-3*m1-m2
           + x*(m2+3*m3 + x*(2*m2+3*m3 + x*(m2+m3)))))

def dquintic(x):    # derivative
    return -3*m1-2*m2 + x*(2*(-3*m1-m2) + x*(3*(m2+3*m3)
            + x*(4*(2*m2+3*m3) + x*5*(m2+m3))))
    
def init_cond(scale):       # collinear initial condition
    r, v = np.zeros((3,2)), np.zeros((3,2)) # $y=[\vec{r}_1,\vec{r}_2,\vec{r}_3]$, same for v 
    x = rtf.newton(quintic, dquintic, 1.,2.e-16)  # solve for $\lambda$
    a = (m2+m3-m1*(1+x+x)/((x*(1+x))**2))**(1./3.)
    
    r[1,0] = (m1/(x*x)-m3)/(a*a)                # non-zero x only
    r[0,0] = r[1,0]-x*a
    r[2,0] = -(m1*r[0,0] + m2*r[1,0])/m3        # CoM at 0
    v[0,1], v[1,1] = scale*r[0,0], scale*r[1,0] # non-zero Vy only
    v[2,1] = -(m1*v[0,1] + m2*v[1,1])/m3        # CoM at rest
    return r, v
    
def set_scene(R, r):        # create bodies, velocity arrows
    vp.display(title='Three-body motion', background=(1,1,1))
    body, vel = [], []      # bodies, vel arrows
    c = [(1,0,0), (0,1,0), (0,0,1), (0,0,0)]    # RGB colors
    for i in range(3):
        body.append(vp.sphere(pos=r[i],radius=R,color=c[i],make_trail=1))
        vel.append(vp.arrow(pos=body[i].pos,shaftwidth=R/2,color=c[i]))
    line, com = vp.curve(color=c[3]), vp.sphere(pos=(0,0), radius=R/4.)
    return body, vel, line
        
def run_3body(scale):
    t, h, ic, cycle, R = 0.0, 0.001, 0, 20, 0.1 # anim cycle, R=obj size
    r, v = init_cond(scale)
    body, vel, line = set_scene(R, r)     # create objects
    while True:
        vp.rate(1000)
        r, v = ode.leapfrog(threebody, r, v, t, h)
        ic = ic + 1
        if (ic % cycle == 0):       # animate once per 'cycle'
            for i in range(3):      # move bodies, draw vel, path, lines
                body[i].pos = r[i]  # bodies 
                vel[i].pos, vel[i].axis = body[i].pos, v[i]
                vel[i].length = R*(1+2*vp.mag(v[i]))    # scale vel vector
            line.pos = [body[i].pos for i in [0,1,2]]   # lines  
            
m1, m2, m3 = 1., 2., 3.             # masses, global
if (sys.version_info[0] < 3):
    run_3body(scale = input('enter scale, eg 0.7 :> '))
else:
    run_3body(scale = eval(input('enter scale, eg 0.7 :> ')))
