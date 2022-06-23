#
# Program 11.2: Entropy of an Einstein solid (entropy.py)
# J Wang, Computational modeling and visualization with Python
#

def entropy(cell):                      # entropy of Einstein solid
    Et, E, N, n, s = sum(cell), 0, len(cell), 0, 0.
    while E < Et:                       # until all cells are counted
        cn  = cell.count(n)             # num. of cells with En 
        n, E = n + 1, E + cn*n          # increase energy, cumul. energy
        p = cn/float(N)                 # probability
        if (cn != 0): s -= p*np.log(p)  # entropy/k, 
    return s
