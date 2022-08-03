from modules.gpio import gpio_output

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
    for crossing in light_gpio_crossing:
        for light in crossing:
            gpio_output(crossing[light][0], 0)
            gpio_output(crossing[light][1], 0)

