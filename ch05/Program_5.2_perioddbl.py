#
# Program 5.2: Period doubling (perioddbl.py)
# J Wang, Computational modeling and visualization with Python
#

import matplotlib.pyplot as plt     # get matplotlib plot functions
ntrans, nsteps = 1000, 200          # num. of transients and to keep
r, rend, dr, x, xa = 0.7, 1.0, 0.001, 0.5, [0.0]*nsteps
plt.figure()
while r <= rend:
    for i in range(ntrans): x = 4*r*x*(1-x)     # discard transients
    for i in range(nsteps): xa[i], x = x, 4*r*x*(1-x)  # keep rest
    plt.plot([r]*nsteps, xa, 'b,')              # blue pixel markers
    r = r + dr
plt.xlabel('r'),  plt.ylabel('x'), plt.show()
