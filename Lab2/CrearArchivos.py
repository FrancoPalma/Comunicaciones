import random
import string
for i in range(30):#se crean 30 archivos
    palabra=""
    for e in range(20):#se crea la palabra con 20 letras minusculas
        palabra+=random.choice(string.ascii_lowercase)
    file = open("/Github/Comunicaciones/Lab2/Archivos/Archivo"+str(1+i)+".txt", "w")#se crean los archivos
    file.write(palabra)
    file.close()
