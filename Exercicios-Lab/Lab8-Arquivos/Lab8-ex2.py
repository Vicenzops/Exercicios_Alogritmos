def conta_palavras():
    file = open("palavras.txt","r")
    count = 0
    data = file.read()
    words = data.split()
    for word in words:
        count += 1
    print("Quantidade de palavras: ",count)
    file.close()