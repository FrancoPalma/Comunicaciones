from PIL import Image
import time
import sys
from PIL import ImageChops
import random
import string
import os
p=1
file = open("/Github/Comunicaciones/Imagenes/datos_img"+str(p)+"_jpg.txt", "w")
for i in range(30):
    start_time = time.time()
    #Esto abre la imagen
    img = Image.open("\GitHub\Comunicaciones\Imagenes\img"+str(p)+".bmp")
    #Esto la convierte a otro formato png, jpeg, tiff
    img.save("\GitHub\Comunicaciones\Imagenes\img"+str(p)+".jpeg","jpeg")
    file.write ("El tamaño de la imagen BMP "+str(p)+" es de:"+str(os.stat("img"+str(p)+".bmp").st_size)+"\n")
    file.write ("El tamaño de la imagen JPG "+str(p)+" es de:"+str(os.stat("img"+str(p)+".jpeg").st_size)+"\n")
    file.write("La diferencia es de: "+str(os.stat("img"+str(p)+".bmp").st_size-os.stat("img"+str(p)+".jpeg").st_size)+"\n")
    file.write("La imagen "+str(p)+" se demoro: %s en comprimirse" %(time.time() - start_time)+"\n\n")
    p+=1
file.close()

p=1
file = open("/Github/Comunicaciones/Imagenes/datos_img"+str(p)+"_png.txt", "w")
for i in range(30):
    start_time = time.time()
    #Esto abre la imagen
    img = Image.open("\GitHub\Comunicaciones\Imagenes\img"+str(p)+".bmp")
    #Esto la convierte a otro formato png, jpeg, tiff
    img.save("\GitHub\Comunicaciones\Imagenes\img"+str(p)+".png","png")
    file.write ("El tamaño de la imagen BMP "+str(p)+" es de:"+str(os.stat("img"+str(p)+".bmp").st_size)+"\n")
    file.write ("El tamaño de la imagen PNG "+str(p)+" es de:"+str(os.stat("img"+str(p)+".png").st_size)+"\n")
    file.write("La diferencia es de: "+str(os.stat("img"+str(p)+".bmp").st_size-os.stat("img"+str(p)+".png").st_size)+"\n")
    file.write("La imagen "+str(p)+" se demoro: %s en comprimirse" %(time.time() - start_time)+"\n\n")
    p+=1
file.close()

p=1
file = open("/Github/Comunicaciones/Imagenes/datos_img"+str(p)+"_gif.txt", "w")
for i in range(30):
    start_time = time.time()
    #Esto abre la imagen
    img = Image.open("\GitHub\Comunicaciones\Imagenes\img"+str(p)+".bmp")
    #Esto la convierte a otro formato png, jpeg, tiff
    img.save("\GitHub\Comunicaciones\Imagenes\img"+str(p)+".gif","gif")
    file.write ("El tamaño de la imagen BMP "+str(p)+" es de:"+str(os.stat("img"+str(p)+".bmp").st_size)+"\n")
    file.write ("El tamaño de la imagen GIF "+str(p)+" es de:"+str(os.stat("img"+str(p)+".gif").st_size)+"\n")
    file.write("La diferencia es de: "+str(os.stat("img"+str(p)+".bmp").st_size-os.stat("img"+str(p)+".gif").st_size)+"\n")
    file.write("La imagen "+str(p)+" se demoro: %s en comprimirse" %(time.time() - start_time)+"\n\n")
    p+=1
file.close()
print("Fin.")
