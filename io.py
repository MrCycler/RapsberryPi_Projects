import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

i = 0

while  i != 100:
	i = i+1
	if i % 2 == 0:
		GPIO.output(12,1)
		time.sleep(5)
		print('LED in ON')
	else:
		GPIO.output(12,0)
		time.sleep(5)
		print('LED IN OFF')
