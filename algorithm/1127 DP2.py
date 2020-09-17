def hamrun(num):
    n = num
    H = [[False]*(n+1) for i in range(n+1)]
    for j in range(1,n+1):
        for k in range(1,n//j+1):
            H[j][j*k] = not H[j-1][j*k]
    count = 0
    for l in range(n):
        if H[n+1][l+1]:
            count += 1
    return count

hamrun(17)
def hamrun(num):
    n = num
    H = [[False]*(n+1) for i in range(n+1)]
    for j in range(1,n+1):
        for k in range(n//j):
            H[j][j*(k+1)] = not H[j-1][j*(k+1)]
        for m in range(n):
            
    print(H)
    H[n][0] = 0
    for l in range(n):
        if H[n+1][l+1]:
            H[n][0] += 1
    return H[n][0]
hamrun(5)

