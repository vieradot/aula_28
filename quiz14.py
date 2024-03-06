import csv

def ler_arquivo_csv(nome_arquivo):
    dados = []
    with open(nome_arquivo, 'r', newline='') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            dados.append(linha)
    return dados
