def SSmn(S):
    n = len(S)
    Soln = []
    for i in range(n+1):
        Soln.append([])
    
    for i in range(1,n+1):
        x_mod = S[i-1] % n
        Soln[i].append(x_mod)
        for j in range(len(Soln[i-1])):
            v = Soln[i-1][j]
            Soln[i].append(v)
            Soln[i].append((v+S[i-1]) % n)
        Soln[i] = list(dict.fromkeys(Soln[i]))
        print(Soln[i])
    
    for i in range(len(Soln[n])):
        if(Soln[n][i] == 0):
            return True
    return False


print(SSmn([3,4,6,12,5]))