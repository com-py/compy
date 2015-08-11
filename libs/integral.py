# Common library file to be placed in the Python path (e.g., C:\Python27)
#
# Program 8.5: Numerical integration (integral.py)
# J Wang, Computational modeling and visualization with Python
#

def simpson(f, h):         # Simpson's rule over discrete points
    n, extra = len(f), 0.0    
    if (n-1)%2 != 0:                # numbers of bins not even
        n = n - 1
        extra = f[-2]+f[-1]         # trapzoid for last bin
      
    sum, w = f[0]+f[n-1], 4
    for i in range(1, n-1):
        sum = sum + w*f[i]
        w = 6 - w                   # alternate between 4, 2
    return h*(sum/3. + extra/2.)
    
def gauss(f, a, b):        # Order 36: abscissas and weights
    x=[0.9978304624840857, 0.9885864789022123, 0.9720276910496981,
       0.9482729843995075, 0.9174977745156592, 0.8799298008903973,
       0.8358471669924752, 0.7855762301322065, 0.7294891715935568,
       0.6680012365855210, 0.6015676581359806, 0.5306802859262452,
       0.4558639444334203, 0.3776725471196892, 0.2966849953440283,
       0.2135008923168655, 0.1287361038093848, 0.04301819847370858]
       
    w=[.005565719664245068, 0.01291594728406522, 0.02018151529773513,
       0.02729862149856854, 0.03421381077030707, 0.04087575092364476,
       0.04723508349026585, 0.05324471397775972, 0.05886014424532480,
       0.06403979735501547, 0.06874532383573639, 0.07294188500565307,
       0.07659841064587077, 0.07968782891207167, 0.08218726670433972,
       0.08407821897966186, 0.08534668573933869, 0.08598327567039468]
       
    p = 0.5*(b+a)       # map from [a,b] to [-1,1]
    q = 0.5*(b-a)
    n = len(x)   
    sum = 0.0
    for i in range(n):
        sum += w[i]*(f(p + q*x[i]) + f(p - q*x[i]))
    return q*sum   
