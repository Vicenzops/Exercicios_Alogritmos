n = int(input("Entre com a quantidade de números que serão digitados: "))

c = 1
maior = int(input("1º número : "))

while c < n:
    c += 1
    t = int(input('%dº número : ' % c))
    if t > maior:
        maior = t

print('Maior número digitado:', maior)