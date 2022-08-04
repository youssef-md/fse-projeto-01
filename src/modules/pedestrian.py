
from modules.gpio import gpio_set_event, gpio_setup
from modules.lights import update_light_transition

def callback(x):
    update_light_transition(2, True)

def pedestrian_button_handler():
    ports = [8, 10, 7, 9]
    
    for port in ports:
        gpio_setup(port, 'input')
        gpio_set_event(port, callback, 400)