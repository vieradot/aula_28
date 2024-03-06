def encontrar_par_soma(lista, soma_desejada):
    pares = []
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] + lista[j] == soma_desejada:
                pares.append((lista[i], lista[j]))
    return pares
