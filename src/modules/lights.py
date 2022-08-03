from modules.gpio import gpio_low, gpio_high, gpio_toggle, gpio_setup_out
from time import sleep

light_gpio_crossing = [
    {
        'green': {
            'main': 2,
            'aux': 1,
        },
        'yellow': {
            'main': 3,
            'aux': 26,
        },
        'red': {
            'main': 11,
            'aux': 21,
        },
    },
    {
        'green': {
            'main': 0,
            'aux': 20,
        },
        'yellow': {
            'main': 5,
            'aux': 16,
        },
        'red': {
            'main': 6,
            'aux': 12,
        }
    }
]

light_transition_state = {
    # 'current': 'green', 
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
        current_state = 'green'

        for crossing in light_gpio_crossing:
            gpio_high(crossing[current_state]['main'])
            sleep(5)
            gpio_low(crossing[current_state]['main'])

        current_state = light_transition_state['current']

            
