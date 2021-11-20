def read_file():
    arquivo = open('poema.txt', 'r')
    for palavra in arquivo:
        print(palavra.strip())