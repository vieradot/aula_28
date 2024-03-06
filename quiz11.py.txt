def is_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def numeros_primos(lista):
    primos = []
    for num in lista:
        if is_primo(num):
            primos.append(num)
    return primos
