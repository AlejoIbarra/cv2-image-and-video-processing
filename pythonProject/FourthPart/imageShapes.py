#dibujar formas en imagenes y como poner texto
import cv2
import numpy as np

#se llena una matriz llena de 0 ahora el numero 0 es negro

#si se deja de la siguiente manera solo sera una escala de grises
#img =np.zeros((512,512))
#por el contrario si le colocamos la funcionalidad de color debemos de agregarle los canales


img=np.zeros((500,500,3))

#para colorear la imagen completa de azul
# y asi podremos agregar valores entre 0 y 255, en pocas palabras lo siguiente crea un cuadrado
#img[200:300,200:300]=[0,0,255]

#crear lineas, se debe definir punto de partida y punto final
# se define, punto inicial, punto final, color y grosor
#cv2.line(img,(0,0),(250,250),(255,0,0),4)

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0),2)
#a continuación se realizara un rectangulo
# se puede poner el grosor o se puede llenar el rectangulo completamente
#cv2.rectangle(img,(0,0),(250,350),(0,255,0),cv2.FILLED)
cv2.rectangle(img,(0,0),(250,350),(0,255,0),2)

#circulos
cv2.circle(img,(250,250),100,(255,0,0),5)

#texto
cv2.putText(img,'Hello World',(150,150),cv2.FONT_HERSHEY_SIMPLEX,1,(100,0,250),2)



#al imprimir, ya no nos saldra el canal por lo que es una escala de grises
print(img.shape)

cv2.imshow("Image",img)

cv2.waitKey(0)
