M = []
i = 0

for num_linha in range(4):
    linha = []
    for num_coluna in range(2):
        linha.append(int(input('Digite o elemento da linha %d e coluna %d: ' % (num_linha,num_coluna))))
    M.append(linha)

print('Matriz original:')
for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        print('%3d' % M[linha][coluna], end=' ')
    print()
print()
for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        if M[linha][coluna] > 10:
            print('%d é maior que 10!' % M[linha][coluna])
            i += 1
print('No total, %d elementos são maiores que 10!' % i)

print('\nMatriz sem os números maiores que 10:')
for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        if M[linha][coluna] > 10:
            M[linha][coluna] = 0
        print('%3d' % M[linha][coluna], end=' ')
    print()