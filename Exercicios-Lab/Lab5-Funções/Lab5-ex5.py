planeta = input('Digite o o nome do planeta desejado: ')
peso = float(input('Digite o peso da pessoa na Terra em kg: '))

def pesoPessoa(planeta, peso):
    if planeta == 'Mercúrio':
        pesoPlaneta = peso * 0.37
    elif planeta == 'Vênus':
        pesoPlaneta = peso * 0.88
    elif planeta == 'Marte':
        pesoPlaneta = peso * 0.38
    elif planeta == 'Júpiter':
        pesoPlaneta = peso * 2.64
    elif planeta == 'Urano':
        pesoPlaneta = peso * 1.17
    elif planeta == 'Netuno':
        pesoPlaneta = peso * 1.18
    return pesoPlaneta
    
print('Peso em %s: %.2f' % (planeta, pesoPessoa(planeta, peso)))