palavrasecreta = input("Digite a palavra secreta:")
erro = 0
letra = "-"*len(palavrasecreta)
listaLetra = list(letra)
lower = palavrasecreta.lower()
repetidas =[]
print('''








''')
print(letra)
erro0 = '''X==:==
X  :
X
X
X
X
==========='''
erro1 = '''X==:==
X  :  
X  O  
X     
X     
X     
==========='''
erro2 = '''X==:==
X  :  
X  O  
X  |  
X     
X     
==========='''
erro3 = '''X==:==
X  :  
X  O  
X \|  
X     
X     
==========='''
erro4 ='''X==:==
X  :  
X  O  
X \|/  
X     
X     
==========='''
erro5 = '''X==:==
X  :  
X  O  
X \|/  
X /    
X     
==========='''
erro6 = '''X==:==
X  :
X  O
X \|/
X / \ 
X
===========
Enforcado!'''

while True:
    acerto = 0
    chute = input("\nDigite uma letra:").lower()
    for i in range(len(lower)):
        if chute == lower[i]:
            listaLetra[i] = chute
            letra = "".join(listaLetra)
            acerto += 1
            repetidas.append(chute)
        else:
            pass
    if acerto == 0:
        erro+=1
        if erro == 1:
            print("Você errou!")
            print(erro1)
            print(letra)
        elif erro == 2:
            print("Você errou!")
            print(erro2)
            print(letra)
        elif erro == 3:
            print("Você errou!")
            print(erro3)
            print(letra)
        elif erro == 4:
            print("Você errou!")
            print(erro4)
            print(letra)
        elif erro == 5:
            print("Você errou!")
            print(erro5)
            print(letra)
        elif erro == 6:
            print("Você errou!")
            print(erro6)
    else:
        if erro == 0:
            print(erro0)
            print(letra)
        elif erro == 1:
            print(erro1)
            print(letra)
        elif erro == 2:
            print(erro2)
            print(letra)
        elif erro == 3:
            print(erro3)
            print(letra)
        elif erro == 4:
            print(erro4)
            print(letra)
        elif erro == 5:
            print(erro5)
            print(letra)
    if letra == lower:
        print('Você acertou!')
        break
    elif erro == 6:
        break