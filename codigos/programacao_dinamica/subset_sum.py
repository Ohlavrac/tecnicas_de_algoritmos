#problema da soma de subconjuntos
def is_sub_set_sum(conj, num, soma):
    subset = ([[False for i in range(soma + 1)] for i in range(num + 1)])
    print(subset[0])

    for index in range(num + 1):
        subset[index][0] = True

    for index in range(1, soma + 1):
        subset[0][index] = False

    for index in range(1, num + 1):
        for index2 in range(1, soma + 1):
            if index2 < conj[index - 1]:
                subset[index][index2] = subset[index - 1][index2]
            if index2 >= conj[index - 1]:
                subset[index][index2] = (subset[index - 1][index2] or subset[index - 1][index2 - conj[index - 1]])

    print(f'>>>> {subset}')
    return subset[num][soma]


conjunto = [3, 34, 4, 12, 5, 2]
som = 9
numero = len(conjunto)
if is_sub_set_sum(conjunto, numero, som):
    print("Encontrado o subset com a determinada soma")
else:
    print("Subset não encontrado")
