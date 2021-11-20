from math import *

carro = []
km=[]
i = 0
n = 0
while i < 5:
    carro.append(input())
    i += 1
while len(km)< len(carro):
    km.append(int(input()))

for indice in range(len(km)):
    if km[indice] == max(km):
        print(carro[indice])

while n < 5:
    print(round(1000/km[n]))
    n += 1