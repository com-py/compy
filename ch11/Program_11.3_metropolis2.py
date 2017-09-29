#
# Program 11.3: Ising model in 2D (metropolis2.py)
# J Wang, Computational modeling and visualization with Python
#

def update2d(N, spin, kT, E, M):    # 2D Ising model, N x N lattice
    i, j, flip = rnd.randint(0, N-1), rnd.randint(0, N-1), 0
    dE = 2*spin[i][j]*( spin[i-1][j] + spin[(i+1)%N][j]
                      + spin[i][j-1] + spin[i][(j+1)%N] )
    if (dE < 0.0): flip=1           # flip if dE<0, else flip 
    else:                           # according to exp(-dE/kT)
        p = np.exp(-dE/kT)
        if (rnd.random() < p): flip=1
    if (flip == 1):
        E = E + dE
        M = M - 2*spin[i][j]
        spin[i][j] = -spin[i][j]
    return E, M
