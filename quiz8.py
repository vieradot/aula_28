import random

def embaralhar_lista(lista):
    lista_embaralhada = lista[:]
    random.shuffle(lista_embaralhada)
    return lista_embaralhada
