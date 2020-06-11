from PIL import Image
import time
import sys
from PIL import ImageChops
import random
import string
import os
p=1
file = open("/Github/Comunicaciones/Imagenes/datos_img"+str(p)+"_jpg.txt", "w")
promediobmp=0
promediojpg=0
promediopng=0
promediogif=0
promediosegjpg=0
promediosegpng=0
promedioseggif=0
tiempo=0
for i in range(30):
    start_time = time.time()
    #Esto abre la imagen
    img = Image.open("\GitHub\Comunicaciones\Imagenes\img"+str(p)+".bmp")
    #Esto la convierte a otro formato png, jpeg, tiff
    img.save("\GitHub\Comunicaciones\Imagenes\img"+str(p)+".jpeg","jpeg")
    tiempo=time.time() - start_time
    file.write ("El tamaño de la imagen BMP "+str(p)+" es de:"+str(os.stat("img"+str(p)+".bmp").st_size)+" bytes.\n")
    promediobmp+=os.stat("img"+str(p)+".bmp").st_size
    file.write ("El tamaño de la imagen JPG "+str(p)+" es de:"+str(os.stat("img"+str(p)+".jpeg").st_size)+" bytes.\n")
    promediojpg+=os.stat("img"+str(p)+".jpeg").st_size
    file.write("La diferencia es de: "+str(os.stat("img"+str(p)+".bmp").st_size-os.stat("img"+str(p)+".jpeg").st_size)+" bytes.\n")
    file.write("La imagen "+str(p)+" se demoro: %s en comprimirse" %tiempo)
    file.write(".\n\n")
    promediosegjpg+=tiempo
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
    tiempo=time.time() - start_time
    file.write ("El tamaño de la imagen BMP "+str(p)+" es de:"+str(os.stat("img"+str(p)+".bmp").st_size)+" bytes.\n")
    file.write ("El tamaño de la imagen PNG "+str(p)+" es de:"+str(os.stat("img"+str(p)+".png").st_size)+" bytes.\n")
    promediopng+=os.stat("img"+str(p)+".png").st_size
    file.write("La diferencia es de: "+str(os.stat("img"+str(p)+".bmp").st_size-os.stat("img"+str(p)+".png").st_size)+" bytes.\n")
    file.write("La imagen "+str(p)+" se demoro: %s en comprimirse" %tiempo)
    file.write(".\n\n")
    promediosegpng+=tiempo
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
    tiempo=time.time() - start_time
    file.write ("El tamaño de la imagen BMP "+str(p)+" es de:"+str(os.stat("img"+str(p)+".bmp").st_size)+" bytes.\n")
    file.write ("El tamaño de la imagen GIF "+str(p)+" es de:"+str(os.stat("img"+str(p)+".gif").st_size)+" bytes.\n")
    promediogif=os.stat("img"+str(p)+".gif").st_size
    file.write("La diferencia es de: "+str(os.stat("img"+str(p)+".bmp").st_size-os.stat("img"+str(p)+".gif").st_size)+" bytes.\n")
    file.write("La imagen "+str(p)+" se demoro: %s en comprimirse" %tiempo)
    file.write(".\n\n")
    promediosegpng+=tiempo
    p+=1
file.close()
file = open("/Github/Comunicaciones/Imagenes/promediodatos.txt", "w")
file.write("Promedio bytes BMP: %s.\n\n"%(promediobmp/30))

file.write("Promedio bytes JPG: %s.\n"%(promediojpg/30))
file.write("Promedio bytes de diferencia entre JPG y BMP: %s.\n"%(promediobmp/30-promediojpg/30))
file.write("Promedio segundos en transformar BMP a JPG: %s.\n\n"%(promediosegjpg/30))

file.write("Promedio bytes PNG: %s.\n"%(promediopng/30))
file.write("Promedio bytes de diferencia entre PNG y BMP: %s.\n"%(promediobmp/30-promediopng/30))
file.write("Promedio segundos en transformar BMP a PNG: %s.\n\n"%(promediosegpng/30))

file.write("Promedio bytes GIF: %s.\n"%(promediogif/30))
file.write("Promedio bytes de diferencia entre GIF y BMP: %s.\n"%(promediobmp/30-promediogif/30))
file.write("Promedio segundos en transformar BMP a GIF: %s.\n\n"%(promedioseggif/30))
file.close()
print("Fin.")
