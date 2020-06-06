import random
import string
from random import randrange
p=1
for i in range(30):
    palabra=""
    n=randrange(3)+3
    letras=""
    for i in range(n):
        letras+=random.choice(string.ascii_lowercase)
    while len(palabra) < 20:
        if (len(palabra)+len(letras)) <= 20:
            palabra+=letras
        if len(palabra)<20:
            palabra+=random.choice(string.ascii_lowercase)
    file = open("/Github/Comunicaciones/ArchivosConPatron/archivo_con_patron"+str(p)+".txt", "w")
    file.write(palabra)
    file.close()
    p+=1
