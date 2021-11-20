L= []
I = []
P = []
i = 0

while i < 20 :
    entrada = int(input())
    L.append(entrada)
    if entrada % 2 == 0:
        P.append(entrada)
    elif entrada % 2 != 0:
        I.append(entrada)
    i+= 1

print(*L)
print(*I)
print(*P)