#
# Program 3.8: Motion of a baseball (baseball.py)
# J Wang, Computational modeling and visualization with Python
#

import ode, visual as vp, numpy as np     # get ODE, VPython, numpy

def baseball(Y, t):                 # Y = [r, v] assumed
    v = Y[1]
    fm = alpha*vp.cross(omega, v)               # Magnus force
    a = (fm - b2*vp.mag(v)*v)/mass - [0,g,0]    # minus g-vec
    return np.array([v, a])                     # np array
    
def set_scene(R):        # draw scene, ball, trails, spin, info box
    scene = vp.display(background=(.2,.5,1), forward=(-1,-.1,-.1),
                       center=(.5*R,1,0), ambient=.4, fullscreen=1)
    floor = vp.box(pos=(R/2,0,0), length=1.1*R, height=.1, width=8, 
                   color=vp.color.orange, opacity=0.7)  # transparent 
    zone = vp.curve(pos=[(R,0,1),(R,1,1),(R,1,-1),(R,0,-1)], radius=.02)
    ball = vp.sphere(pos=(0,0,0), radius=.2, material=vp.materials.rough)
    trail = vp.curve(pos=(0,0,0), radius=0.04)
    ideal = vp.curve(pos=(0,0,0), radius=0.04, color=vp.color.green)
    spin = vp.arrow(axis=omega,pos=(0,0,0),length=1)   # omega dir
    info = vp.label(pos=(1.1*R,2,-2),text='Any key=repeat')
    return scene, ball, trail, ideal, spin
    
def go(x, y, vx, vy):       # motion with full drag and spin effects
    h, t, Y = 0.01, 0., np.array([[x,y,0.], [vx,vy,0.]])  # initialize
    while (Y[0,0]<R and Y[0,1]>0.2):    # before homeplate&above ground
        vp.rate(40)
        t, Y = t+h, ode.RK4(baseball, Y, t, h)  # integrate
        ball.pos, spin.pos = Y[0], Y[0]-offset # move ball, arrow 
        spin.rotate(angle=phi), ball.rotate(angle=phi,axis=omega)  #spin
        trail.append(pos=ball.pos)
        ideal.append(pos=(x+vx*t, y+vy*t-0.5*g*t*t, 0.))  # ideal case
    while (not scene.kb.keys):              # check for key press 
        vp.rate(40)
        spin.rotate(angle=phi), ball.rotate(angle=phi,axis=omega)
    scene.kb.getkey()                       # clear key 
    trail.append(pos=(0,0,0), retain=0)     # reset trails 
    ideal.append(pos=(0,0,0), retain=0)

g, b2, alpha, mass = 9.8, .0013, 5e-5, .15  # parameters    
R, omega = 18.4, 200.*np.array([0,1,1])     # range, angular velocity 
phi, offset = np.pi/16., 0.4*omega/vp.mag(omega)

scene, ball, trail, ideal, spin = set_scene(R)
while (1):
    go(x=0., y=2., vx=30., vy=0.)           # initially z=0, vz=0

