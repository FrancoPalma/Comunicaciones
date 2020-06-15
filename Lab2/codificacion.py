p=1
for i in range(30):
    file = open("Archivos/Archivo"+str(p)+".txt", "r")
    texto = ""
    min=99
    count=0
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
        if ((int(binario[0])+int(binario[2])+int(binario[4]))%2) == 0:
            binario+=str(0)
        else:
            binario+=str(1)
        file2.write(binario)
        for i in binario:
            if i =='1':
                count+=1
        if count < min and count != 0:
            min = count
    file2.write("\nEl minimo es: "+str(min))
    file2.close()
    p+=1
