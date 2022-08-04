import RPi.GPIO as GPIO
from time import sleep

gpio_setup_type = {
    'input': GPIO.IN,
    'output': GPIO.OUT
}

def config_gpio():
    GPIO.setmode(GPIO.BCM)

def gpio_setup(port, type):
    GPIO.setup(port, gpio_setup_type[type])

def gpio_high(port):
    GPIO.output(port, 1)

def gpio_low(port):
    GPIO.output(port, 0)

def gpio_set_event(port, callback, bouncetime):
    GPIO.add_event_detect(port, GPIO.RISING, callback=callback, bouncetime=bouncetime)