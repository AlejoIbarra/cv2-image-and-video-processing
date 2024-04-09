import cv2
import numpy as np

#reutilizamos la función de partes anteriores, en este caso la 6
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img):
    #recupera los contornos exteriores externos, hay otras alternativas, pero esta es realmente buena cob cv2.RETR_EXTERNAL
    #luego se solicita los valores comprimidos, para reducir los puntos
    countours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    #recorremos los contornos
    for cnt in countours:
        area=cv2.contourArea(cnt)
        #ahora vamos a imprimir ese contorno
        #escanea las imagenes y muestra las areas que encuentra para cada una de las formas
        print(area)

        #se pone un umbral para que no detecte el ruido
        if area >500:
            # se las dibuja para verlas claramente
            cv2.drawContours(imgContour, cnt, -1, (0, 255, 0), 3)
            #ahora lo que se hara es calcular la longitud de la curva, por que la longitud de las curvas
            #nos ayudan a aproximar las esquinas de nuestras formas
            #true significa que esta cerrado
            peri=cv2.arcLength(cnt, True)
            #print(peri)
            approx =cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            #vamos a crear las esquinas del objeto
            objCor =len(approx)
            #se crea un cuadro delimitador al objeto detectado, por lo que se obtiene el cuadro delimitador
            #se crea este cuadro delimitador al rededor del objeto y serán X&Y y el ancho y el alto
            x,y,w,h=cv2.boundingRect(approx)

            #ahora lo que haremos sera clasificarlos
            if objCor ==3:ObjectType="Tri"
            else:ObjectType="other"

            #ahora vamos a dibujarlos para obtener una imagen clara
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.putText(imgContour,ObjectType,(x+(w//2),y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX,
                        0.5,(0,0,0),1)




# en este ejercicio, se van a detectar formas en una imagen, en pocas palabras se detectara
#contornos, puntos de las esquina y en base a ello definir la forma de este objeto
path = '../Resources/img/shapes.png'
img=cv2.imread(path)

#se crea otra imagen para analizarla con los contornos, se hara una copia
imgContour=img.copy()

#Primero preprocesamos nuestra imagen, en pocas palabras la convertimos en escala de grises

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(7,7),1)
#se llama img canny y se aplica a imgBlur, despues se aplica el umbral50,50
imgCanny=cv2.Canny(imgBlur,50,50)

getContours(imgCanny)

imgBlank = np.zeros_like(img)

imgStack = stackImages(0.6,([img,imgGray,imgBlur],[imgCanny,imgContour,imgBlank]))

#cv2.imshow("stack",imgStack)
#cv2.imshow('Original Image',img)
#cv2.imshow('imgGray',imgGray)
#cv2.imshow('blur Image',imgBlur)

cv2.imshow('stackImages',imgStack)
cv2.waitKey(0)

