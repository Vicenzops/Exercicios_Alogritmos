#[Python] Escreva uma função chamada procuraReversa que encontre todas as chaves, 
#em um dicionário, que estão associadas a um valor específico. A função receberá o dicionário e o valor a procurar como seus únicos parâmetros. 
#A função retornará uma lista (possivelmente vazia) de chaves associadas ao valor fornecido. 

#Faça um programa principal que mostra a o funcionamento da função. 
#Seu programa principal deve criar um dicionário e mostrar que a função procuraReversa funciona corretamente quando retorna várias chaves, uma única chave ou nenhuma chave.
# O dicionário sempre deverá conter 8 chaves ao todo.

dicionario = {}
valor = int(input())
def procuraReversa(dicionario, item):
    lista = []
    for chave, valor in dicionario.items():
        if valor == item:
            lista.append(chave)

    return lista


def main():
    
    i=0
    while i <8:
        key = input()
        value = int(input())
        dicionario[key] = value
        i+=1
    
    print(procuraReversa(dicionario, valor))


main()