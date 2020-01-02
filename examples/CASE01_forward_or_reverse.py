"""
https://www.elecfreaks.com/learn-en/microbitKit/smart_cutebot/cutebot_case01.html
"""

from microbit import *
import cutebot


display.show(Image.HAPPY)

while True:
    if button_a.is_pressed():
        cutebot.go_forward()
    elif button_b.is_pressed():
        cutebot.go_backward()
