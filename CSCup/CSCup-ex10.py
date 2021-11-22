#[Python] Dado uma matriz 3x3, imprima o segundo maior valor existente na matriz.

m = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input()))
    m.append(linha) 

maximo = m[0][0]
for i in range(3):
    for j in range(3):
        if m[i][j] > maximo:
            maximo = m[i][j]

segMaximo = 0
for i in range(3):
    for j in range(3):
        if m[i][j] > segMaximo and m[i][j] != maximo:
            segMaximo = m[i][j]
print(segMaximo)