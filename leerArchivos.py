import time
import string
import test
import math

# Build the dictionary.
dict_size = 256
dictionary = dict((chr(i), i) for i in range(dict_size))

aux = 1
f = open("ResultadosTestCP.txt", "w")
while(aux <= 30):
    #time.sleep(5)
    f.write("Archivo"+str(aux)+"\n")
    start_time = time.time()
    time.sleep(0.1)
    l=[]
    file = open("ArchivosCP/archivo"+str(aux)+".txt", "r")
    x = ""

    for i in file:
        x += i;
    compressed = test.compress(x)
    f.write("El archivo comprimido es: "+str(compressed)+"\n")


    decompressed = test.decompress(compressed)
    f.write("Descomprimido es: "+str(decompressed)+".\n")

    num_simbolos = []
    for c in decompressed:
        if c in dictionary:
            num_simbolos.append(dictionary[c])


    f.write(str((time.time()-start_time)-0.01))
    f.write("\n\n")
    aux+=1
f.close()
#-------------------------------------------

aux = 1
f = open("ResultadosTestSP.txt", "w")
while(aux <= 30):
    f.write("Archivo"+str(aux)+"\n")
    #time.sleep(5)
    start_time = time.time()
    time.sleep(0.1)
    l=[]
    file = open("ArchivosSP/archivo"+str(aux)+".txt", "r")
    x = ""

    for i in file:
        x += i;
    compressed = test.compress(x)
    f.write("El archivo comprimido es: "+str(compressed)+"\n")



    decompressed = test.decompress(compressed)
    f.write("Descomprimido es: "+str(decompressed)+".\n")

    num_simbolos = []
    for c in decompressed:
        if c in dictionary:
            num_simbolos.append(dictionary[c])

    """bits = 0;           #total de bits
    for i in num_simbolos:
        bits_simbolo = math.log2(i);
        if(bits_simbolo%1 != 0):
            bits_simbolo = bits_simbolo // 1;
            bits_simbolo +=1;
            bits += bits_simbolo;
        else:
            bits += bits_simbolo"""

    f.write("Cantidad de simbolos de descomprimidos es: "+str(len(num_simbolos))+".\n")
    f.write("\n")
    f.write(str((time.time()-start_time)-0.01))
    f.write("\n\n")
    aux+=1
f.close()
