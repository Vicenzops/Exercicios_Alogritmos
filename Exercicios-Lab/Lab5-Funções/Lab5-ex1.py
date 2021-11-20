from math import sqrt

a = int(input('Digite o primeiro lado do triângulo: '))
b = int(input('Digite o segundo lado do triângulo: '))

def formula(a, b):
    x = sqrt(a**2 + b**2)
    return x
print ('Hipotenusa: {0:.2f}'.format(formula(a, b)))
