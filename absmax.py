def Absmax(a, n, m):
    y = 0
    i = k = 1
    for p in range(1, n+1):
        for q in range(1, m+1):
            if abs(a[p-1][q-1]) > y:
                y = abs(a[p-1][q-1])
                i = p
                k = q
    return y, i, k

print(Absmax([(2,5,3,8,5),(2,5,3,8,5),(2,5,3,8,5),(2,5,9,8,-52)],4,4))