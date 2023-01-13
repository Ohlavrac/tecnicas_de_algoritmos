def par_proximo(pri, segun, alvo):
    if not len(pri) or not len(segun):
        return ()
    x = 0
    y = 0
    for index in range(len(pri)):
        for index2 in range(len(segun)):
            if abs(pri[index] + segun[index2] - alvo) < abs(pri[x] + segun[y] - alvo):
                x = index
                y = index2

    return pri[x], segun[y]


primeiro = [1, 4, 19, 45]
segundo = [2, 7, 10, 17]
alv = 14
par = par_proximo(pri=primeiro, segun=segundo, alvo=alv)
print(f'O par mais proximo é: {par}')