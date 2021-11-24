#Leia um valor inteiro n. Apresente o quadrado de cada um dos valores pares, de 1 até n, inclusive n, se for o caso.

n = int(input())
y = 2
for i in range(1, n+1):
    if i % 2 == 0:
        print("{0}^{1} = {2}".format(i,y,i**y))