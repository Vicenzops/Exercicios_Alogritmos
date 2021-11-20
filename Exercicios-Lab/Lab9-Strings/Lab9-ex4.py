def spellChecker(x):
    lista=[]
    nrec=[]
    arquivo = open("words.txt", "r")
    for i in arquivo.readlines():
        lista.append(i.lower().strip())
    fraselow = x.lower().replace(",","").split()
    for i in range(len(fraselow)):
        if fraselow[i] in lista:
            pass
        else:
            nrec.append(fraselow[i])
    return nrec