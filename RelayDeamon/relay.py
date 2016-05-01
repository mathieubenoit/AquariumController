import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, True)

GPIO.setup(27, GPIO.OUT)

for i in range(10):

	GPIO.output(27, True)
	sleep(1)
	GPIO.output(27, False)
	sleep(1)
	GPIO.output(27, True)
