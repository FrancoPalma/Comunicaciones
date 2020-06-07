from PIL import Image
import sys
from PIL import ImageChops
try:
    img = Image.open("\GitHub\Comunicaciones\Imagenes\jpg\img3.jpg")
    img2 = Image.open("paisaje.tiff")
except:
    print("No se pudo cargar la imagen")
    sys.exit(1)
#img.show()
#Conversión de JPG a PNG
#img.save("paisaje.tiff","tiff")
#Rotación de imágenes
#img2 = img.rotate(45)
#img2.show()
#Encontrar ancho y alto de una imagen
ancho,alto = img.size
print("Ancho: ",ancho)
print("Alto: ",alto)
datos_img = img.getdata()
datos_img2= img2.getdata()
'''
dif = [abs(datos_img[x] - datos_img2[x]) for x in range(len(datos_img))]

img_dif = Image.new('L', img.size)
img_dif.putdata(dif)
img_dif.save('dif')

print(img.histogram)
print(img2.histogram)
'''
diff = ImageChops.difference(img,img2)

if diff.getbbox():
    print("imagenes son distintas")
else:
    print("Imagenes iguales")

#Reescalar imágenes y crear thumbnails
#size = (200,200)
#img3 = img.resize(size)
#img4 = img.copy()
#img4.thumbnail(size)
#img3.show()
#img4.show()
#Averiguar los colores de un pixel
#pixels = img.load()
#clr = pixels[10,10]
#print(clr)
