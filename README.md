# OpenCV image and video processing AIB

Proyecto inicial para procesamiento de imagenes, videos y webcam, filtros, recortes y nuevos tamaños
## Dependencias

Este proyecto requiere las siguientes dependencias:

- **OpenCV (cv2)**: Biblioteca de visión por computadora utilizada para trabajar con imágenes y videos.
- **NumPy**: Biblioteca fundamental para computación científica que proporciona soporte para matrices y funciones matemáticas.

Para instalar las dependencias, puedes utilizar pip:

pip install opencv-python numpy


## Uso

Importación de librerias

```python
import cv2
import numpy as np
```
Importación de Imagen
```python
img = cv2.imread("../Resources/img/woman.jpg")
cv2.imshow("Output",img)
cv2.waitKey(0)
```
Importación de WebCam
```python
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,489)
cap.set(10,100)
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

Importación de Video
```python

cap = cv2.VideoCapture("../Resources/Videos/video.mp4")
while True:
    success, img = cap.read()
    if success and img is not None and img.shape[0] > 0 and img.shape[1] > 0:
        cv2.imshow("Video", img)
    #Espera la palabra q para romper el bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

## Contribuyendo
-Alejandro Ibarra

## Créditos
-murtazasworkshop
-Pixabay
