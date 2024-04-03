import cv2

#import video and define the route if the route is 0 the application activace camera
cap = cv2.VideoCapture(0)
#ancho es el id numero 3
cap.set(3,640)
#alto es el id numero 4
cap.set(4,489)
#el id del brillo es 10 y para darle 100 de brillo es de la siguiente forma
cap.set(10,100)
#recordando que un video es una secuencia de imagenes o de frames, por lo que se hace un while
while True:
    success, img = cap.read()
    #se muestra el resultado, img es la variable
    cv2.imshow("Video", img)
    #Espera la palabra q para romper el bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break