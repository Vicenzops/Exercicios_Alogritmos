n = int(input("Digite o número desejado: "))
cont = 0
i = 0

while i <= n or cont < 2:
    i = i + 1
    x = n % i
    if x == 0:
        cont = cont + 1

if cont <= 2:
    print("Número primo")
else:

    print("Número não primo")