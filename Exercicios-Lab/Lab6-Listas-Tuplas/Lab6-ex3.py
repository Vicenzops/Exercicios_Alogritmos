from math import *
x = []
soma = 0
dpi = 0
N = int(input('Qual o tamanho da lista: '))

print('Digite os valores:')
for i in range(N):
    x.append(float(input('')))

for i in x:
    soma += i
media = soma / len(x)

sun = 0
for i in x:
    sun += ((i-media)**2)
    dpi = sqrt((sun/N))

print('Média = {0:.2f} e Desvio = {1:.4f}'.format(media, dpi))