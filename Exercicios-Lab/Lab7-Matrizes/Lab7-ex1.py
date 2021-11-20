M = []
maior = 0

for num_linha in range(2):
    linha = []
    for num_coluna in range(2):
        linha.append(int(input('Digite o elemento da linha %d e coluna %d: ' % (num_linha,num_coluna))))
    M.append(linha)

for linha in range(2):
    for coluna in range(2):
        if M[linha][coluna] > maior:
            maior = M[linha][coluna]

print('Matriz resultante:')
for linha in range(len(M)):
    for coluna in range(len(M[linha])):
        M[linha][coluna] = M[linha][coluna] * maior
        print('%3d' % M[linha][coluna], end=' ')
    print()