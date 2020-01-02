"""
https://www.elecfreaks.com/learn-en/microbitKit/smart_cutebot/cutebot_case08.html
In this case there are smaller speeds than in the official example. For me the Cutebot drives to fast to stay on the line-tracking map.
"""

from microbit import *
import cutebot


display.show(Image.HAPPY)

while True:
    if not cutebot.has_left_track() and cutebot.has_right_track():
        cutebot.set_motors_speed(30, 10)
    elif cutebot.has_left_track() and not cutebot.has_right_track():
        cutebot.set_motors_speed(10, 30)
    elif cutebot.has_left_track() and cutebot.has_right_track():
        cutebot.set_motors_speed(30, 30)
