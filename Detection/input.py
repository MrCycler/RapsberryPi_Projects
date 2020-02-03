import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)

i = 0

while  i != 100:
        i = i+1
        if GPIO.input(12):
                time.sleep(1)
                print('Detected')
        else:
                time.sleep(1)
                print('No detected')

