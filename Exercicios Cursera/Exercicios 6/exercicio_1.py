def remove_repetidos(lista):
    set_values = set(lista)
    lista_valor = list(set_values)
    lista_valor.sort()
    return lista_valor
