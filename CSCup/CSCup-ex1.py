#[Python] Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, incluse o X se for o caso.

x = int(input())
impar = 0
while impar < 12:
    impar += 1
    if x % 2 != 0:
        print(x)
    x += 1