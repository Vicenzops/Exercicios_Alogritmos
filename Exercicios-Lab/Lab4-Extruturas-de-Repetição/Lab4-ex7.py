x = int(input('Digite o número desejado: '))
p = x/2
erro = abs(p**2 - x)
while erro > 10**-12:
    p = (p +(x/p))/ 2
    erro = p**2 - x 
print("%.3f" % (p))