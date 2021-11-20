# 5
a = []
b = []
tam = int(input('Digite a dimensão dos vetores: '))
soma = 0
n = 0
m = 0

print('Digite o vetor 1:')
while n < tam:
    a.append(int(input()))
    n+=1

print('Digite o vetor 2:')
while m < tam:
    b.append(int(input()))
    m += 1
    
for i, j in zip(a, b):
    # for j in range(len(b)):
    soma += i * j

print(soma)