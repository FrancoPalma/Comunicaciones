import random
import string
p=1
for i in range(30):
    palabra=""
    for i in range(20):
        palabra+=random.choice(string.ascii_lowercase)
    file = open("/Github/Comunicaciones/Archivos/archivo"+str(p)+".txt", "w")
    file.write(palabra)
    file.close()
    p+=1
