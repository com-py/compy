#
# Program 6.8: A falling tablecloth (tablecloth.py)
# J Wang, Computational modeling and visualization with Python
#

import ode, vpm, numpy as np, visual as vp

def force(r):       # force of particle pair, with relative pos r
    s = np.sqrt(np.sum(r*r, axis=-1))           # distance 
    s3 = np.dstack((s, s, s))                   # make (m,n,3) array 
    return -spring_k*(1.0 - spring_l/s3)*r      # Hooke's law 
    
def cloth(Y, t):    # tablecloth
    r, v, f = Y[0], Y[1], np.zeros((N,M,3))
    
    rtop = r[0:-1, :] - r[1:, :]                # rel pos to top neighbor 
    rright = r[:, 0:-1] - r[:, 1:]              # rel pos to right neighbor
    ftop, fright = force(rtop), force(rright)   # forces from top, right
    f[0:-1, :] = ftop                   # force from top 
    f[:, 0:-1] += fright                # force from right 
    f[1:, :] -= ftop                    # below, left: use 3rd law 
    f[:, 1:] -= fright
    a = (f - damp*v)/mass + gvec
    v[0,0], v[0,-1], v[-1,0], v[-1,-1]=0, 0, 0, 0   # fixed coners 
    return np.array([v,a])
    
L, M, N = 2.0, 15, 15                   # size, (M,N) particle array
h, mass, damp = 0.01, 0.004, 0.01       # keep damp between [.01,.1]
x, y = np.linspace(0,L,M), np.linspace(0,L,N)       # particle grid
r, v = np.zeros((N,M,3)), np.zeros((N,M,3))
spring_k, spring_l = 50.0, x[1]-x[0]    # spring const., relaxed length
r[:,:, 0], r[:,:, 1] = np.meshgrid(x,y)             # initialize pos
Y, gvec = np.array([r, v]), np.array([0,0,-9.8])    # [v,a], g vector

scene = vp.display(title='Tablecloth', background=(.2,.5,1), 
                   up=(0,0,1), center=(L/2,L/2,-L/4), forward=(1,2,-1))
vp.points(pos=[(0,0,0),(0,L,0),(L,L,0),(L,0,0)], size=50)   # corners
x, y, z = r[:,:,0], r[:,:,1], r[:,:,2]                      # mesh points
net = vpm.net(x, y, z, vp.color.yellow, 0.005)              # mesh net
mesh = vpm.mesh(x, y, z, vp.color.red, vp.color.yellow)

while (1):
    vp.rate(100), vpm.wait(scene)       # pause if key pressed
    Y = ode.RK4(cloth, Y, 0, h)
    x, y, z = Y[0,:,:,0], Y[0,:,:,1], Y[0,:,:,2]
    net.move(x, y, z), mesh.move(x, y, z)
