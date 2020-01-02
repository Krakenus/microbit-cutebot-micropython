"""
https://www.elecfreaks.com/learn-en/microbitKit/smart_cutebot/cutebot_case02.html
"""

from microbit import *
import cutebot


display.show(Image.HAPPY)

while True:
    for speed in range(cutebot.MAX_SPEED):
        cutebot.set_motors_speed(speed, speed)
