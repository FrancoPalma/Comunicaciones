from PIL import Image
import sys
import ImageChops
try:
    img = Image.open("descarga.jpg")
    img2 = Image.open("paisaje.png")
except:
    print("No se pudo cargar la imagen")
    sys.exit(1)
#img.show()
#Conversión de JPG a PNG
#img.save("paisaje.gif","gif")
#Rotación de imágenes
#img2 = img.rotate(45)
#img2.show()
#Encontrar ancho y alto de una imagen
ancho,alto = img.size
print("Ancho: ",ancho)
print("Alto: ",alto)
diff = ImageChops.difference(img,img2)
print(diff)
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
