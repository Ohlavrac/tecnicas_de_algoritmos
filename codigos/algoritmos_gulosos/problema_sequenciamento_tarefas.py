def sequenciamento_tarefas(array, t):
    tamanho = len(array)

    print(f'Array na ordem original: {array}')

    for i in range(tamanho):
        for j in range(tamanho - 1 - i):
            if array[j][2] < array[j + 1][2]:
                array[j], array[j + 1] = array[j + 1], array[j]

    print(f'Array organizado em ordem crescente com base no lucro: {array}')

    resultado = [False] * t

    trabalho = ['-1'] * t

    print(trabalho)
    print(resultado)

    for i in range(len(array)):
        print('>>>>', min(t - 1, array[i][1] - 1))
        for j in range(min(t - 1, array[i][1] - 1), -1, -1):
            if resultado[j] is False:
                resultado[j] = True
                trabalho[j] = array[i][0]
                break

    print(trabalho)
    print(resultado)


arr = [['a', 2, 100],
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]

sequenciamento_tarefas(array=arr, t=3)
