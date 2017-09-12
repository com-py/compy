#
# Program 4.3: Precession of Mercury (mercury.py)
# J Wang, Computational modeling and visualization with Python
#

import ode, numpy as np         # get ODE solvers, numpy
import visual as vp             # get VPython modules for animation
import matplotlib.pyplot as plt # get matplotlib plot functions
import sys

def mercury(id, r, v, t):       # eqns of motion for mercury
    if (id == 0): return v      # velocity, dr/dt
    s = vp.mag(r)               
    return -GM*r*(1.0 + lamb/(s*s))/(s*s*s)     # acceleration, dv/dt

def set_scene(r):     # r = init position of planet
    # draw scene, mercury, sun, info box, Runge-Lenz vector
    scene = vp.display(title='Precession of Mercury', 
                       center=(.1*0,0), background=(.2,.5,1))
    planet= vp.sphere(pos=r, color=(.9,.6,.4), make_trail=True,
                      radius=0.05, material=vp.materials.diffuse)
    sun   = vp.sphere(pos=(0,0), color=vp.color.yellow,
                      radius=0.02, material=vp.materials.emissive)
    sunlight = vp.local_light(pos=(0,0), color=vp.color.yellow)
    info = vp.label(pos=(.3,-.4), text='Angle') # angle info
    RLvec = vp.arrow(pos=(0,0), axis=(-1,0,0), length = 0.25)
    return planet, info, RLvec
    
def go(animate = True):                     # default: True
    r, v = np.array([0.4667, 0.0]), np.array([0.0, 8.198]) # init r, v
    t, h, ta, angle = 0.0, 0.002, [], []
    w = 1.0/vp.mag(r)                       # $W_0=\Omega(r)$
    
    if (animate): planet, info, RLvec = set_scene(r)
    while t<100:                            # run for 100 years
        L = vp.cross(r, v)                  # $\vec{L}/m=\vec{r}\times \vec{v}$
        A = vp.cross(v, L) - GM*r/vp.mag(r) # scaled RL vec, 
        ta.append(t)
        angle.append(np.arctan(A.y/A.x)*180*3600/np.pi) # arcseconds
        if (animate):    
            vp.rate(100)   
            planet.pos = r                              # move planet
            RLvec.axis, RLvec.length = A, .25           # update RL vec
            info.text='Angle": %8.2f' %(angle[-1])      # angle info 
        r, v, t, w = ode.leapfrog_tt(mercury, r, v, t, w, h)
        
    plt.figure()        # make plot
    plt.plot(ta, angle)
    plt.xlabel('Time (year)'), plt.ylabel('Precession (arcsec)')
    plt.show()

GM = 4*np.pi*np.pi      # G*Msun
# lamb=relativistic correction, global, used in 'mercury()'
if (sys.version_info[0] < 3):
    lamb = input('Please enter lambda, eg: 0.01, or 1.1E-8 :> ')
else:
    lamb = eval(input('Please enter lambda, eg: 0.01, or 1.1E-8 :> '))
go(animate = True)      # set to False to speed up calc. for plots
        
