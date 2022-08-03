from time import sleep

light_gpio_crossing = [
    {
        'green': [1,2],
        'yellow': [26, 3],
        'red': [21, 11]
    },
    {
        'green': [20, 0],
        'yellow': [16, 5],
        'red': [12, 6]
    }
]

light_transition_state = {
    'red': 'green',
    'green': 'yellow',
    'yellow': 'red'
}

def reset_all_lights():


def init_lights():

    # GPIO.setup(SEMAFORO_1_VERDE, GPIO.OUT)
    # GPIO.output(SEMAFORO_1_VERDE, 0)

    # for verde in SEMAFORO_1_VERDE:
    #     GPIO.output(verde, 1)
    #     sleep(1)
    #     GPIO.output(verde, 0)