def max_recursive(lista, number):
    if number == 1:
        return lista[0]
    else:
        x = int()
        x = max_recursive(lista=lista, number=number - 1)
        if x > lista[number - 1]:
            return x
        else:
            return lista[number - 1]


lll = [2, 5, 3, 40, 29, 49, 23, 1]
maxi = max_recursive(lista=lll, number=len(lll))
print(lll)
print(f'O maior número do array é: {maxi}')