def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = len([char for char in palavra if char in vogais])
    print("Número de vogais:", contador)
 
palavras = ['camargo', 'teste']
for palavra in palavras:
    contar_vogais(palavra)