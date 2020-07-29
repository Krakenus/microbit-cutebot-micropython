"""
Sets angle of servo connected to cutebot from 0 to 180 degrees and backwards.
"""

from microbit import display, Image, sleep

import cutebot


display.show(Image.HAPPY)

while True:
    print('Incrementing servo angle...')
    for i in range(cutebot.SERVO_ANGLE_MAX):
        cutebot.set_servo_1_angle(i)
        sleep(50)
    print('180 degrees reached')
    sleep(1000)
    print('Decrementing servo angle...')
    for i in range(cutebot.SERVO_ANGLE_MAX):
        cutebot.set_servo_1_angle(cutebot.SERVO_ANGLE_MAX - i)
        sleep(50)
    print('0 degrees reached')
    sleep(1000)
