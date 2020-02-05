from threading import Thread
import time

contador_a = 0
contador_b = 0
contador_c = 0
contador_total = 0

def contar1():
    global contador_a
    while  1:
        time.sleep(4)
        contador_a = contador_a + 1
        print('-----------------------------------')
        print('cuenta 1:',contador_a)
        print('cuenta 2:',contador_b)
        print('cuenta 3:',contador_c)
        contador_total = contador_a + contador_b + contador_c
        print('cuenta total:',contador_total)
        print('-----------------------------------')

def contar2():
    global contador_b
    while  1:
        time.sleep(2)
        contador_b = contador_b + 1
        print('-----------------------------------')
        print('cuenta 1:',contador_a)
        print('cuenta 2:',contador_b)
        print('cuenta 3:',contador_c)
        contador_total = contador_a + contador_b + contador_c
        print('cuenta total:',contador_total)
        print('-----------------------------------')

def contar3():
    global contador_c
    while  1:
        time.sleep(1)
        contador_c = contador_c + 1
        print('-----------------------------------')
        print('cuenta 1:',contador_a)
        print('cuenta 2:',contador_b)
        print('cuenta 3:',contador_c)
        contador_total = contador_a + contador_b + contador_c
        print('cuenta total:',contador_total)
        print('-----------------------------------')

hilo1 = Thread(target=contar1)
hilo2 = Thread(target=contar2)
hilo3 = Thread(target=contar3)

hilo1.start()
hilo2.start()
hilo3.start()