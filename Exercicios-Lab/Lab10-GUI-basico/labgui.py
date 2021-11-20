from tkinter import *
from tkinter import scrolledtext

window = Tk()

#Janela
window.title("Filtro de Palavras")
window.geometry('800x700')

#Scrolledtext
txt = scrolledtext.ScrolledText(window, width=95, height=30)
txt.place(relx=0.5, rely=0.55, anchor=CENTER)

#Label
rotulo1 = Label(window, text="Palavra Suspeita:", font=("Times New Roman", 15))
rotulo2 = Label(window, text="Frequência:", font=("Times New Roman", 15))
rotulo3 = Label(window, text="Ocorrências:", font=("Times New Roman", 15))

rotulo1.place(x=15,y=5)
rotulo2.place(x=30,y=30)
rotulo3.place(x=30,y=100)

#Entry
entrada1 = Entry(window, width=20, font=("Times New Roman", 15))
entrada2 = Entry(window, width=20, font=("Times New Roman", 15), text="")

entrada1.place(x=260,y=20,anchor=CENTER)
entrada2.place(x=260,y=50, anchor=CENTER)

def incidenciaPalavras():
    entrada2.delete(0, END)
    txt.delete(1.0, END)
    frequencia = 0
    word = entrada1.get()
    
    arqWord = []
    arquivo = open('chat.txt', 'r')
    for i in arquivo.readlines():
        arqWord.append(i.strip().split())
    arquivo.close()
    
    for i in range(len(arqWord)):
        for k in range(len(arqWord[i])):
            if word.lower() == arqWord[i][k].lower().replace('!', '').replace('?', '').replace(',', '').replace('.', '').replace(': -)', '').replace('*', ''):
                arqWord[i][-1] = arqWord[i][-1]+'\n\n'
                txt.insert(1.0, ' '.join(arqWord[i]))
                frequencia+=1
    
    entrada2.insert(0, frequencia)


#Botão
btn = Button(window, text="Pesquisar", command=incidenciaPalavras)
btn.place(x=395,y=20, anchor=CENTER)



window.mainloop()