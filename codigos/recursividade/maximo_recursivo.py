def max_recursive(lista, numero):
    if numero == 1:
        return lista[0]
    else:
        x = int()
        x = max_recursive(lista=lista, numero=numero - 1)
        if x > lista[numero - 1]:
            return x
        else:
            return lista[numero - 1]


l = [2, 5, 3, 40, 29, 49, 23, 1]
maxi = max_recursive(lista=l, numero=len(l))
print(l)
print(f'O maior número do array é: {maxi}')