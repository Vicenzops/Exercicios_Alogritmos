def acha_palavra(palavra):
    arquivo = open('busca.txt', 'r')
    palavras = []
    k = 0
    for linha in arquivo.readlines():
        linha_separada = linha.split()
        palavras.append(linha_separada)
    for p in range(len(palavras)):
        for l in range(len(palavras[p])):
            if palavras[p][l] == palavra:
                k += 1
    print(k)
    arquivo.close()