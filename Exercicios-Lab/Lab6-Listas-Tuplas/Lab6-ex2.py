lista=[]
menor = []
maior = []
i = 1
m = 0
n = 0
while i != 0:
    i = int(input())
    if i < 0:
        menor.append(i)
    elif i > 0:
        maior.append(i)
for n in range(len(menor)):
    lista.append(menor[n])
    n += 1
for m in range(len(maior)):
    lista.append(maior[m])
    m += 1

print(lista)