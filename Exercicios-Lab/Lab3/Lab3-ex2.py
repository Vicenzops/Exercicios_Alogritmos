dia = int(input('Digite o dia desejado: '))
mes = input('Digite o mês desejado: ')

if mes == 'janeiro':
    print('Verão')
if mes == 'fevereiro':
    print('Verão')
if mes == 'março':
    if 20 <= dia <= 31:
        print('Outono')
    else:
        print('Verão')
if mes == 'abril':
    print('Outono') 
if mes == 'maio':
    print('Outono')
if mes == 'junho':
    if 21 <= dia <= 30:
        print('Inverno')
    else:
        print('Outono')
if mes == 'julho':
    print('Inverno')
if mes == 'agosto':
    print('Inverno')
if mes == 'setembro':
    if 22 <= dia <= 30:
        print('Primavera')
    else:
        print('Inverno')
if mes == 'outubro':
    print('Primavera')
if mes == "novembro":
    print('Primavera')
if mes == 'dezembro':
    if 21 <= dia <= 31:
        print('Verão')
    else:
        print('Primavera')