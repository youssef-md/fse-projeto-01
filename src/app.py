from modules.lights import config_light_output, init_traffic_control
from modules.gpio import config_gpio

config_gpio()
config_light_output()

init_traffic_control()