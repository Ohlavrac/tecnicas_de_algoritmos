#problema da soma de subconjuntos
def is_sub_set_sum(conj, numb, suma):
    subset = ([[False for i in range(suma + 1)] for i in range(numb + 1)])
    print(subset[0])

    for index in range(numb + 1):
        subset[index][0] = True

    for index in range(1, suma + 1):
        subset[0][index] = False

    for index in range(1, numb + 1):
        for index2 in range(1, suma + 1):
            if index2 < conj[index - 1]:
                subset[index][index2] = subset[index - 1][index2]
            if index2 >= conj[index - 1]:
                subset[index][index2] = (subset[index - 1][index2] or subset[index - 1][index2 - conj[index - 1]])

    print(f'>>>> {subset}')
    return subset[numb][suma]


conjunto = [3, 34, 4, 12, 5, 2]
som = 9
number = len(conjunto)
if is_sub_set_sum(conjunto, number, som):
    print("Encontrado o subset com a determinada soma")
else:
    print("Subset não encontrado")
