#problema da soma de subconjuntos
def is_sub_set_sum(conj, num, soma):
    subset = ([[False for i in range(soma + 1)] for i in range(num + 1)])
    print(subset[0])

    for i in range(num + 1):
        subset[i][0] = True

    for i in range(1, soma + 1):
        subset[0][i] = False

    for i in range(1, num + 1):
        for i2 in range(1, soma + 1):
            if i2 < conj[i - 1]:
                subset[i][i2] = subset[i - 1][i2]
            if i2 >= conj[i - 1]:
                subset[i][i2] = (subset[i - 1][i2] or subset[i - 1][i2 - conj[i - 1]])

    print(f'>>>> {subset}')
    return subset[num][soma]


conjunto = [3, 34, 4, 12, 5, 2]
som = 9
numero = len(conjunto)
if is_sub_set_sum(conjunto, numero, som):
    print("Encontrado o subset com a determinada soma")
else:
    print("Subset não encontrado")
