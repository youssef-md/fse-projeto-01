from modules.lights import reset_all_lights
from modules import gpio

gpio.config_gpio()
reset_all_lights()
