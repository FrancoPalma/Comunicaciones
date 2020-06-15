p=1
for i in range(30):
    file = open("Codigos/Codigo"+str(p)+".txt", "r")
    texto = ""
    aux=""
    bina=""
    Verificador=True
    for i in file:
        texto += i;
    file.close()
    file2 = open("Descodificados/SinError/Descodificado"+str(p)+".txt", "w")
    for i in texto:
        aux+=i
        if len(aux) == 9:
            if ((int(aux[0])+int(aux[1])+int(aux[2]))%2) == aux[5]:
                Verificador=False
            if ((int(aux[1])+int(aux[2])+int(aux[3]))%2) == aux[6]:
                Verificador=False
            if ((int(aux[2])+int(aux[3])+int(aux[4]))%2) == aux[7]:
                Verificador=False
            if ((int(aux[0])+int(aux[2])+int(aux[4]))%2) == aux[8]:
                Verificador=False
            bina='011'
            for i in range(5):
                bina+=aux[i]
            file2.write(chr(int(bina,2)+1))
            aux=""
    if Verificador:
        file2.write("\nNo hay error.")
    else:
        file2.write("\nSe detecto un error.")
    file2.close()
    p+=1
