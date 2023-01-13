def max_recursive(lista, tamanho):
    if tamanho == 1:
        return lista[0]
    else:
        x = int()
        x = max_recursive(lista=lista, tamanho=tamanho - 1)
        if x > lista[tamanho - 1]:
            return x
        else:
            return lista[tamanho - 1]


l = [2, 5, 3, 40, 29, 49, 23, 1]
maxi = max_recursive(lista=l, tamanho=len(l))
print(l)
print(f'O maior número do array é: {maxi}')