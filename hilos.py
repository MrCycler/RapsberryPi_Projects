from threading import Thread
import serial
import time

global cycle
cycle= 0
global bandera
bandera=0
global finalcd
finalcd=60

class Hello5Program:
    def __init__(self):
        self._running = True
        
    def terminate(self):
        self._running = False
        
    def run(self):
        global cycle
        global bandera
        while self._running:
            #cambia los valores de pwm cada seg            
            time.sleep(1)
            ser.write(chr(cycle))
            if(bandera==0):
                cycle = cycle+50
            if(bandera==1):
                cycle = cycle-50
            if(cycle>250):
                cycle=250
                bandera=1
            if(cycle<0):
                cycle=0
                bandera=0
            print "Hilo2 says: duty cicle", cycle

ser = serial.Serial('/dev/ttyACM0',9600)
FiveSecond = Hello5Program()
FiveSecondThread = Thread(target=FiveSecond.run)
FiveSecondThread.start()

Exit = False
while Exit==False:
    finalcd = finalcd - 5
    print "Hilo1 principal says: Finalcd en segundos$", finalcd
    time.sleep(5)
    if (finalcd==0): Exit = True
    
FiveSecond.terminate()
print "Jajaja Saludos"
            
        