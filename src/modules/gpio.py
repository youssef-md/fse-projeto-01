import RPi.GPIO as GPIO
import lights

def config_gpio():
    GPIO.setmode(GPIO.BCM)
    config_outputs()

def config_outputs():
    for crossing in lights.light_gpio_crossing:
        for light in crossing:
            GPIO.setup(crossing[light][0], GPIO.OUT)
            GPIO.setup(crossing[light][1], GPIO.OUT)

def gpio_output(port, signal):
    GPIO.output(port, signal)