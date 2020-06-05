import random
import string
for i in range(30):
    palabra=""
    for i in range(20):
        palabra+=random.choice(string.ascii_lowercase)
    file = open("D:/Github/archivo"+p+".txt", "w")
    file.write(palabra)
    file.close()
