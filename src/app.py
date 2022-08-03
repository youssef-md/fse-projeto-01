from modules.lights import config_light_output, init_traffic_control, debug_lights
from modules.gpio import config_gpio

config_gpio()
config_light_output()

# debug_lights()
init_traffic_control()