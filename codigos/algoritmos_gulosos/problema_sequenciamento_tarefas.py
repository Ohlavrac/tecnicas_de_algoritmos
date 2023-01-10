def sequenciamentoTarefas(array, t):
    size = len(array)
    
    print(f'Array na ordem original: {array}')
    
    for index in range(size):
        for index2 in range(size - 1 - index):
            if array[index2][2] < array[index2 + 1][2]:
                array[index2], array[index2 + 1] = array[index2 + 1], array[index2]
        
    print(f'Array organizado em ordem crescente com base no lucro: {array}')
                
    result = [False] * t
    
    job = ['-1'] * t
    
    print(job)
    print(result)
    
    for index in range(len(array)):
        print('>>>>', min(t - 1, array[index][1] - 1))
        for index2 in range(min(t - 1, array[index][1] - 1), -1, -1):
            if result[index2] is False:
                result[index2] = True
                job[index2] = array[index][0]
                break
            
    print(job)
    print(result)
    
arr = [['a', 2, 100],
			['b', 1, 19],
			['c', 2, 27],
			['d', 1, 25],
			['e', 3, 15]]

sequenciamentoTarefas(array=arr, t=3)