#
# Program 8.6: Gauss abscissa and weight (gaussxw.py)
# J Wang, Computational modeling and visualization with Python
#

from scipy.special import legendre

n = 36                  # order
p = legendre(n)
x = p.weights[:,0]      # abscissa
w = p.weights[:,1]      # weight

for i in range(n):
    print ('%20.16f %20.16f' %(x[i], w[i]))
   
