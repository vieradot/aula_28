def substituir_letra(string, letra_antiga, letra_nova):
    nova_string = ''
    for letra in string:
        if letra == letra_antiga:
            nova_string += letra_nova
        else:
            nova_string += letra
    return nova_string

string = input("Digite a palavra que deseja alterar: ")
letra_antiga = input("Qual letra deseja alterar de '{}': ".format(string))
letra_nova = input("Por qual letra deseja substituir a antiga? ")

nova_palavra = substituir_letra(string, letra_antiga, letra_nova)
print("Nova palavra:", nova_palavra)
