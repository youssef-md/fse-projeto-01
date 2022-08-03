import RPi.GPIO as GPIO

def config_gpio():
    GPIO.setmode(GPIO.BCM)

def gpio_high(port):
    GPIO.output(port, 1)

def gpio_low(port):
    GPIO.output(port, 0)

def gpio_setup_out(port):
    GPIO.setup(port, GPIO.OUT)
