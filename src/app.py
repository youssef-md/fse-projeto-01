from modules.lights import init_traffic_control, debug_lights
from modules.gpio import config_gpio
from modules.pedestrian import pedestrian_button_handler

def main():

    config_gpio()
    pedestrian_button_handler()
    init_traffic_control()

    while True:
        signal.pause()

if __name__ == "__main__":
    main()