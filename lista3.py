def contar_palavras(string):
    contador = len(string.split())
    print(contador)

string = input("Digite sua frase para descobrir o número de palavras: ")

contar_palavras(string)