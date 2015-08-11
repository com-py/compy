#
# Program 11.2: Entropy of an Einstein solid (entropy.py)
# J Wang, Computational modeling and visualization with Python
#

def entropy(cell):                      # entropy of Einstein solid
    N, n, nt, s = len(cell), 0, 0, 0.
    while nt < N:                       # until all cells are counted
        cn  = cell.count(n)             # num. of cells with En 
        n, nt = n + 1, nt + cn          # increase energy, cumul. cells
        p = cn/float(N)                 # probability
        if (cn != 0): s -= p*np.log(p)  # entropy/k, 
    return s
