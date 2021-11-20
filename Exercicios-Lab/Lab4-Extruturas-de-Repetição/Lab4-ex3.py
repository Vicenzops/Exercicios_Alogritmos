ano = int(input("Digite o ano desejado: "))
if ano<2007:
    print("Por favor digite um ano maior que 2007.")
else:
    salario = (5000*1.015)*1.030
    aumento = 0.03
    z = ano-2007
    
    while z>0:
        aumento *= 2
        salario *=(aumento+1)
        z -= 1
        
print("Salário de %d: R$ %.2f" % (ano, salario))