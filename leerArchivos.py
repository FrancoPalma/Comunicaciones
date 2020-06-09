import time
import string
import test
import math

l2=[]
aux = 1
while(aux <= 30):
    start_time = time.time()
    time.sleep(0.1)
    l=[]
    file = open("ArchivosCP/archivo"+str(aux)+".txt", "r")
    x = ""
    for i in file:
        x += i;
    compressed = test.compress(x)
    l.append (compressed)

    bits = 0;       #total de bits
    for i in compressed:
        bits_simbolo = math.log2(i);
        if(bits_simbolo%1 != 0):
            bits_simbolo = bits_simbolo // 1;
            bits_simbolo +=1;
            bits += bits_simbolo;
        else:
            bits += bits_simbolo
    l.append(bits);

    decompressed = test.decompress(compressed)
    l.append (decompressed)
    aux += 1
    l.append("--- %s seconds ---" % ((time.time() - start_time)-0.1))
    l2.append(l)
#f = open("/Github/Comunicaciones/ResultadosTestCP.txt", "w")
f = open("ResultadosTestCP.txt", "w")
for i in l2:
    for e in i:
        f.write(str(e))
    f.write("\n")
f.close()
#-------------------------------------------
l2=[]
aux = 1
while(aux <= 30):
    #time.sleep(5)
    start_time = time.time()
    time.sleep(0.1)
    l=[]
    file = open("ArchivosSP/archivo"+str(aux)+".txt", "r")
    x = ""

    for i in file:
        x += i;
    compressed = test.compress(x)
    l.append (compressed)

    bits = 0;           #total de bits
    for i in compressed:
        bits_simbolo = math.log2(i);
        if(bits_simbolo%1 != 0):
            bits_simbolo = bits_simbolo // 1;
            bits_simbolo +=1;
            bits += bits_simbolo;
        else:
            bits += bits_simbolo
    l.append(bits);

    decompressed = test.decompress(compressed)
    l.append (decompressed)
    aux += 1
    l.append("--- %s seconds ---" % ((time.time() - start_time)-0.1))
    l2.append(l)
f = open("ResultadosTestSP.txt", "w")
for i in l2:
    for e in i:
        f.write(str(e))
    f.write("\n")
f.close()
