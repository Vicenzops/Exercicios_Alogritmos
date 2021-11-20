import os
#Biblioteca para requerir o dia e hora (servira para o extrato!)
from datetime import datetime

def identificaSenha(op = None):
    cpf = input ('Digite o CPF: ')          #Requer o CPF ao usuario
    if os.path.isfile(cpf+'.txt'):          #confere se existe um arquivo com cpf referente
        arquiv = open(cpf+'.txt', 'r')      #Abre tal arquivo
        senha = input('Digite uma Senha: ') #Requer uma senha ao usuario
        leitor = arquiv.readlines()         #Variavel que lê as linhas do arquivo
        arquiv.close()                      #Fechamento do arquivo
        dados = []                          #Dados é uma lista que vai armazenaras linhas do arquivo
        for y in leitor:                    #Para cada elemento lido
            organizador = y.split()         #Organizador guarda cada elemento sem o \n
            dados.append(organizador)       #Adiciona na lista dados os elementos sem o \n
    else:
        print('\nCPF incorreto e/ou Conta inexistente!\n') #Registra que o CPF esta errado ou inexistente
    if op:                                  #Se op tiver um valor diferente de None
        return dados, senha, cpf            #Retorna os valores dados, senha e cpf
    else:
        return dados, senha                 #Retorna os valores dados, senha

#Criação do Usuario!
def criarClient():
    data_e_hora_atuais = datetime.now()     #Define a data e hora atual utilizando a biblioteca datetime
    nome = input('Digite o nome: ')         #Requer o nome do usuario
    cpf = input('Digite o CPF: ')           #Requer o cpf do usuario
    if os.path.isfile(cpf+'.txt'):          #confere se existe um arquivo com cpf referente
        print('\nCliente ja registrado!\n')     #Diz que o cliente ja existe
    else:
        contaTipo = input('Digite o tipo de conta(Salário, Comum, Plus): ') 
        valInicial = float(input('Digite o Valor inicial da Conta: '))
        senha = input('Digite uma Senha: ')
        arquiv = open(cpf+'.txt', 'w')  
        arquiv.write('%s\n' % nome)         #Arquiva o nome inserido pelo usuario
        arquiv.write('%s\n' % senha)        #Arquiva a senha inserido pelo usuario
        arquiv.write('%s\n' % cpf)          #Arquiva o cpf inserido pelo usuario
        arquiv.write('%s\n' % contaTipo)    #Arquiva o tipo de conta inserido pelo usuario
        arquiv.write('Data:{0} + {1:.2f} Tarifa:0.00 Saldo: {2:.2f} \n' #Arquiva a data em ano/mes/ano hora:minutos + quantidade inicial, Tarifa e saldo
        .format(data_e_hora_atuais.strftime('%Y-%m-%d %H:%M'), valInicial, valInicial))
        arquiv.write('%.2f\n' % valInicial) #Arquiva o valor inicial                                           
        arquiv.close()
        print('\nConta criada com sucesso!\n')

#Função para apagar a conta
def apagarClient():
    dados, senha, cpf = identificaSenha(1)  #Retornas os dados do usuario que serão manipulados
    if dados[1][0] == senha:                #Se o dado referente a senha for igual a senha inserida pelo usuario
        os.remove(cpf+'.txt')               #os.remove() apaga o arquivo, removendo os dados do usuario do sistema
        print('\nConta apagada!\n')           #Retorna que a conta foi apagada
    elif dados[1][0] != senha:              #Se o dado referente for diferente a senha inserida pelo ususario
        print('\nSenha incorreta!\n')         #Retorna que a senha esta incorreta

#Debitar um valor na conta1
def debitar():
    data_e_hora_atuais = datetime.now()         #Define a data e hora atual utilizando a biblioteca datetime
    dados, senha, cpf = identificaSenha(1)      #Retornas os dados do usuario que serão manipulados
    if dados[1][0] == senha:                    #Se o dado referente a senha for igual a senha inserida pelo usuario
        arquiv = open(cpf+'.txt', 'a')          #abre o arquivo para dar append
        valDebit = float(input('\nDigite o valor que deseja debitar: ')) #Requer o valor que deseja ser debitado
        if dados[3][0] == 'Salário':            #Relaciona o tipo de conta
            dados[-1][0] = float(dados[-1][0]) - valDebit*1.05 #Utiliza o dado inserido para fazer o calculo das taxações
            if float(dados[-1][0]) >= 0:        #Confere se a conta vai ficar negativada ou não
                tarifa = valDebit*0.05          #Calcula a tarifa baseada no tipo de conta
                arquiv.write(('Data: {0} - {1:.2f} Tarifa: {2:.2f} Saldo: {3:.2f} \n'.format(data_e_hora_atuais.strftime('%Y-%m-%d %H:%M'),valDebit, tarifa,dados[-1][0]))) #Arquiva a data em ano/mes/ano hora:minutos - quantidade debitada, Tarifa cobrada e saldo
                arquiv.close()
                print('\nValor debitado com sucesso!\n')
            elif float(dados[-1][0]) < 0:
                print('\nContas Salário não podem ter saldo negativo!\n') #Diz que a conta esta negativa
        elif dados[3][0] == 'Comum':            #Relaciona o tipo de conta
            dados[-1][0] = float(dados[-1][0]) - valDebit*1.03 #Utiliza o dado inserido para fazer o calculo das taxações
            if float(dados[-1][0]) >= -500:     #Confere se a conta vai ficar negativada ou não
                tarifa = valDebit*0.03          #Calcula a tarifa baseada no tipo de conta
                arquiv.write(('Data: {0} - {1:.2f} Tarifa: {2:.2f} Saldo: {3:.2f} \n'.format(data_e_hora_atuais.strftime('%Y-%m-%d %H:%M'),valDebit, tarifa,dados[-1][0]))) #Arquiva a data em ano/mes/ano hora:minutos - quantidade debitada, Tarifa cobrada e saldo
                arquiv.write('%.2f\n' % dados[-1][0])
                arquiv.close()
                print('\nValor debitado com sucesso!\n')
            else:
                print('\nContas Comuns não podem ter saldo negativo menor que R$500,00!\n') #Diz que a conta esta negativa
        elif dados[3][0] == 'Plus':             #Relaciona o tipo de conta
            dados[-1][0] = float(dados[-1][0]) - valDebit*1.01 #Utiliza o dado inserido para fazer o calculo das taxações
            if float(dados[-1][0]) >= -5000:    #Confere se a conta vai ficar negativada ou não
                tarifa = valDebit*0.01          #Calcula a tarifa baseada no tipo de conta
                arquiv.write(('Data: {0} - {1:.2f} Tarifa: {2:.2f} Saldo: {3:.2f} \n'.format(data_e_hora_atuais.strftime('%Y-%m-%d %H:%M'),valDebit, tarifa,dados[-1][0]))) #Arquiva a data em ano/mes/ano hora:minutos - quantidade debitada, Tarifa cobrada e saldo
                arquiv.write('%.2f\n' % dados[-1][0])
                arquiv.close()
                print('\nValor debitado com sucesso!\n')
            else:
                print('\nContas Plus não podem ter saldo negativo menor que R$5000,00!\n') #Diz que a conta esta negativa
    elif dados[1][0] != senha:
        print('\nSenha incorreta\n')

