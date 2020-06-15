import random
p=1

H = [[1,1,1,0,0,1,0,0,0],
     [0,1,1,1,0,0,1,0,0],
     [0,0,1,1,1,0,0,1,0],
     [1,0,1,0,1,0,0,0,1]]

l =[]
tabla_sindrome = []
l.append(0)
l.append(0)
l.append(0)
l.append(0)
tabla_sindrome.append(l)

cont = 1
l =[]
for cont in range(9):
    l.append(H[0][cont])
    l.append(H[1][cont])
    l.append(H[2][cont])
    l.append(H[3][cont])
    tabla_sindrome.append(l)
    l = []
    cont +=1


for i in range(30):
    file = open("Archivos/Archivo"+str(p)+".txt", "r")
    texto = ""
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

        if (l[0] + l[2] + l[4])%2 != 0:
            l.append(1)
        else:
            l.append(0)


        codigo.append(l)
        l = []

    min= 999;
    for i in codigo:
        aux= 0
        for j in i:
            aux += j

        if (aux <= min):
            if aux !=0:
                min = aux


    file2 = open("Paridad/Paridad"+str(p)+".txt", "a+")
    file2.write(str(codigo))
    file2.write("\n")
    file2.write(str(min))
    file2.write("\n")
    file2.write("\n")
    file2.close()

    Ferror = []
    Serror = []
    Terror = []

    l2 = []
    for i in codigo:
        for j in i:
            if random.random() <= 0.1:
                if j == 0:
                    l2.append(1)
                else:
                    l2.append(0)
            else:
                l2.append(j)

        Ferror.append(l2)
        l2 = []

    l2 = []
    sindrome = []

    for i in Ferror:
        fila = 0
        while fila < 4:
            suma = 0
            columna = 0
            while columna < 9:
                suma += i[columna]*H[fila][columna]
                columna += 1
            if(suma % 2 == 0):
                suma = 0
            else:
                suma = 1
            l2.append(suma)
            fila += 1
        sindrome.append(l2)
        l2 = []

    file2 = open("Paridad/Paridad"+str(p)+".txt", "a+")
    file2.write("ERROR 0.1")
    file2.write("\n")
    file2.write(str(Ferror))
    file2.write("\n")
    file2.write("\n")
    file2.write("SINDROMES 0.1")
    file2.write("\n")
    file2.write(str(sindrome))
    file2.write("\n")
    file2.write("\n")
    file2.close()

    l2 = []
    for i in codigo:
        for j in i:
            if random.random() <= 0.01:
                if j == 0:
                    l2.append(1)
                else:
                    l2.append(0)
            else:
                l2.append(j)

        Serror.append(l2)
        l2 = []

    l2 = []
    sindrome = []

    for i in Serror:
        fila = 0
        while fila < 4:
            suma = 0
            columna = 0
            while columna < 9:
                suma += i[columna]*H[fila][columna]
                columna += 1
            if(suma % 2 == 0):
                suma = 0
            else:
                suma = 1
            l2.append(suma)
            fila += 1
        sindrome.append(l2)
        l2 = []




    file2 = open("Paridad/Paridad"+str(p)+".txt", "a+")
    file2.write("ERROR 0.01")
    file2.write("\n")
    file2.write(str(Serror))
    file2.write("\n")
    file2.write("\n")
    file2.write("SINDROMES")
    file2.write("\n")
    file2.write(str(sindrome))
    file2.write("\n")
    file2.write("\n")
    file2.close()

    l2 = []
    for i in codigo:
        for j in i:
            if random.random() <= 0.001:
                if j == 0:
                    l2.append(1)
                else:
                    l2.append(0)
            else:
                l2.append(j)

        Terror.append(l2)
        l2 = []

    l2 = []
    sindrome = []

    for i in Terror:
        fila = 0
        while fila < 4:
            suma = 0
            columna = 0
            while columna < 9:
                suma += i[columna]*H[fila][columna]
                columna += 1
            if(suma % 2 == 0):
                suma = 0
            else:
                suma = 1
            l2.append(suma)
            fila += 1
        sindrome.append(l2)
        l2 = []

    file2 = open("Paridad/Paridad"+str(p)+".txt", "a+")
    file2.write("ERROR 0.001")
    file2.write("\n")
    file2.write(str(Terror))
    file2.write("\n")
    file2.write("\n")
    file2.write("SINDROMES")
    file2.write("\n")
    file2.write(str(sindrome))
    file2.write("\n")
    file2.write("\n")
    file2.close()

    p+=1

file2 = open("Paridad/tabla_sindrome.txt", "w")
file2.write("\n")
file2.write(str(tabla_sindrome))
file2.close()
