import numpy as np
import sys

def MIS(w):
    n = len(w)
    Soln = np.full(n, -1)
    sol = max(MISminus(w, n, Soln), MISplus(w, n, Soln))
    print(Soln)
    return sol

def MISplus(w, i, Soln):
    if (i == 0):
        return 0
    
    return w[i-1] + MISminus(w, i-1, Soln)

def MISminus(w, i, Soln):
    if (i <= 1):
        return 0
    if(Soln[i-1] == -1):
        Soln[i-1] = max(MISplus(w, i-1, Soln), MISminus(w, i-1, Soln))

    return Soln[i-1]

w = [2,7,6,3,6]
print(MIS(w))