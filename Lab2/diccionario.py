p=1
for i in range(30):
    file = open("Archivos/Archivo"+str(p)+".txt", "r")
    texto = ""
    binario=""
    for i in file:
        texto += i;
    file.close()

    codigo = []
    l = []
    for i in texto:
        if i == 'a':
            l.append(0)
            l.append(0)
            l.append(0)
            l.append(0)
            l.append(0)

        if i == 'b':
            l.append(0)
            l.append(0)
            l.append(0)
            l.append(0)
            l.append(1)

        if i == 'c':
            l.append(0)
            l.append(0)
            l.append(0)
            l.append(1)
            l.append(0)

        if i == 'd':
            l.append(0)
            l.append(0)
            l.append(0)
            l.append(1)
            l.append(1)

        if i == 'e':
            l.append(0)
            l.append(0)
            l.append(1)
            l.append(0)
            l.append(0)

        if i == 'f':
            l.append(0)
            l.append(0)
            l.append(1)
            l.append(0)
            l.append(1)

        if i == 'g':
            l.append(0)
            l.append(0)
            l.append(1)
            l.append(1)
            l.append(0)

        if i == 'h':
            l.append(0)
            l.append(0)
            l.append(1)
            l.append(1)
            l.append(1)

        if i == 'i':
            l.append(0)
            l.append(1)
            l.append(0)
            l.append(0)
            l.append(0)

        if i == 'j':
            l.append(0)
            l.append(1)
            l.append(0)
            l.append(0)
            l.append(1)

        if i == 'k':
            l.append(0)
            l.append(1)
            l.append(0)
            l.append(1)
            l.append(0)

        if i == 'l':
            l.append(0)
            l.append(1)
            l.append(0)
            l.append(1)
            l.append(1)

        if i == 'm':
            l.append(0)
            l.append(1)
            l.append(1)
            l.append(0)
            l.append(0)

        if i == 'n':
            l.append(0)
            l.append(1)
            l.append(1)
            l.append(0)
            l.append(1)

        if i == 'o':
            l.append(0)
            l.append(1)
            l.append(1)
            l.append(1)
            l.append(0)

        if i == 'p':
            l.append(0)
            l.append(1)
            l.append(1)
            l.append(1)
            l.append(1)

        if i == 'q':
            l.append(1)
            l.append(0)
            l.append(0)
            l.append(0)
            l.append(0)

        if i == 'r':
            l.append(1)
            l.append(0)
            l.append(0)
            l.append(0)
            l.append(1)

        if i == 's':
            l.append(1)
            l.append(0)
            l.append(0)
            l.append(1)
            l.append(0)

        if i == 't':
            l.append(1)
            l.append(0)
            l.append(0)
            l.append(1)
            l.append(1)

        if i == 'u':
            l.append(1)
            l.append(0)
            l.append(1)
            l.append(0)
            l.append(0)

        if i == 'v':
            l.append(1)
            l.append(0)
            l.append(1)
            l.append(0)
            l.append(1)

        if i == 'w':
            l.append(1)
            l.append(0)
            l.append(1)
            l.append(1)
            l.append(1)

        if i == 'x':
            l.append(1)
            l.append(1)
            l.append(0)
            l.append(0)
            l.append(0)

        if i == 'y':
            l.append(1)
            l.append(1)
            l.append(0)
            l.append(0)
            l.append(1)

        if i == 'z':
            l.append(1)
            l.append(1)
            l.append(0)
            l.append(1)
            l.append(0)

        if (l[0] + l[1] + l[2] )%2 != 0:
            l.append(1)
        else:
            l.append(0)

        if (l[1] + l[2] + l[3])%2 != 0:
            l.append(1)
        else:
            l.append(0)

        if (l[2] + l[3] + l[4])%2 != 0:
            l.append(1)
        else:
            l.append(0)

        if (l[1] + l[2] + l[4])%2 != 0:
            l.append(1)
        else:
            l.append(0)


        codigo.append(l)
        l = []


        file2 = open("Paridad/paridad"+str(p)+".txt", "a+")
        file2.write(str(codigo))
        file2.close()



    min= 999;
    for i in codigo:
        aux= 0
        for j in i:
            aux += j

        if (aux <= min):
            if aux !=0:
                min = aux

    file2 = open("Paridad/paridad"+str(p)+".txt", "a+")
    file2.write("\n")
    file2.write(str(min))
    file2.close()
    p+=1
