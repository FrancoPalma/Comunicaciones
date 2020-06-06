import random
import string
p=1
for i in range(30):
    palabra=""
    for i in range(4):
        palabra+=random.choice(string.ascii_lowercase)
    palabra=palabra+palabra+palabra+palabra+palabra
    file = open("/Github/Comunicaciones/ArchivosCP/archivo"+str(p)+".txt", "w")
    file.write(palabra)
    file.close()
    p+=1
