def line_count():
    lista =[]
    k = 0
    arquivo = open('story.txt', 'r')
    for linha in arquivo.readlines():
        linha_separada = linha.split()
        lista.append(linha_separada)
    for p in range(len(lista)):
        for n in range(len(lista[p])):
            if lista[p][n] == 'E' or lista[p][n] == 'Em':
                k += 1
    print("Numero de linhas que nao comecam com 'E'=", len(lista) - k) 
    arquivo.close()