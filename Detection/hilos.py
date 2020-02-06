from threading import Thread
import multiprocessing
import time

contador_a = multiprocessing.Value('i') 
contador_b = multiprocessing.Value('i') 
contador_c = multiprocessing.Value('i') 
contador_total = multiprocessing.Value('i') 
contador_a.value = 0
contador_b.value = 0
contador_c.value = 0
contador_total.value = 0


def contar1(contador_a,contador_b,contador_c,contador_total):
    #global contador_a
    while  1:
        time.sleep(4)
        contador_a.value = contador_a.value + 1
        print('-----------------------------------')
        print('cuenta 1:',contador_a.value)
        print('cuenta 2:',contador_b.value)
        print('cuenta 3:',contador_c.value)
        contador_total.value = contador_a.value + contador_b.value + contador_c.value
        print('cuenta total:',contador_total.value)
        print('-----------------------------------')

def contar2(contador_a,contador_b,contador_c,contador_total):
    #global contador_b
    while  1:
        time.sleep(2)
        contador_b.value = contador_b.value + 1
        print('-----------------------------------')
        print('cuenta 1:',contador_a.value)
        print('cuenta 2:',contador_b.value)
        print('cuenta 3:',contador_c.value)
        contador_total.value = contador_a.value + contador_b.value + contador_c.value
        print('cuenta total:',contador_total.value)
        print('-----------------------------------')

def contar3(contador_a,contador_b,contador_c,contador_total):
    #global contador_c
    while  1:
        time.sleep(1)
        contador_c.value = contador_c.value + 1
        print('-----------------------------------')
        print('cuenta 1:',contador_a.value)
        print('cuenta 2:',contador_b.value)
        print('cuenta 3:',contador_c.value)
        contador_total.value = contador_a.value + contador_b.value + contador_c.value
        print('cuenta total:',contador_total.value)
        print('-----------------------------------')

hilo1 = multiprocessing.Process(target=contar1,args=(contador_a,contador_b,contador_c,contador_total))
hilo2 = multiprocessing.Process(target=contar2,args=(contador_a,contador_b,contador_c,contador_total))
hilo3 = multiprocessing.Process(target=contar3,args=(contador_a,contador_b,contador_c,contador_total))

hilo1.start()
hilo2.start()
hilo3.start()