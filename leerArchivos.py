import time
import string
import test

l2=[]
aux = 1
while(aux <= 30):
    time.sleep(0.1)
    start_time = time.time()
    l=[]
    file = open("ArchivosCP/archivo"+str(aux)+".txt", "r")
    x = ""
    for i in file:
        x += i;
    compressed = test.compress(x)
    l.append (compressed)
    decompressed = test.decompress(compressed)
    l.append (decompressed)
    aux += 1
    l.append("--- %s seconds ---" % (time.time() - start_time))
    l2.append(l)
f = open("/Github/Comunicaciones/ResultadosTestCP.txt", "w")
for i in l2:
    print(i)
    for e in i:
        f.write(str(e))
    f.write("\n")
f.close()
#-------------------------------------------
l2=[]
aux = 1
while(aux <= 30):
    time.sleep(5)
    start_time = time.time()
    l=[]
    file = open("ArchivosSP/archivo"+str(aux)+".txt", "r")
    x = ""
    for i in file:
        x += i;
    compressed = test.compress(x)
    l.append (compressed)
    decompressed = test.decompress(compressed)
    l.append (decompressed)
    aux += 1
    l.append("--- %s seconds ---" % (time.time() - start_time))
    l2.append(l)
f = open("/Github/Comunicaciones/ResultadosTestSP.txt", "w")
for i in l2:
    print(i)
    for e in i:
        f.write(str(e))
    f.write("\n")
f.close()
