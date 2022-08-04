
from modules.gpio import gpio_set_event, gpio_setup
from modules.lights import update_light_transition

def callback(x):
    update_light_transition(2, True)

def pedestrian_button_handler():
    port = 9
    gpio_setup(port, 'input')
    gpio_set_event(port, callback, 400)