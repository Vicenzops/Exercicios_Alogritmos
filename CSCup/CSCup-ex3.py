#[Python] Uma cientista quer fazer experimentos com cobaias para saber no final do ano quantas cobaias foram 
# utilizadas no laboratório e o percentual de cada tipo de cobaia. No laboratório utilizam três tipos de cobaias: 
# sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, 
# o tipo da cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

#A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. 
# Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas 
# e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

n = int(input())
c = 0
r = 0
s = 0

for i in range(1 , n + 1):
    x = input().split()
    a, b, = x
    if b == 'C':
        c = c + int(a)
    if b == 'R':
        r = r + int(a)
    if b == 'S':
        s = s + int(a)

total = c + r + s
pc = (c / total) * 100
pr = (r / total) * 100
ps = (s / total) * 100

print('Total: {} cobaias'.format(total))
print('Total de coelhos: {}'.format(c))
print('Total de ratos: {}'.format(r))
print('Total de sapos: {}'.format(s))
print('Percentual de coelhos: {:.2f} %'.format(pc))
print('Percentual de ratos: {:.2f} %'.format(pr))
print('Percentual de sapos: {:.2f} %'.format(ps))