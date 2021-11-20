def lista_arquivo(cores):
    arquivo = open('arquivo.txt', 'w')
    for i in cores:
        arquivo.write('%s\n' %i)
    arquivo.close()
    arquivo = open('arquivo.txt', 'r')
    for p in arquivo.readlines():
        print(p.strip())