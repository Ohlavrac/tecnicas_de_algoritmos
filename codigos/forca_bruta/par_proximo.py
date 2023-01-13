def par_proximo(pri, segun, alvo):
    if not len(pri) or not len(segun):
        return ()
    x = 0
    y = 0
    for i in range(len(pri)):
        for j in range(len(segun)):
            if abs(pri[i] + segun[j] - alvo) < abs(pri[x] + segun[y] - alvo):
                x = i
                y = j

    return pri[x], segun[y]


primeiro = [1, 4, 19, 45]
segundo = [2, 7, 10, 17]
alv = 14
par = par_proximo(pri=primeiro, segun=segundo, alvo=alv)
print(f'O par mais proximo é: {par}')
