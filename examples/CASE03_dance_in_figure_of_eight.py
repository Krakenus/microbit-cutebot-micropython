"""
https://www.elecfreaks.com/learn-en/microbitKit/smart_cutebot/cutebot_case03.html
"""

from microbit import *
import cutebot


display.show(Image.PACMAN)

while True:
    cutebot.go_forward()
    sleep(200)
    cutebot.set_motors_speed(100, 40)
    sleep(1000)
    cutebot.go_forward()
    sleep(200)
    cutebot.go_forward()
    sleep(200)
    cutebot.set_motors_speed(40, 100)
    sleep(1000)
    cutebot.go_forward()
    sleep(200)
