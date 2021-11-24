#Faça um programa que leia um valor N. 
#Este N será o tamanho de um vetor X[N]. 
#A seguir, leia cada um dos valores de X, encontre o menor elemento deste vetor 
#e a sua posição dentro do vetor, mostrando esta informação.

n = int(input("Digite o valor de N:"))
menor = 100
pos = 0

lista = []
for i in range(1,n+1):
    a = int(input("Digite o %i valor de X:" %(i)))
    lista.append(a)

for i in range(len(lista)):
    if lista[i] < menor:
        menor = lista[i]
        pos = i
print('Menor valor:', menor)
print('Posicao:', pos)
