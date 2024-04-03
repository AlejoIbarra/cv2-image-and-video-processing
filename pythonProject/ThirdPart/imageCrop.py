import cv2

img = cv2.imread("../Resources/img/woman.jpg")
# se imprime el tamaño, donde (y,x,numeroCanales)
print(img.shape)

#se define el ancho y alto que tendra, primero se define el ancho luego el alto
imgResize=cv2.resize(img,(200,400))
print(imgResize.shape)

#recortar imagen
#primero la altura y luego el ancho
# se definen los rangos que quedaran
imgCropped=img[100:350,200:640]

cv2.imshow("Original", img)
cv2.imshow("Resized", imgResize)
cv2.imshow("Cropped", imgCropped)
#print(imgCropped.shape)
cv2.waitKey(0)