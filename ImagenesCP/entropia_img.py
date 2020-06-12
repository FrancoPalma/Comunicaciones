import numpy as np
from skimage import io, color, img_as_ubyte
from skimage.feature import greycomatrix, greycoprops
from sklearn.metrics.cluster import entropy
from PIL import Image
import time
import sys
from PIL import ImageChops
import random
import string
import os

p=1
file = open("entropia_img"+str(p)+"_jpg.txt", "w")
file2 = open("entropia_img"+str(p)+"_bmp.txt", "w")
promediobmp=0
promediojpg=0
promediopng=0
promediogif=0
promediosegjpg=0
promediosegpng=0
promedioseggif=0
tiempo=0


for i in range(30):


    img_aux = io.imread('imgcp_'+str(p)+'.bmp')
    entropia = entropy(img_aux)
    file2.write("La entropia de la imagen BMP ")
    file2.write(str(p))
    file2.write(" es de: ")
    file2.write(str(entropia))
    file2.write("\n")


    img_aux = io.imread('imgcp_'+str(p)+'.jpeg')
    entropia = entropy(img_aux)
    file.write("La entropia de la imagen JPEG ")
    file.write(str(p))
    file.write(" es de: ")
    file.write(str(entropia))
    file.write("\n")


    p+=1
file.close()
file2.close()

p=1
file = open("entropia_img"+str(p)+"_png.txt", "w")
for i in range(30):


    img_aux = io.imread('imgcp_'+str(p)+'.png')
    entropia = entropy(img_aux)
    file.write("La entropia de la imagen PNG ")
    file.write(str(p))
    file.write(" es de: ")
    file.write(str(entropia))
    file.write("\n")



    p+=1
file.close()

p=1
file = open("entropia_img"+str(p)+"_gif.txt", "w")
for i in range(30):


    img_aux = io.imread('imgcp_'+str(p)+'.gif')
    entropia = entropy(img_aux)
    file.write("La entropia de la imagen GIF ")
    file.write(str(p))
    file.write(" es de: ")
    file.write(str(entropia))
    file.write("\n")


    p+=1
file.close()


print("Fin.")
