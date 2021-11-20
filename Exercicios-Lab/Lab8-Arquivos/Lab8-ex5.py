def ao_quadrado():
    arquivo = open('quadrado.txt', 'r')
    lista = []
    for linha in arquivo.readlines():
        linha_separada = int(linha.strip())
        lista.append(linha_separada)
    for l in range(len(lista)):
        lista[l] = lista[l]**2
    print(lista)
    arquivo.close()