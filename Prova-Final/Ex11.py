from random import randint

p = input()

m = []

for i in range(12):
    linha = []
    for i in range(12):
        linha.append(randint(0,10))
    m.append(linha)


print("Matriz criada:")
for linha in range(len(m)):
    for coluna in range(len(m[linha])):
        print('%3d' % m[linha][coluna], end=' ')
    print()

if p == "S":
    soma = 0
    for linha in range(len(m)):
        for coluna in range(len(m[linha])):
            if (linha == 0) :
                pass
            elif (linha == 11) and (1<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 10) and (2<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 9) and (3<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 8) and (4<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 7) and (5<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 6) and (6<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 5) and (7<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 4) and (8<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 3) and (9<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 2) and (10<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 1) and (coluna==11):
                soma += m[linha][coluna]

    print(f"Resultado da conta: {soma}")

elif p== "M":
    soma = 0
    for linha in range(len(m)):
        for coluna in range(len(m[linha])):
            if (linha == 0) :
                pass
            elif (linha == 11) and (1<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 10) and (2<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 9) and (3<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 8) and (4<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 7) and (5<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 6) and (6<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 5) and (7<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 4) and (8<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 3) and (9<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 2) and (10<=coluna<=11):
                soma += m[linha][coluna]
            elif (linha == 1) and (coluna==11):
                soma += m[linha][coluna]
    
    media = soma/66
    media = round(media)
    print(f"Resultado da conta: {media}")

