import cv2
import numpy as np

img=cv2.imread('../resources/img/woman.jpg')

#primero sera horizontal, sirve para agregar otra imagen, horizontalmente
imgHor =np.hstack((img,img))

#Se apilara ahora de forma vertical

imgVer = np.vstack((img,img))

#Para poder lograr esto las dos imagenes deberan de tener el mismo canal, y otro problema es que
#no se podran reajustar el tamaño, pero hay una solucion para esto
cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVer)
cv2.waitKey()