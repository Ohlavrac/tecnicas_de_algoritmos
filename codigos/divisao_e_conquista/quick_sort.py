def particion(lista, start, end):
    pivo = lista[end - 1]
    for index in range(start, end):
        if lista[index] > pivo:
            end += 1
        else:
            end += 1
            start += 1
            lista[index], lista[start - 1] = lista[start - 1], lista[index]
    return start - 1


def quick_sort(lista, start, end):
    if end is not None:
        end = end
    else:
        end = len(lista)
    if start < end:
        part = particion(lista=lista, start=start, end=end)
        quick_sort(lista=lista, start=start, end=part)
        quick_sort(lista=lista, start=part + 1, end=end)
    return lista


a = [8, 5, 15, 55, 3, 7, 82, 44, 35, 25, 41, 29, 17, 29, 59]
print(a)
print(quick_sort(lista=a, start=0, end=len(a)))
