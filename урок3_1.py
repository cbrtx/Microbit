from microbit import *
import gamepad
import music

while True:
    if gamepad.button_A():
        display.show(Image.ANGRY)
        gamepad.vibrate(duration=100)
        display.clear()
        
    if gamepad.button_B():
        display.show(Image.MUSIC_QUAVER)
        music.play(music.BA_DING, wait=False)
        sleep(300)
        display.clear()