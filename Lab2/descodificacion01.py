p=1
for i in range(30):
    file = open("CodCE01/CodigoCE"+str(p)+".txt", "r")
    texto = ""
    aux=""
    for i in file:
        texto += i;
    file.close()
    file2 = open("Descodificados/Error01/Descodificado"+str(p)+".txt", "w")
    for i in texto:
        aux+=i
        if len(aux) == 9:
            file2.write(chr(int(aux,2)))
            aux=""
    file2.close()
    p+=1
