

def ChooseDinnerDates(P,k):
    n = len(P)
    if(n == 0):
        return [];

    dmin = min(P, key=lambda tup: tup[1])[1]
    i = 0

    while(i < k):
        if(len(P) == 0):
            break
        pair = min(P, key=lambda tup: tup[0])
        if(pair[0] <= dmin):
            P.remove(pair)
            i += 1
        else:
            break
    return [dmin] + ChooseDinnerDates(P,k)

def ChooseDinnerDates2(P,k):
    n = len(P)
    if(n == 0):
        return [];

    smax = max(P, key=lambda tup: tup[0])[0]
    i = 0

    while(i < k):
        if(len(P) == 0):
            break
        pair = max(P, key=lambda tup: tup[1])
        if(pair[1] >= smax):
            P.remove(pair)
            i += 1
        else:
            break
    return [smax] + ChooseDinnerDates2(P,k)

def PrintSchedule(P):
    res = ""
    for i in range(len(P)):
        s = P[i][0]
        d = P[i][1]
        h = s + (d - s)/2
        off = 0.2
        res += f"\n\draw [|-|,thick] ({s},{-i}) -- ({d},{-i});\n\\node[align=center, above] at ({h},{-i}){ {i+1} };\n\\node[align=center, below] at ({s},{-i-off}){ {s} };\n\\node[align=center, below] at ({d},{-i-off}){ {d} };"
    return res

P = [
    (5,8),
    (4,10),
    (7,7),
    (3,8),
    (6,7),
    (9,10),
    (11,12),
    (15,20),
]
k = 3

res = ChooseDinnerDates2(P,k)
# res = PrintSchedule(P)
print(res)