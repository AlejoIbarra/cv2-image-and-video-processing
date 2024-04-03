import cv2
import numpy as np


#ruta de la imagen
img=cv2.imread('../Resources/img/woman.jpg')


#todos los valores sean 1 significa ones
#matriz de 5*5 y el uint8 significa que los valores varian de 0 a 255
kernel=np.ones((5,5),np.uint8)

#Escala de grises
#primero se debe definir que se va a convertir,
#luego se define a que espacio de color se convertira
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#desenfoque// se usa desenfoque gausiano y se define el tamaño del nucleo o el radio
#el desenfoque deben ser numero impares
#sigma x sera 0
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)

# se usara img canny // puede servir para detectar los puntos negros de barros
#varian los valores entre 100 y 50 para variar los detalles a obtener
imgCanny=cv2.Canny(img,100,150)

#Dilatación
imDilation = cv2.dilate(imgCanny,kernel,iterations= 1)

#eroción, es lo contrario de la dilatación
imgEroded=cv2.erode(imDilation,kernel,iterations= 1)

cv2.imshow('Gray Image',imgGray)
cv2.imshow('Blur Image',imgBlur)
cv2.imshow('Canny Image',imgCanny)
cv2.imshow('Dilation Image',imDilation)
cv2.imshow('Eroded Image',imgEroded)



cv2.waitKey(0)