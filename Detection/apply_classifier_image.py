import numpy as np
import cv2

#Se crea el clasificador con el archivo .xml
object_cascade = cv2.CascadeClassifier('object_cascade.xml')

#Captura una imagen
cap = cv2.VideoCapture(0)

while 1:
    #Se extrae la imagen
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       
    #Se detectan los objetos
    objects = object_cascade.detectMultiScale(gray, 50, 50)
    
    #Se dibujan los rectangulos sobre los objetos
    for (x,y,w,h) in objects:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()