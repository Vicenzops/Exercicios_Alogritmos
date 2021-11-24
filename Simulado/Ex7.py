#A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. 
#Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores.
# Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

n = int(input())
a=1
b=1
lista = [0, 1, 1]
if n==1:
    print('0')
elif n==2:
    print('0','1')
else:
    for i in range(n-3):
        total = a + b
        b = a
        a = total
        lista.append(total)
print(*lista)
