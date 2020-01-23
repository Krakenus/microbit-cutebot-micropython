"""
https://www.elecfreaks.com/learn-en/microbitKit/smart_cutebot/cutebot_case06.html
"""

from micropython import const

from microbit import *
import neopixel
import cutebot


RIGHT = const(0)
LEFT = const(1)
BLINK_COUNT = const(5)

np = neopixel.NeoPixel(pin15, 2)

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

while True:
    if button_a.is_pressed():
        for i in range(BLINK_COUNT):
            np[RIGHT] = YELLOW
            np.show()
            cutebot.set_right_rgb_led(*YELLOW)
            sleep(500)
            np[RIGHT] = BLACK
            np.show()
            cutebot.set_right_rgb_led(*BLACK)
            sleep(500)

    if button_b.is_pressed():
        for i in range(BLINK_COUNT):
            np[LEFT] = YELLOW
            np.show()
            cutebot.set_left_rgb_led(*YELLOW)
            sleep(500)
            np[LEFT] = BLACK
            np.show()
            cutebot.set_left_rgb_led(*BLACK)
            sleep(500)

