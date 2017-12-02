from threading import Thread
import serial
import smbus
import time


class HiloRKZ:
    def _init_(self):
        self._running = True
        
    def terminate(self):
        self._running = False
        
    def run(self):
        
        while self._running:
            #cambia los valores cada seg            
          # while True:
				print "Light Level : " + str(readLight()) + " lx"
				time.sleep(0.5)
          
# Define some constants from the datasheet
 
DEVICE     = 0x23 # Default device I2C address
 
POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value
 
# Start measurement at 4lx resolution. Time typically 16ms.
CONTINUOUS_LOW_RES_MODE = 0x13
# Start measurement at 1lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_1 = 0x10
# Start measurement at 0.5lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_2 = 0x11
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_1 = 0x20
# Start measurement at 0.5lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_2 = 0x21
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_LOW_RES_MODE = 0x23
 
#bus = smbus.SMBus(0) # Rev 1 Pi uses 0
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1
 
def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number
  return ((data[1] + (256 * data[0])) / 1.2)
 
def readLight(addr=DEVICE):
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
  return convertToNumber(data)

bluetoothSerial = serial.Serial("/dev/rfcomm0",baudrate=9600)
print("Bluetooth connected")
FiveSecond = HiloRKZ()
FiveSecondThread = Thread(target=FiveSecond.run)
FiveSecondThread.start()
Exit = False
while Exit==False:
	c=raw_input("Ingrese Comando del Carro:")
	if(c=='w'):
		print("Carro Avanzando")
		bluetoothSerial.write("1")
	elif(c=='a'):
		print("Carro Izquierda")
		bluetoothSerial.write("2")
	elif(c=='d'):
		print("Carro Derecha")
		bluetoothSerial.write("3")
	elif(c=='s'):
		print("Carro Atras")
		bluetoothSerial.write("4")
	elif(c=='x'):
		print ("Stop")
		bluetoothSerial.write("0")
	elif(c=='q'):
		print ("Quit")
		bluetoothSerial.write("0")
		Exit = True
	else:
		print("Codigo Incorrecto")
	
FiveSecond.terminate()
print "Jajaja Saludos"