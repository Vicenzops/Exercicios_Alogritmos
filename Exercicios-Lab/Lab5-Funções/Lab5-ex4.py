Km = float(input("Digite a quantidade de quilômetros: "))
def tarifa(Km):
    return 10.00 + (0.5 * (Km/0.125))
print("Tarifa %.2f" % tarifa(Km))