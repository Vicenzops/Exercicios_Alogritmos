n = int(input("Digite n: "))
m = int(input("Digite m: "))
mdc = n

while n % mdc != 0 or m % mdc != 0: 
    mdc = mdc - 1

print(mdc)