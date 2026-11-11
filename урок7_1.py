from microbit import *

smooth = 0

while True:
    level = microphone.sound_level()      # 0..255
    smooth = (smooth * 3 + level) // 4   # сглаживание

    bars = (smooth * 5) // 255           # 0..5 уровней

    display.clear()
    for y in range(5):
        if y >= 5 - bars:
            display.set_pixel(2, y, 9)

    sleep(50)