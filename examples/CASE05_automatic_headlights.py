"""
https://www.elecfreaks.com/learn-en/microbitKit/smart_cutebot/cutebot_case05.html
"""

from micropython import const

from microbit import *
import cutebot


# change this value to set different speed
SPEED = cutebot.FULL_SPEED
# change this value to set minimal light level to turn of the lights
MIN_LIGHT = const(10)

cutebot.set_motors_speed(SPEED, SPEED)

while True:
    light = display.read_light_level()
    if light < MIN_LIGHT:
        cutebot.set_left_rgb_led(cutebot.RGB_MAX, cutebot.RGB_MAX, cutebot.RGB_MAX)
        cutebot.set_right_rgb_led(cutebot.RGB_MAX, cutebot.RGB_MAX, cutebot.RGB_MAX)
    else:
        cutebot.set_left_rgb_led(cutebot.RGB_MIN, cutebot.RGB_MIN, cutebot.RGB_MIN)
        cutebot.set_right_rgb_led(cutebot.RGB_MIN, cutebot.RGB_MIN, cutebot.RGB_MIN)
