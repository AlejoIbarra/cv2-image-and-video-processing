import cv2
import numpy as np

#en este ejercicio lo que se obtendra sera una imagen plana
#en especifico de una carta
img = cv2.imread("../Resources/img/cards.jpg")

#de define width,height

width,height=250,350

#declaramos 4 diferentes puntos
#  se inicia desde la esquina superior izquienda, luego con la superior derecha y finaliza con
#inferior izquierda e inferior derecha
pts1=np.float32([[335,130],[453,175],[264,283],[395,280]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])

# hay que definir todos loos 4 puntos

matrix=cv2.getPerspectiveTransform(pts1,pts2)

imgOutPut=cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Original",img)
cv2.imshow("Wrapped",imgOutPut)

cv2.waitKey(0)
