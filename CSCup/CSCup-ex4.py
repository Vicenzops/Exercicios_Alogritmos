#[Python] Você está trabalhando em um sistema de comunicação. 
# Porém, todos os valores que você recebe vem no formato de string. 
# Para isso, utiliza-se o caracter _ para definir uma quebra de parâmetros. 
# Você recebe mensagens no seguinte formato "<Nome>_<CPF>_<e-mail>". 
# Crie uma função chamada separate e realize a separação dessa mensagem e exiba as informações de forma separada. 
# Caso um CPF não tenha o tamanho de 11 dígitos e os caracteres . e - deve ser mostrado uma mensagem de CPF inválido. 
# Caso o e-mail não possua o domínio (a parte que fica depois do @), uma mensagem de e-mail inválido deve ser exibida.

x = input()
x=x.split("_")
nome = ""
cpf = ""
email = ""
for i in x:
    y = i.isalpha()
    if (i.count(".") == 2) and (i.count("-") == 1):
        cpf = i
    elif y == True:
        if cpf == "":
            nome += i + " "
        else:
            pass
    else:
        if i.find("@") > 0:
            email = i
        else:
            email = "Inválido"
            cpf = "Inválido"

nome = nome.strip(" ")

print("Nome:" ,nome)
print("CPF:" ,cpf)
print("e-mail:" ,email)