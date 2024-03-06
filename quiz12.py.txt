def menor_string(lista):
    menor = lista[0]
    for string in lista:
        if len(string) < len(menor):
            menor = string
    return menor
