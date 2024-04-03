import cv2
import numpy as np

#import video and define the route
cap = cv2.VideoCapture("../Resources/Videos/video.mp4")

kernel=np.ones((5,5),np.uint8)


#el id del brillo es 10 y para darle 100 de brillo es de la siguiente forma
#cap.set(10,100)
#recordando que un video es una secuencia de imagenes o de frames, por lo que se hace un while
while True:
    success, img = cap.read()
    #se muestra el resultado, img es la variable
    if success and img is not None and img.shape[0] > 0 and img.shape[1] > 0:
        imgCanny = cv2.Canny(img, 200, 150)


        cv2.imshow("Video", imgCanny)

    #Espera la palabra q para romper el bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break