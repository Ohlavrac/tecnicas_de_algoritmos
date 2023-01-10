def maxRecursive(array, number):
    if number == 1:
        return array[0]
    else:
        x = int()
        x = maxRecursive(array=array, number=number-1)
        if x > array[number-1]:
            return x
        else:
            return array[number-1]
        
array = [2, 5, 3, 40, 29, 49, 23, 1]
max = maxRecursive(array=array, number=len(array))
print(array)
print(f'O maior numero do array é: {max}')