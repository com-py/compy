#
# Program 11.1: Einstein solid class (einsteinsolid.py)
# J Wang, Computational modeling and visualization with Python
#

import random as rnd

class EinsteinSolid:                        # Einstein solid object
    def __init__(self, N=400, q=10):
        self.N = N
        self.cell = [q]*N                   # q units energy per cell
        
    def __add__(self, other):               # combine two solids
        self.N += other.N
        self.cell += other.cell
        return self
        
    def exchange(self, L=20):               # iterate L times
        for i in range(L):
            take = rnd.randint(0, self.N-1) # random pair
            give = rnd.randint(0, self.N-1) 
            while self.cell[take] == 0:     # find a nonzero-energy cell
                take = rnd.randint(0, self.N-1)
            self.cell[take] -= 1            # exchange energy
            self.cell[give] += 1