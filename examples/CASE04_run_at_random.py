"""
https://www.elecfreaks.com/learn-en/microbitKit/smart_cutebot/cutebot_case04.html
"""

import random

from microbit import *
import cutebot

# Uncomment this to set different pseudo-random generator seed.
# random.seed(666)

display.show(Image.GHOST)

while True:
    left_speed = random.randint(-100, 100)
    right_speed = random.randint(-100, 100)
    cutebot.set_motors_speed(left_speed, right_speed)
    sleep(1000)
