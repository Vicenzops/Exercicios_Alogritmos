#[Python] Bases de numeração podem facilitar ou dificultar a forma como interpretamos algum valor numérico. 
# Portanto, é desejável que tenhamos noção e sejamos capazes de trabalhar com as base binária, decimal e hexadecimal. 
# Implemente um algoritmo que possa realizar essa conversão de base, 
# lembre-se que será primeiro passado o tipo da base do número original e em seguida o número em formato de string.

base = input()
num = input()

if base == 'b':
    dec = int(num, 2)
    num = int(num)
    hexa = hex(num).replace('0x','')
    print(f'Decimal = {dec}\nHexadecimal = {hexa[-1]}')
elif base == 'd':
    num = int(num)
    bina = format(num, 'b')
    hexa = format(num, 'X')
    print(f'Binário = {bina}\nHexadecimal = {hexa}')
elif base == 'h':
    dec = int(num, 16)
    bina = str(bin(int(num, 16)))[2:]
    print(f'Binário = {bina}\nDecimal = {dec}')