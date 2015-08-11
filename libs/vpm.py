# Common library file to be placed in the Python path (e.g., C:\Python27)
#
# Program 6.4 (DOC): VPM - VPython modules (vpm.py)
# J Wang, Computational modeling and visualization with Python
#

# Computational modeling, J Wang, UMass Dartmouth
# vpm - VPython modules:
# pause()/wait()
# line()
# bars()
# slinky()
# net()
# mesh()
#
import numpy as np, visual as vp

def pause(scene):       # pause until a key is pressed
    while (scene.kb.keys):      # clear key buffer first
        k =scene.kb.getkey()
    return scene.kb.getkey()

def wait(scene):        # wait for 2nd key after a key press
    if scene.kb.keys:
        return pause(scene)

class line:
    """ create a line by connecting points x[], y[], z[].
        optionally, specify line color and thickness """
    def __init__(self, x, y, z, linecolor=(1,1,1), thick = .05):
        self.line = vp.curve(color=linecolor, radius=thick)
        self.move(x, y, z)

    def move(self, x, y, z):        # update line
        self.line.pos = np.column_stack((x, y, z))

class bars:
    """ create a bar graph over points x[], y[], z[],
        with height h[] at each point (along y-axis).
        optionally, specify width, thckness, color, and axis """
    def __init__(self, x, y, z, h, width=0.05, thick = 0.05,
                 barcolor=(1,1,1), axis=(1,0,0)):
        self.bars=[vp.box(length=width, width=thick, color=barcolor,
                          axis=axis) for i in range(len(x))]
        self.move(x, y, z, h)

    def move(self, x, y, z, h):     # update bars
        for i in range(len(x)):
            self.bars[i].pos = (x[i], y[i]+h[i]/2, z[i])
            self.bars[i].height = abs(h[i])

class slinky:
    """ create a slinky by placing coils at points x[], y[], z[].
        other input: dir=axis of alinky, r=radius of coil,
                     thick=thinckness of wire """
    def __init__(self, x, y, z, dir=(0,-1,0), r=1, thick=.2):
        self.slinky, self.m, self.dir = [], len(x), dir
        for i in range(self.m):
            c = (0.9, 1 - 0.8*i/self.m, 0.1)        # RGB color mix
            self.slinky.append(vp.helix(radius=r, coils=1, color=c,
                                        thickness=thick))
        self.move(x, y, z)

    def move(self, x, y, z):        # update slinky
        d = (x[:-1]-x[1:])**2 + (y[:-1]-y[1:])**2 + (z[:-1]-z[1:])**2
        d = np.sqrt(np.append(d, d[-1]))
        for i in range(self.m):
            self.slinky[i].axis = self.dir
            self.slinky[i].pos = (x[i],y[i],z[i])
            self.slinky[i].length = d[i]    # set length last

# build a net of quadrilaterals, 4-sided polygons
class net:
    """ create a fishnet, grid points are given by x[,],y[,],z[,]
        other input: netcolor and thread thickness """
    #    j
    #    ^ n * * * ... *
    #    | : * * * ... *
    #    | 2 * * * ... *
    #    | 1 * * * ... *
    #    | 0 * * * ... *
    #    | o 0 1 2 ... m ---> i
    def __init__(self, x, y, z, netcolor=(1,1,1), thick=.05):
        self.m, self.n = len(x[:,0]), len(y[0,:])   # nx, ny points
        self.net=[vp.curve(color=netcolor, radius=thick)
                  for i in range(self.m + self.n)]
        self.move(x, y, z)

    def move(self, x, y, z):        # update net
        for i in range(self.m):             # vertical lines
            self.net[i].pos = np.column_stack((x[i,:],y[i,:],z[i,:]))
        for j in range(self.n):             # horizontal lines
            self.net[self.m+j].pos=np.column_stack((x[:,j],y[:,j],z[:,j]))

# build a mesh of triangles from quadrilaterals
class mesh:
    """ create a mesh surface, grid points are given by x[,],y[,],z[,]
        other input: top and bottom surface colors """
    def __init__(self, x, y, z, topcolor=(1,0,0), botcolor=(0,1,1)):
        self.t = vp.faces(color=topcolor)         # top, bot faces
        self.b = vp.faces(color=botcolor)
        self.move(x, y, z)          # set initial position

    def corners(self, x, y, z):     # cut rectangles diagonally
        p = np.dstack((x, y, z))                # grid points
        cs = np.column_stack                            # triangle
        s = lambda u:  np.reshape(u, (-1,3))            #       b___c
        a, c = s(p[:-1,:-1]), s(p[1:,1:])               #       | 1/|
        t1 = cs((a, s(p[:-1,1:]), c))                   # abc   | /2|
        t2 = cs((a, c, s(p[1:,:-1])))                   # acd   |/__|
        q = np.concatenate((t1,t2)).reshape(-1,3)       #       a   d
        r = np.reshape(q, (len(q)//3,3,3))      # bottom, ccw winding
        r = np.reshape(r[:,[0,2,1],:], (-1,3))  # back to Nx3
        return q, r

    def move(self, x, y, z):        # update mesh
        self.t.pos, self.b.pos = self.corners(x, y, z)  # get corners
        self.t.make_normals(), self.b.make_normals()    # actual normals
