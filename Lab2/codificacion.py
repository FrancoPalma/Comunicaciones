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
        if ((int(binario[0])+int(binario[1])+int(binario[2]))%2) == 0:
            binario+=str(0)
        else:
            binario+=str(1)
        if ((int(binario[1])+int(binario[2])+int(binario[3]))%2) == 0:
            binario+=str(0)
        else:
            binario+=str(1)
        if ((int(binario[2])+int(binario[3])+int(binario[4]))%2) == 0:
            binario+=str(0)
        else:
            binario+=str(1)
        if ((int(binario[3])+int(binario[4])+int(binario[5]))%2) == 0:
            binario+=str(0)
        else:
            binario+=str(1)
        file2.write(binario)
    file2.close()
    p+=1
