from PIL import Image
import time
import sys
from PIL import ImageChops
import random
import string
import os
p=1

for i in range(29):
    time.sleep(0.1)
    start_time = time.time()
    #Esto abre la imagen
    img = Image.open("\GitHub\Comunicaciones\Imagenes\Bmp\img"+str(p)+".bmp")
    #Esto la convierte a otro formato png, jpeg, tiff
    img.save("\GitHub\Comunicaciones\Imagenes\jpg\img"+str(p)+".jpeg","jpeg")
    file = open("/Github/Comunicaciones/Imagenes/jpg/datos_img"+str(p)+".txt", "w")
    file.write (os.stat(img).st_size)
    file.write("La imagen "+str(p)+" se demoro: %s" %(time.time() - start_time))
    file.close()
    p+=1
