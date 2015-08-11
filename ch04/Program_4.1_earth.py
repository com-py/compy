#
# Program 4.1: Planetary motion (earth.py)
# J Wang, Computational modeling and visualization with Python
#

import ode, numpy as np     # get ODE solvers, numpy
import visual as vp         # get VPython modules for animation

def earth(id, r, v, t):            # return the eqns of motion
    if (id == 0): return v         # velocity, dr/dt
    s = vp.mag(r)                  # $s=|\vec{r}|$
    return -GM*r/(s*s*s)           # accel dv/dt, faster than s**3  
        
def go():
    r = np.array([1.017, 0.0])     # initial x,y position for earth   
    v = np.array([0.0, 6.179])     # initial vx, vy                   
    
    # draw the scene, planet earth/path, sun/sunlight               
    scene = vp.display(title='Planetary motion',          # scene start 
                       background=(.2,.5,1), forward=(0,2,-1))
    planet= vp.sphere(pos=r, radius=0.1, make_trail=True,
                      material=vp.materials.earth, up=(0,0,1))
    sun   = vp.sphere(pos=(0,0), radius=0.2, color=vp.color.yellow,
                      material=vp.materials.emissive)
    sunlight = vp.local_light(pos=(0,0), color=vp.color.yellow) #scn end 
    
    t, h = 0.0, 0.001
    while True:
        vp.rate(200)   # limit animation speed
        r, v = ode.leapfrog(earth, r, v, t, h)  # integrate 
        planet.pos = r                          # move planet    
        if (scene.kb.keys): scene.kb.getkey(), scene.kb.getkey() #pause 

GM = 4*np.pi*np.pi          # G*Msun
go()
       
