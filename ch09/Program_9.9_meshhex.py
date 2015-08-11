#
# Program 9.9: Hexagon mesh generator (meshhex.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np, fileio

def mesh(a, N):                 # generate Hexagon mesh 
    node, elm = [], []          # nodes, elements
    bp, ip, h = [], [], a/N     # boundary and internal nodes, size
    M = (N*(3*N+1))//2          # last node before y=0 (center row)
    K = M + 2*N +1              # last node at end of center row
    ndn = lambda i, j: j*N + (j*(j+1))//2 + i    # node number at i,j
    
    for j in range(N+1):        # go up till y=0
        x, y = - 0.5*(a + j*h), (j*h - a)*np.sqrt(3.0)/2.0
        for i in range(N+1+j):
            node.append([x + i*h, y])
            if (j != N):
                elm.append([ndn(i,j), ndn(i+1,j+1),ndn(i,j+1)])
                if (i != N+j):
                    elm.append([ndn(i,j), ndn(i+1,j),ndn(i+1,j+1)])
            if (j == 0 or i == 0 or i == N+j): bp.append(ndn(i,j))
            else: ip.append(ndn(i,j))
    
    node, elm = np.array(node), np.array(elm)   # get y>0 by reflection
    flip = np.column_stack((node[:M][:,0], -node[:M][:,1])) # c-stack 
    node = np.concatenate((node, flip))         
    
    flip = elm[:,[1, 0, 2]]         # swap nodes so they are ccw 
    flip[flip<M] += K               # add offset, excluding center row 
    elm = np.concatenate((elm, flip))
    
    bp = np.concatenate((bp, K + np.array(bp[:-2])))
    ip = np.concatenate((ip, K + np.array(ip[:-(N+N-1)])))
    fileio.writemesh('meshHexagon.txt', node, elm.tolist(), bp, ip)
    print ('Hex mesh: %d nodes (%d/%d bndry/intrnl), %d elements'
            %(len(node), len(bp), len(ip), len(elm)))

a, N = 1.0, 10      # side length, num intervals
mesh(a, N)




