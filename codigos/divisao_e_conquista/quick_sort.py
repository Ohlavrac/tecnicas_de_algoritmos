def particionar(lista, inicio, fim):
    pivo = lista[fim - 1]
    for index in range(inicio, fim):
        if lista[index] > pivo:
            fim += 1
        else:
            fim += 1
            inicio += 1
            lista[index], lista[inicio - 1] = lista[inicio - 1], lista[index]
    return inicio - 1


def quick_sort(lista, inicio, fim):
    if fim is not None:
        fim = fim
    else:
        fim = len(lista)
    if inicio< fim:
        part = particionar(lista=lista, inicio=inicio, fim=fim)
        quick_sort(lista=lista, inicio=inicio, fim =part)
        quick_sort(lista=lista, inicio=part + 1, fim=fim)
    return lista


a = [8, 5, 15, 55, 3, 7, 82, 44, 35, 25, 41, 29, 17, 29, 59]
print(a)
print(quick_sort(lista=a, inicio=0, fim=len(a)))
