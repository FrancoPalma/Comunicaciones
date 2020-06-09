import time
import string
import test
import math

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

    bits = 0;           #total de bits
    for i in compressed:
        bits_simbolo = math.log2(i);
        if(bits_simbolo%1 != 0):
            bits_simbolo = bits_simbolo // 1;
            bits_simbolo +=1;
            bits += bits_simbolo;
        else:
            bits += bits_simbolo
    f.write("El peso en bites es: "+str(bits)+".\n")

    decompressed = test.decompress(compressed)
    f.write("Descomprimido es: "+str(decompressed)+".\n")
    aux += 1
    f.write(" %s seconds" % ((time.time() - start_time)-0.1))
    f.write("\n\n")
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

    bits = 0;           #total de bits
    for i in compressed:
        bits_simbolo = math.log2(i);
        if(bits_simbolo%1 != 0):
            bits_simbolo = bits_simbolo // 1;
            bits_simbolo +=1;
            bits += bits_simbolo;
        else:
            bits += bits_simbolo
    f.write("El peso en bites es: "+str(bits)+".\n")

    decompressed = test.decompress(compressed)
    f.write("Descomprimido es: "+str(decompressed)+".\n")
    aux += 1
    f.write(" %s seconds" % ((time.time() - start_time)-0.1))
    f.write("\n\n")
f.close()
