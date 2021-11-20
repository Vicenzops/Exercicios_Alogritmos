minimo = int(input("Digite o valor mínimo em graus C: "))
maximo = int(input("Digite o valor máximo em graus C: "))

print("%18s %18s" % ("Temperatura em C", "Temperatura em F"))
for i in range(minimo, maximo +1,5):
    print("%18d %18d" % (i, i*9/5+32))