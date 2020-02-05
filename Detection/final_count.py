import RPi.GPIO as GPIO
#from threading import Thread
import multiprocessing
import numpy as np
import time
import cv2

contador_a = 0
contador_b = 0
contador_c = 0
contador_total = 0

def contador_hilo1():

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.IN)

    global contador_a
    global contador_b
    global contador_c

    while  1:
        channel = GPIO.wait_for_edge(11,GPIO.FALLING,timeout=3000)
        if channel is None:
            #print('Timeout')
            if GPIO.input(11)==0:
                print('Translape Carril 1')
                contador_a = contador_a + 1
                print('-----------------------------------')
                print('Cuenta Carril 1:', contador_a)
                print('Cuenta Carril 2:', contador_b)
                print('Cuenta Carril 3:', contador_c)
                contador_total = contador_a + contador_b + contador_c
                print('Cuenta Total:',contador_total)
                print('-----------------------------------')
        else:
            contador_a = contador_a + 1
            print('-----------------------------------')
            print('Cuenta Carril 1:', contador_a)
            print('Cuenta Carril 2:', contador_b)
            print('Cuenta Carril 3:', contador_c)
            contador_total = contador_a + contador_b + contador_c
            print('Cuenta Total:',contador_total)
            print('-----------------------------------')
            time.sleep(0.5)
        k = cv2.waitKey(10) & 0xff
        if k == ord('q'):
            break

def contador_hilo2():
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.IN)

    global contador_a
    global contador_b
    global contador_c

    while  1:
        channel2 = GPIO.wait_for_edge(12,GPIO.RISING,timeout=3000)
        if channel2 is None:
            #print('Timeout')
            if GPIO.input(12):
                print('Translape Carril 2')
                contador_b = contador_b + 1
                print('-----------------------------------')
                print('Cuenta Carril 1:', contador_a)
                print('Cuenta Carril 2:', contador_b)
                print('Cuenta Carril 3:', contador_c)
                contador_total = contador_a + contador_b + contador_c
                print('Cuenta Total:',contador_total)
                print('-----------------------------------')
        else:
            contador_b = contador_b + 1
            print('-----------------------------------')
            print('Cuenta Carril 1:', contador_a)
            print('Cuenta Carril 2:', contador_b)
            print('Cuenta Carril 3:', contador_c)
            contador_total = contador_a + contador_b + contador_c
            print('Cuenta Total:',contador_total)
            print('-----------------------------------')
            time.sleep(0.5)
        k = cv2.waitKey(10) & 0xff
        if k == ord('q'):
            break

def contador_hilo3():
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13,GPIO.IN)

    global contador_a
    global contador_b
    global contador_c

    while  1:
        channel3 = GPIO.wait_for_edge(13,GPIO.RISING,timeout=3000)
        if channel3 is None:
            #print('Timeout')
            if GPIO.input(13):
                print('Translape Carril 3')
                contador_c = contador_c + 1
                print('-----------------------------------')
                print('Cuenta Carril 1:', contador_a)
                print('Cuenta Carril 2:', contador_b)
                print('Cuenta Carril 3:', contador_c)
                contador_total = contador_a + contador_b + contador_c
                print('Cuenta Total:',contador_total)
                print('-----------------------------------')
        else:
            contador_c = contador_c + 1
            print('-----------------------------------')
            print('Cuenta Carril 1:', contador_a)
            print('Cuenta Carril 2:', contador_b)
            print('Cuenta Carril 3:', contador_c)
            contador_total = contador_a + contador_b + contador_c
            print('Cuenta Total:',contador_total)
            print('-----------------------------------')
            time.sleep(0.5)
        k = cv2.waitKey(10) & 0xff
        if k == ord('q'):
            break

def video_hilo():
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
        if k == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

hilo1 = multiprocessing.Process(target=contador_hilo1)
hilo2 = multiprocessing.Process(target=contador_hilo2)
hilo3 = multiprocessing.Process(target=contador_hilo3)
hilo4 = multiprocessing.Process(target=video_hilo)

hilo1.start()
hilo2.start()
hilo3.start()
hilo4.start()

