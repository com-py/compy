# Common library file to be placed in the Python path (e.g., C:\Python27)
#
# Program 9.6: FEM library (fem.py)
# J Wang, Computational modeling and visualization with Python
#

import numpy as np

def abg(p1, p2, p3):        # return alpha, beta, gamma, area of element
    [x1,y1], [x2,y2], [x3,y3] = p1, p2, p3
    alfa = [x2*y3 - x3*y2, x3*y1 - x1*y3, x1*y2 - x2*y1]
    beta, gama = [y2-y3, y3-y1, y1-y2], [x3-x2, x1-x3, x2-x1]
    area = 0.5*(alfa[0] + alfa[1] + alfa[2])       # area of triangle
    return alfa, beta, gama, area
    
def overlap(i, j, p1, p2, p3):          # return $\int \varphi_i \varphi_j dx dy$, 
    a, b, c, area = abg(p1, p2, p3)     # over eltriangle and pts p1-p3
    X, Y, XY, X2, Y2 = 0., 0., 0., 0., 0.
    for [x, y] in [p1, p2, p3]:
        X, Y, XY, X2, Y2 = X+x, Y+y, XY+x*y, X2+x*x, Y2+y*y 
    return ((a[i]*b[j]+b[i]*a[j])*X + (a[i]*c[j]+c[i]*a[j])*Y +
            (b[i]*b[j]*(X2+X*X) +(b[i]*c[j]+c[i]*b[j])*(XY+X*Y) +
             c[i]*c[j]*(Y2+Y*Y))/4 + 3*a[i]*a[j])/(12*area)
    
def A_mat(node, elm):      # fills matrix $\int \nabla \phi_i \cdot \nabla \phi_j dx dy$, 
    A = np.zeros((len(node),len(node)))
    for e in elm:
        [x1,y1], [x2,y2], [x3,y3] = node[e[0]], node[e[1]], node[e[2]]
        a = 2*(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))        # $4 A_e$
        if (a<=0.0): print ('Warning: zero or negative elm area')
        beta, gama = [y2-y3, y3-y1, y1-y2], [x3-x2, x1-x3, x2-x1]
        for i in range(3):                              
            for j in range(i,3):                            # 
                A[e[i],e[j]] += (beta[i]*beta[j] + gama[i]*gama[j])/a     
                if (i != j): A[e[j],e[i]] = A[e[i],e[j]]
    return A                # A=twice KE, $- \frac12 < \nabla^2 >$

def B_mat(node, elm):       # overlap matrix,  $\int \phi_i \phi_j dx dy$, 
    B = np.zeros((len(node),len(node)))
    for e in elm:
        p1, p2, p3 = node[e[0]], node[e[1]], node[e[2]]
        for i in range(3):
            for j in range(i,3):
                B[e[i],e[j]] += overlap(i, j, p1, p2, p3)
                if (i != j): B[e[j],e[i]] = B[e[i],e[j]]
    return B   
    
   
