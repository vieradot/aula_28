def intersecao_listas(lista1, lista2):
    intersecao = []
    for item in lista1:
        if item in lista2 and item not in intersecao:
            intersecao.append(item)
    return intersecao
