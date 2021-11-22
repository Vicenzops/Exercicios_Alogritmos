#[Python] Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números ímpares entre eles.

x = int(input())
y = int(input())

maior = x if x > y else y
menor = y if y < x else x
menor+=1
soma = 0

while (menor < maior):
    if(menor % 2 != 0):
        soma+=menor
    menor+=1
print(soma)