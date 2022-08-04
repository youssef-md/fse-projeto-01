from modules.lights import init_traffic_control, debug_lights
from modules.gpio import config_gpio

def main():

    config_gpio()
    init_traffic_control()
    
    while True:
        signal.pause()

if __name__ == "__main__":
    main()