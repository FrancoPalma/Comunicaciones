from PIL import Image
import time
import sys
from PIL import ImageChops
import random
import string
import os
p=1
file = open("/Github/Comunicaciones/Imagenes/jpg/datos_img"+str(p)+".txt", "w")
for i in range(30):
    time.sleep(0.1)
    start_time = time.time()
    #Esto abre la imagen
    img = Image.open("\GitHub\Comunicaciones\Imagenes\Bmp\img"+str(p)+".bmp")
    #Esto la convierte a otro formato png, jpeg, tiff
    img.save("\GitHub\Comunicaciones\Imagenes\jpg\img"+str(p)+".jpeg","jpeg")
    file.write ("El tamaño de la imagen "+str(p)+" es de:"+str(os.stat("img"+str(p)+".bmp").st_size)+"\n")
    file.write("La imagen "+str(p)+" se demoro: %s" %(time.time() - start_time)+"\n\n")
    file.write("")
    p+=1
file.close()
