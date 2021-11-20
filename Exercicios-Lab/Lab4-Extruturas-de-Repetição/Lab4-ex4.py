N = int(input('Digite o número desejado: '))
e = 1

for I in range(1, N+1):
    e += 1/I
print('%.3f' % (e))