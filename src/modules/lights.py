from modules.gpio import gpio_low, gpio_high, gpio_setup
from time import sleep
from threading import Thread

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
    'main_state': 'green',
    'aux_state': 'red',
    'green': 'yellow',
    'yellow': 'red',
    'red': 'green',
    'main_duration': 10,
    'aux_duration': 10,
    'hasPedestrian': False,
}

def init_traffic_control():
    config_light_output()

    thread_main_street = Thread(target=control_street, args=('main',))
    thread_aux_street = Thread(target=control_street, args=('aux',))

    thread_main_street.start()
    thread_aux_street.start()

    thread_main_street.join()
    thread_aux_street.join()
    

def control_street(street):
    while True:
        street_state = f'{street}_state'
        street_duration = f'{street}_duration'
        current_state = light_transition_state[street_state]
        
        if(light_transition_state['hasPedestrian']):
            update_light_transition(5, False)

        gpio_high(light_gpio_crossing[0][current_state][street])
        gpio_high(light_gpio_crossing[1][current_state][street])

        if(light_transition_state[street_state] == 'yellow'):
            sleep(1)
        else:
            sleep(light_transition_state[street_duration])
        
        gpio_low(light_gpio_crossing[0][current_state][street])
        gpio_low(light_gpio_crossing[1][current_state][street])

        light_transition_state[street_state] = light_transition_state[current_state]
       


def update_light_transition(duration, hasPedestrian):
    light_transition_state['main_duration'] = duration
    light_transition_state['aux_duration'] = duration
    light_transition_state['hasPedestrian'] = hasPedestrian


def config_light_output():
    for crossing in light_gpio_crossing:
        for light in crossing:
            main = crossing[light]['main']
            aux = crossing[light]['aux']
            gpio_setup(main, 'output')
            gpio_setup(aux, 'output')
            gpio_low(main)
            gpio_low(aux)

def debug_lights():
    gpio_high(light_gpio_crossing[1]['green']['main'])
    gpio_high(light_gpio_crossing[1]['yellow']['main'])
    gpio_high(light_gpio_crossing[1]['red']['main'])
    sleep(2)
    gpio_high(light_gpio_crossing[1]['green']['aux'])
    gpio_high(light_gpio_crossing[1]['yellow']['aux'])
    gpio_high(light_gpio_crossing[1]['red']['aux'])
