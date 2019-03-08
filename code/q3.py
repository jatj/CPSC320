import numpy as np
import sys

def M(n, Soln):
    if n <= 1:
        return 1
    if Soln[n-1] != 1:
        return Soln[n-1]
    Min = sys.maxsize
    for i in range(1,n):
        Min = min(Min, M(n-i, Soln) + M(i,Soln))
        if (i+1 < n/2 and n%(i+1) == 0):
            Min = min(Min, M(int(n/(i+1)), Soln) + M(i+1,Soln))
    Soln[n-1] = Min
    print(Soln)
    return Min

n = 14
Soln = np.full(n,1)
print(M(n,Soln))