#Faça um programa que leia uma lista N[10]. Troque a seguir, 
#o primeiro elemento com o último, o segundo elemento com o penúltimo, etc., 
#até trocar o 5º com o 6º. Mostre a lista modificada.

N=[]

for i in range(10):
    N.append(int(input()))

reverse=[]
for i in range(len(N)-1,-1,-1):
    reverse.append(N[i])

for i in range(len(reverse)):
    print(f'N[{i}] = {reverse[i]}')