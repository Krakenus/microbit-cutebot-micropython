"""
Prints distance computed from echo of HC-SR04 ultrasonic module connected to cutebot.
"""

from microbit import display, Image, sleep

import cutebot


display.show(Image.HAPPY)

while True:
    distance = cutebot.get_sonar_distance()
    print('Distance: {}'.format(distance))
    sleep(1000)
