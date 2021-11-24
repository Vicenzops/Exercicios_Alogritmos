s=str(input("Entre com uma string: "))
s.islower()
s = s.upper()
s = s.lower()
words=s.split()
count=0
palavras = {}
for word in words:
    word = word.replace(",","")
    palavras[word] = s.count(word)
    count = count + 1

print(palavras)

#Executando o programa, se o usuário digitar a palavra: Dd, aa Aa, dd dD,
#Qual será o conteúdo da variável palavras (na função print) ?