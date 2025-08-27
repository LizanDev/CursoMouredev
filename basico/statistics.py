def media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)


def calcular_mediana(lista):
    if not lista:
        return 0
    sorted_lista = sorted(lista)
    mid = len(sorted_lista) // 2
    if len(sorted_lista) % 2 == 0:
        return (sorted_lista[mid - 1] + sorted_lista[mid]) / 2
    else:
        return sorted_lista[mid]
