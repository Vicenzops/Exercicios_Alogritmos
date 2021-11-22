#[Python] Faça um  programa que leia um número inteiro que representa um código de DDD para discagem interurbana. 
# Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:

# https://moodle.fei.edu.br/pluginfile.php/90972/question/questiontext/82019/38/201090/image.png

#Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
#DDD não cadastrado.

x = int(input())

if x == 61:
    print('Brasilia')
if x == 71:
    print('Salvador')
if x == 11:
    print('Sao Paulo')
if x == 21:
    print('Rio de Janeiro')
if x == 32:
    print('Juiz de Fora')
if x == 19:
    print('Campinas')
if x == 27:
    print('Vitoria')
if x == 31:
    print('Belo Horizonte')
if x != 61 and  x != 71 and x != 11 and x != 21 and x != 32 and x != 19 and x != 27 and x != 31:
    print('DDD nao cadastrado')