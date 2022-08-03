from modules.gpio import gpio_low, gpio_high, gpio_toggle, gpio_setup_out
from time import sleep

light_gpio_crossing = [
    {
        'green': {
            'main': 20,
            'aux': 1,
        },
        'yellow': {
            'main': 16,
            'aux': 26,
        },
        'red': {
            'main': 12,
            'aux': 21,
        },
    },
    {
        'green': {
            'main': 0,
            'aux': 2,
        },
        'yellow': {
            'main': 5,
            'aux': 3,
        },
        'red': {
            'main': 6,
            'aux': 11,
        }
    }
]

light_transition_state = {
    'current': 'green',
    'green': 'yellow',
    'yellow': 'red',
    'red': 'green',
}

def config_light_output():
    for crossing in light_gpio_crossing:
        for light in crossing:
            main = crossing[light]['main']
            aux = crossing[light]['aux']
            gpio_setup_out(main)
            gpio_setup_out(aux)
            gpio_low(main)
            gpio_low(aux)

def init_traffic_control():
    while True:
        current_state = light_transition_state['current']

        
        gpio_high(light_gpio_crossing[0][current_state]['main'])
        gpio_high(light_gpio_crossing[1][current_state]['main'])
        sleep(2)
        gpio_low(light_gpio_crossing[0][current_state]['main'])
        gpio_low(light_gpio_crossing[1][current_state]['main'])

        light_transition_state['current'] = light_transition_state[current_state]

            
def debug_lights():
    gpio_high(light_gpio_crossing[1]['green']['main'])
    gpio_high(light_gpio_crossing[1]['yellow']['main'])
    gpio_high(light_gpio_crossing[1]['red']['main'])
    sleep(2)
    gpio_high(light_gpio_crossing[1]['green']['aux'])
    gpio_high(light_gpio_crossing[1]['yellow']['aux'])
    gpio_high(light_gpio_crossing[1]['red']['aux'])
