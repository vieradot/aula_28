def ler_arquivo_texto(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    return conteudo
