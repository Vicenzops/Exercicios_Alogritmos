from tkinter import *
from tkinter import messagebox
import random
import os


window = Tk()

#Janela
window.title("Cadastro")
window.geometry('450x300')

#Label
rotLab = Label(window, text="Cadastro de Usuário", font=("Times New Roman", 15))
rotNome = Label(window, text="Nome:", font=("Times New Roman", 15))
rotNasc = Label(window, text="Data de Nascimento:", font=("Times New Roman", 15))
rotNasc2 = Label(window, text="(dd/mm/aaaa)", font=("Times New Roman", 10))
rotEnd = Label(window, text="Endereço:", font=("Times New Roman", 15))
rotProf = Label(window, text="Profissão:", font=("Times New Roman", 15))

rotLab.place(x=223,y=20, anchor=CENTER)
rotNome.place(x=55,y=40)
rotProf.place(x=55,y=65)
rotEnd.place(x=55,y=95)
rotNasc.place(x=25,y=125)
rotNasc2.place(x=55,y=145)

#Entry
entrNome = Entry(window, width=20, font=("Times New Roman", 15), text="")
entrNasc = Entry(window, width=20, font=("Times New Roman", 15))
entrEnd = Entry(window, width=20, font=("Times New Roman", 15), text="")
entrProf = Entry(window, width=20, font=("Times New Roman", 15), text="")

entrNome.place(x=300,y=50,anchor=CENTER)
entrProf.place(x=300,y=80, anchor=CENTER)
entrEnd.place(x=300,y=110, anchor=CENTER)
entrNasc.place(x=300,y=140, anchor=CENTER)



def cadastro():
    idi = random.randrange(10000, 99999)    #Gera o id aleatoriamente
    ids = str(idi)
    if os.path.isfile(ids+'.txt'):
        resp = messagebox.showerror('Erro!', 'Usuário já Cadastrado!')
    else:
        nome = entrNome.get()
        nasc = entrNasc.get().replace("/", " ")
        ende = entrEnd.get()
        prof = entrProf.get()           #recebe o que foi escrito na entry


        
        arqv = open(ids+'.txt', 'w')     #cria um novo arquivo baseado no id gerado
        
        arqv.write('%s\n' % ids)
        arqv.write('%s\n' % nome)
        arqv.write('%s\n' % ende)
        arqv.write('%s\n' % prof)                #escreve no arquivo
        arqv.write('%s\n' % nasc)
        arqv.close()

        arqv = open(ids+'.txt', 'r')
        leitor = arqv.readlines()         
        arqv.close()                      
        dados = []                          
        for y in leitor:                    
            organizador = y.split()         
            dados.append(organizador)
        idade_usr = 2021 - int(dados[-1][2])

        arqv = open(ids+'.txt', 'a')
        arqv.write('%s\n' % idade_usr)
        arqv.close()
        
        entrNome.delete(0, END)
        entrNasc.delete(0, END)
        entrEnd.delete(0, END)
        entrProf.delete(0, END)         #apaga o que foi escrito nas entry´s

        resp = messagebox.showinfo('Sucesso!', 'O Usuário foi Cadastrado!')


#Botão
btn = Button(window, text="Cadastrar", command=cadastro)
btn.place(x=225,y=200, anchor=CENTER)

window.mainloop()