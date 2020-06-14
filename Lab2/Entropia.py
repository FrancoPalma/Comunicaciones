p=1
l=[]
file2 = open("Entropia/Entropia"+str(p)+".txt", "w")
for i in range(30):
    verificador=True
    file = open("Archivos/Archivo"+str(p)+".txt", "r")
    file2.write("-----Entropa Archivo"+str(p)+"-----")
    texto = ""
    aux=""
    for i in file:
        texto += i;
    file.close()
    for i in texto:
    file2.write(aux)
    p+=1
file2.close()
