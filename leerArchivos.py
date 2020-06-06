import time
import string
import test
<<<<<<< HEAD
import huffman

start_time = time.time()

aux = 1
while(aux <= 30):
    file = open("Archivos_sin_patron/archivo"+str(aux)+".txt", "r")
=======
l2=[]
aux = 1
while(aux <= 30):
    start_time = time.time()
    l=[]
    file = open("ArchivosCP/archivo"+str(aux)+".txt", "r")
>>>>>>> 76ac47a2c55286e15a0cf2f259b5991ac8573bb3
    x = ""
    for i in file:
        x += i;

    compressed = test.compress(x)
    l.append (compressed)
    decompressed = test.decompress(compressed)
<<<<<<< HEAD
    print (decompressed)
    huffman.funcion(x)
=======
    l.append (decompressed)
>>>>>>> 76ac47a2c55286e15a0cf2f259b5991ac8573bb3
    aux += 1
    l.append("--- %s seconds ---" % (time.time() - start_time))
    l2.append(l)
for i in l2:
    print(i)
