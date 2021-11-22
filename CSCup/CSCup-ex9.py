#[Python] Faça um código que conte a quantidade de palavras que aparecem em um texto. 
# Crie uma função chamada ContaPalavras() e chame ela no main. Caracteres "!", "?", ",", "." e """ não devem ser contados, 
# como também as letras maiúsculas devem ser ignoradas.

word = input()
def ContaPalavras(word):

    txt = word.lower()
    txt = txt.replace("!", "").replace("?", "").replace(",", "").replace("'", "").replace(".", "").replace('"', "")
    novoTxt = txt.split()
    
    dicionario = {}
    for palavra in novoTxt:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1

    return print(dicionario)

def main():
    ContaPalavras(word)

main()