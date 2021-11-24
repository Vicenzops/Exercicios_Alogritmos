#Nessa questão você deve completar o código que contém 3 funções para solucionar os três problemas abaixo:
#Uma função chamada mínimo que recebe dois parâmetros e retorna o menor dos dois.
#Uma função chamada máximo que recebe dois parâmetros e retorna o maior dos dois.
#Uma função chamada múltiplos que recebe dois parâmetros e retorna True se o número do primeiro parâmetro for múltiplo do número do segundo parâmetro.
#esponda corretamente para que o programa funcione corretamente e conforme especificado acima. 
#(Atenção: o programa deverá funcionar conforme a especificação acima atendendo os requisitos descritos.)


def minimo(x,y):
    if x > y:
        return y
    else:
        return x


def maximo(x, y):
    if  x < y:
        return y
    else:
        return x

def multiplo(x,y):
    return(x%y==0)