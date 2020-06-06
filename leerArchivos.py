import time
import string
import test

start_time = time.time()

aux = 1
while(aux <= 30):
    file = open("Archivos/archivo"+str(aux)+".txt", "r")
    x = ""
    for i in file:
        x += i;

    compressed = test.compress(x)
    print (compressed)
    decompressed = test.decompress(compressed)
    print (decompressed)
    aux += 1


print("--- %s seconds ---" % (time.time() - start_time))
