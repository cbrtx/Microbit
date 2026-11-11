# player.py - Модуль управления для Piano Hero
from microbit import *
import gamepad

def get_pressed_lane():
    if gamepad.button_A():
        return 0
    elif gamepad.button_B():
        return 1
    elif gamepad.button_X():
        return 3
    elif gamepad.button_Y():
        return 4
    return None

def draw_zone():
    for x in [0, 1, 3, 4]:
        display.set_pixel(x, 4, 2)