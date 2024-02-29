def contar_ocorrencias(frase, palavra):
    palavras_na_frase = frase.split()
    
    contador = 0
    
    for p in palavras_na_frase:
        if p == palavra:
            contador += 1
    
    return contador

frase = "Esta é uma frase de exemplo para contar quantas vezes a palavra exemplo aparece na frase."
palavra_procurada = "exemplo"
ocorrencias = contar_ocorrencias(frase, palavra_procurada)
print("A palavra '{}' ocorre {} vezes na frase.".format(palavra_procurada, ocorrencias))
