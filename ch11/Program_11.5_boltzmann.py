#
# Program 11.5: Boltzmann distribution (boltzmann.py)
# J Wang, Computational modeling and visualization with Python
#

from einsteinsolid import EinsteinSolid
import matplotlib.pyplot as plt, numpy as np

solid = EinsteinSolid(N=1024, q=1)      # initialize solid
L, M, kT = 100, 6, 1./np.log(2.)        # L = base iteration num.
E, bin = np.linspace(0., M, 100), np.zeros(M+1)
fig = plt.figure()
for i in range(9):                      # 3x3 subplots
    ax = fig.add_subplot(3, 3, i+1)
    for n in range(M+1):
        bin[n] = solid.cell.count(n)    # count n   @\lbl{line:count}@
    plt.step(range(len(bin)), bin/max(bin), where='mid')
    plt.plot(E, np.exp(-E/kT))
    if (i == 3): plt.ylabel('$P(n)$', fontsize=14)
    if (i == 7): plt.xlabel('$n$', fontsize=14)
    if (i <= 5):
        plt.xticks(range(M+1), ['' for j in range(M+1)])
    if (i > 0): plt.text(M-2, 0.8, repr(L*2**(i-1)))
    solid.exchange(L*2**i)              # double L each time
plt.show()
