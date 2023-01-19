def coeficiente_binomial(m, p):
    c = [[0 for x in range(p + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(min(i, p) + 1):
            if j == 0 or j == i:
                c[i][j] = 1
            else:
                c[i][j] = c[i-1][j-1] + c[i-1][j]
    return c[m][p]


n = 5
k = 2
print("O valor do Coeficiente Binomial de [" + str(n) + "][" + str(k) + "] eh " + str(coeficiente_binomial(n, k)))
