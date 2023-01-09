def parProximo(first, second, targe):
    if not len(first) or not len(second):
        return ()
    
    x = 0
    y = 0

    for index in range(len(first)):
        for index2 in range(len(second)):
            if abs(first[index] + second[index2] - targe) < abs(first[x] + second[y] - targe):
                x = index
                y = index2

    return first[x], second[y]

first = [1, 4, 19, 45]
second = [2, 7, 10, 17]
targe = 14
par = parProximo(first=first, second=second, targe=targe)
print(f'O par mais proximo é: {par}')