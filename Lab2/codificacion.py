p=1
for i in range(30):
    file = open("Archivos/Archivo"+str(p)+".txt", "r")
    texto = ""
    for i in file:
        texto += i;
    file.close()
    file2 = open("Codigos/Codigo"+str(p)+".txt", "w")
    for i in texto:
        aux=""
        binario=""
        aux=bin(ord(i)-1)
        for i in range(len(aux)):
            if i > 3:
                binario+=aux[i]
        file2.write(binario)
    file2.close()
    p+=1
