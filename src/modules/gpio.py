import RPi.GPIO as GPIO
from time import sleep

def config_gpio():
    GPIO.setmode(GPIO.BCM)

def gpio_setup_out(port):
    GPIO.setup(port, GPIO.OUT)

def gpio_high(port):
    GPIO.output(port, 1)

def gpio_low(port):
    GPIO.output(port, 0)

def gpio_toggle(port, time):
    gpio_high(port)
    sleep(time)
    gpio_low(port)
