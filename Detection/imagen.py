import numpy as np
import cv2

#Se crea el clasificador con el archivo .xml
object_cascade = cv2.CascadeClassifier('object_cascade.xml')

#lectura de la imagen
img = cv2.imread('imagen.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Se detectan los objetos
objects = object_cascade.detectMultiScale(gray, 5, 5)

#Se dibujan los rectangulos sobre los objetos
for (x,y,w,h) in objects:
    print (x,y,w,h)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),3)

    #segmentacion opcional
    #roi_gray = gray[y:y+h, x:x+w]
    #roi_color = img[y:y+h, x:x+w]

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()