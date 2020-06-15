p=1
for i in range(30):
    file = open("Archivos/Archivo"+str(p)+".txt", "r")
    texto = ""
    aux=""
    codigo = []
    for i in file:
        codigo.append(i)
    file.close()
    cont = 0;
    for i in codigo:
        if codigo[cont] == '0' && codigo[cont + 1] == '0' && codigo[cont +2] == '0':
            



    file2 = open("Codigos/Codigo"+str(p)+".txt", "w")
    file2.write(aux)
    file2.close()
    p+=1
