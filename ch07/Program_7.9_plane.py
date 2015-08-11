#
# Program 7.9: Plane electromagnetic waves (plane.py)
# J Wang, Computational modeling and visualization with Python
#

import visual as vp, numpy as np, vpm

t, dt, v, L = 0.0, 0.01, 0.2, 1.0       # time, speed, wavelength
n, scale, E, B = 61, 0.2, [], []        # grid, scale

scene=vp.display(title='Electromagnetic waves', background=(.2,.5,1),
                   center=(0,0,L), forward=(-.4,-.3,-1))
ax, ay, az = (1,0,0), (0,1,0), (0,0,1)          # axes and labels
vp.arrow(pos=(.2, -.2, L), axis=ax, length=0.2, color=(1,1,0))
vp.arrow(pos=(.2, -.2, L), axis=ay, length=0.2, color=(0,1,1))
vp.arrow(pos=(.2, -.2, L), axis=az, length=0.2, color=(1,1,1))
vp.label(pos=(.45, -.2, L), text='E', box=False, height=30)
vp.label(pos=(.25, -.0, L), text='B', box=False, height=30)
vp.label(pos=(.2, -.15, L+.3), text='v', box=False, height=30)

idx, z = np.arange(n), np.linspace(-L, 2*L, n)  # order of vectors
mag = scale*np.sin(2*np.pi*z/L)                 # sine envelope
ewave = vp.curve(color=(1,1,0), pos=np.column_stack((mag,0*z,z)))
bwave = vp.curve(color=(0,1,1), pos=np.column_stack((0*z,mag,z)))
for i in idx:
    E.append( vp.arrow(pos=(0, 0, z[i]), axis=ax, length=mag[i],
                       color=(1,1,0)) )
    B.append( vp.arrow(pos=(0, 0, z[i]), axis=ay, length=mag[i], 
                       color=(0,1,1)) )
while True:
    vp.rate(100), vpm.wait(scene)               # hit a key to pause
    t, mg = t + dt, mag*np.cos(t)               # sinusoidal wave
    for i in range(n):                          
        E[i].pos.z += v*dt                      # traveling wave
        B[i].pos.z += v*dt
        if (E[i].pos.z > 2*L):                  # wrap around
            E[i].pos.z, B[i].pos.z = -L, -L 
            idx = np.insert(idx, 0, i)[:-1]     # move to end 
            
        E[i].axis, B[i].axis = ax, ay           # reset axis to 
        E[i].length, B[i].length = mg[i], mg[i] #   draw correctly
        id = idx[i]
        ewave.pos[i] = (mg[id], 0, E[id].pos.z) # envelope curves
        bwave.pos[i] = (0, mg[id], B[id].pos.z)
