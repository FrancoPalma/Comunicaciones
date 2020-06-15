from random import randrange
p=1
for i in range(30):
    file = open("Codigos/Codigo"+str(p)+".txt", "r")
    texto = ""
    aux=""
    for i in file:
        texto += i;
    file.close()
    file2 = open("CodCE0001/CodigoCE"+str(p)+".txt", "w")#Los guardo en CodicosConError
    for i in texto:
        if i == '1' or i == '0':
            if randrange(1000) < 1: #aca marca la probabilidad de que salga 0 entre 0 a 9 ----> 0.1
                if i == '1':
                    file2.write('0')
                else:
                    file2.write('1')
            else:
                file2.write(i)
        else:
            file2.write(i)
    file2.close()
    p+=1
