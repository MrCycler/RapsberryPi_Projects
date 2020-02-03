import RPi.GPIO as GPIO
from threading import Thread
import time
import cv2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)

i = 0

while  1:
	channel = GPIO.wait_for_edge(11,GPIO.RISING,timeout=3000)
	if channel is None:
		print('Timeout')
		if GPIO.input(11):
			print('Translape')
			i = i + 1
			print('cuenta :',i)
	else:
		i = i+1
		print('cuenta : ', i)
		time.sleep(0.5)
	k = cv2.waitKey(10) & 0xff
	if k == ord('q'):
      		break


