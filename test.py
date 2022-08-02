import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

SEMAFORO_1_VERDE = [1, 2]

GPIO.setup(SEMAFORO_1_VERDE, GPIO.OUT)
GPIO.output(SEMAFORO_1_VERDE, 0)


for verde in SEMAFORO_1_VERDE:
	GPIO.output(verde, 1)
	sleep(1)
	GPIO.output(verde, 0)