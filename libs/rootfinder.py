# Common library file to be placed in the Python path (e.g., C:\Python27)
#
# Programs 3.6, 3.7: Root finders library (rootfinder.py, Ch. 3, Sec. 3.A)
# J Wang, Computational modeling and visualization with Python
#

def bisect(f, a, b, eps=1.e-6):  # user-defined f(x) and bracket [a,b]
    fa, fb, gap = f(a), f(b), abs(b-a)  # end points and initial gap
    if (fa*fb > 0.0):                   # no root in bracket
        print('Bisection error: no root bracketed')
        return None       
    elif fa == 0.0:   return a
    elif fb == 0.0:   return b
    
    while (True):
        xmid = 0.5*(a+b)
        fmid = f(xmid)
        if (fa*fmid > 0.0):         # root in [xmid, b]
            a, fa = xmid, fmid      # set a=xmid and save a function call
        else: b=xmid                # root in [a, xmid]
        if (fmid == 0.0 or abs(b-a) < eps*gap): break   # root found @ \label{line:biseceps} @

    return xmid
    
def newton(f, df, x, eps=1.e-6):  # user-defined f(x),df/dx, init root
    nmax, fx = 20, f(x)           # max number of iterations
    if (fx == 0.0): return x
    
    for i in range(nmax):
        delta = fx/df(x)
        if (i == 0): gap = abs(delta)   # save initial gap
        x = x - delta                   # 'improved' root
        fx = f(x)                       # prep for next round
        if (fx == 0.0 or abs(delta) < eps*gap): break     # root found @ \label{line:newtoneps} @

    return x
    