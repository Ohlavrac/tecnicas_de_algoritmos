def isSubSetSum(number, set, sum):
    subset = ([False for index in range(sum + 1)] for index in range(number + 1))
    
    for index in range(number + 1):
        subset[index][0] = True
    
    for index in range(1, sum + 1):
        subset[0][index] = False
        
    for index in range(1, number + 1):
        for index2 in range(1, sum + 1):
            if index2 < set[index - 1]:
                subset[index][index2] = subset[index-1][index2]
            if index2 >= set[index - 1]:
                subset[index][index2] = (subset[index - 1][index2] or subset[index - 1][index2 - set[index - 1]])
    
    return subset[number][sum]

set = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(set)
if (isSubSetSum(set, n, sum) == True):
    print("Encontrado o subset com a determinada soma")
else:
    print("Subset não encontrado")