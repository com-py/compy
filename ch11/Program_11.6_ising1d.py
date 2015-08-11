#
# Program 11.6: Ising model in 1D (ising1d.py)
# J Wang, Computational modeling and visualization with Python
#

import random as rnd, numpy as np
import matplotlib.pyplot as plt

def initialize(N):  # set initial spins
    p, spin, E, M = 0.5, [1]*N, 0., 0.      # p = order para.
    for i in range(1, N):
         if (rnd.random() < p): spin[i]=-1
         E = E - spin[i-1]*spin[i]
         M = M + spin[i]
    return spin, E - spin[N-1]*spin[0], M+spin[0]

def update(N, spin, kT, E, M):      # Metropolis sampling
    i, flip = rnd.randint(0, N-1), 0
    dE = 2*spin[i]*(spin[i-1] + spin[(i+1)%N])  # periodic bc
    if (dE < 0.0): flip=1           # flip if dE<0, else flip 
    else:                           # according to exp(-dE/kT)
        p = np.exp(-dE/kT)
        if (rnd.random() < p): flip=1
    if (flip == 1):                 # accept
        E = E + dE
        M = M - 2*spin[i]
        spin[i] = -spin[i]
    return E, M

N, passes = 1000, 10
iter, Nmc = passes*N, passes*N
T, Eavg, Mavg = [], [], []
for i in range(1,41):               # temperature loop
    kT = 0.1*i                      # kT = reservoir temperature
    spin, E, M  = initialize(N)
    for k in range(iter):           # let it equilibrate
        E, M = update(N, spin, kT, E, M)
        
    E1, M1 = 0., 0.
    for k in range(Nmc):            # take averages
        E, M = update(N, spin, kT, E, M)
        E1, M1 = E1 + E, M1 + M
    E1, M1 = E1/Nmc, M1/Nmc
    T.append(kT), Eavg.append(E1/N), Mavg.append(M1/N)
    
plt.figure()
plt.plot(T, Eavg, 'o', T, -np.tanh(1./np.array(T)))
plt.xlabel('$kT/\epsilon$'), plt.ylabel(r'$\langle E \rangle/N\epsilon$')
plt.figure()
plt.plot(T, Mavg,'o')
plt.xlabel('$kT/\epsilon$'), plt.ylabel(r'$\langle M \rangle/N$')
plt.show()