#Depositar um valor na conta
def depositar():
    data_e_hora_atuais = datetime.now()         #Define a data e hora atual utilizando a biblioteca datetime
    dados, senha, cpf = identificaSenha(1)      #Retornas os dados do usuario que serão manipulados
    if dados[1][0] == senha:                    #Se o dado referente a senha for igual a senha inserida pelo usuario
        arquiv = open(cpf+'.txt', 'a')          #abre o arquivo para dar append
        valDept = float(input('Digite o valor que deseja depositar: ')) #Requer a quantidade que deseja ser debitada 
        saldo = float(dados[-1][0]) + valDept   #Calcula o saldo total
        arquiv.write('Data:{0} + {1:.2f} Tarifa:0.00 Saldo: {2:.2f} \n'.format(data_e_hora_atuais.strftime('%Y-%m-%d %H:%M'), valDept, saldo)) #Arquiva a data em ano/mes/ano hora:minutos + quantidade inicial, Tarifa e saldo
        dados[-1][0] = float(dados[-1][0]) + valDept #Modifica o ultimo item da lista
        arquiv.write('%.2f\n' % dados[-1][0])   #Escrevre o novo ultimo item da lista
        arquiv.close()                          #Fecha o arquivo
        print('\nDeposito feito com sucesso!\n')
    elif dados[1][0] != senha:
        print('\nSenha incorreta!\n')

#Verificar saldo da conta
def saldo():
    dados, senha = identificaSenha()        #Retornas os dados do usuario que serão manipulados
    if dados[1][0] == senha:                #Se o dado referente a senha for igual a senha inserida pelo usuario
        saldo = float(dados[-1][-1])         #Variavel saldo é a mesma coisa que o ultimo valor de dados
        print("\nSaldo Bancario: %.2f \n" % saldo) #Imprime o saldo bancario
    elif dados[1][0] != senha:
        print('\nSenha incorreta!\n')


#Verificar extrato bancario (nome, cpf, tipo de conta, todas as 
# trandações com data, horario e o que foi feito; Tarifa e saldo.)
def extrato():
    dados, senha= identificaSenha()         #Retornas os dados do usuario que serão manipulados
    if dados[1][0] == senha:                #Se o dado referente a senha for igual a senha inserida pelo usuario
        print()
        print('Nome: %s' % dados[0][0])     #Retorna o nome
        print('CPF: %s' % dados[2][0])      #Retorna o CPF
        print('Conta: %s' % dados[3][0])    #Retorna o tipo da conta
        for i in range(4,len(dados),2):     #Para cada item dentro do tamanho da lista, a partir do quarto, aumenta de 2 em 2
            print(*dados[i])                #Retorna dados[i] sem a formatação de lista
        print()
    elif dados[1][0] != senha:
        print('\nSenha incorreta!\n')



#Criação do Menu interativo!
def menu():
    while True:
        print()
        print('_____ Menu _____')
        print()
        print('1 - Criar Novo Cliente')
        print('2 - Apagar Cliente')
        print('3 - Debitar')
        print('4 - Depositar')
        print('5 - Saldo')
        print('6 - Extrato')
        print()
        print()
        print()
        print('0 - Sair')
        print()

        opcao = input('Escolha uma das opções: ') #Variavel que requer a opção escolhida pelo usuario

        print()

        if opcao == '1':
            criarClient()                   #Realiza a função criarClient()
        elif opcao == '2':
            apagarClient()                  #Realiza a função apagarClient()
        elif opcao == '3':
            debitar()                       #Realiza a função debitar()
        elif opcao == '4':
            depositar()                     #Realiza a função depositar()
        elif opcao == '5':
            saldo()                         #Realiza a função saldo()
        elif opcao == '6':
            extrato()                       #Realiza a função extrato()
        elif opcao == '0':
            break
        else:
            break
menu()                                      #Realiza a função menu()