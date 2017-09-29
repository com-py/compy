#
# Program 3.7: Newton's method (newton.py)
# J Wang, Computational modeling and visualization with Python
#

def newton(f, df, x, eps=1.e-6):  # user-defined f(x),df/dx, init root
    nmax, fx = 20, f(x)           # max number of iterations
    if (fx == 0.0): return x
    
    for i in range(nmax):
        delta = fx/df(x)
        if (i == 0): gap = abs(delta)   # save initial gap
        x = x - delta                   # 'improved' root
        fx = f(x)                       # prep for next round
        if (fx == 0.0 or abs(delta) < eps*gap): break     # root found 

    return x
