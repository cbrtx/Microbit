from microbit import *
import gamepad
import music

player_x = 0
player_y = 0

mines = [(1, 1), (2, 2), (3, 0), (0, 3), (4, 2)]

# 2
    
while True:
    # управление
    if gamepad.joystick_x() < 200 and player_x > 0:
        player_x -= 1
        sleep(200)
    elif gamepad.joystick_x() > 800 and player_x < 4:
        player_x += 1
        sleep(200)
    # сами для y
    if gamepad.joystick_y() < 200 and player_y > 0:
        player_y -= 1
        sleep(200)
    elif gamepad.joystick_y() > 800 and player_y < 4:
        player_y += 1
        sleep(200)
    # 3 
    display.clear()
    display.set_pixel(player_x, player_y, 9)
    #4
    # Собираем текущие координаты в кортеж
    current_pos = (player_x, player_y)

    # Проверяем встал ли игрок на мины
    if current_pos in mines:
        music.play(music.BA_DING, wait=False)
        gamepad.vibrate(100)
        display.show(Image.SKULL)
        sleep(300)

        # Возврат игрока на старт
        player_x = 0
        player_y = 0
    
    #5
    # выигрыш
    if player_x == 4 and player_y == 4:
        music.play(music.ENTERTAINER, wait=False)
        display.show(Image.HAPPY)

        # Салют из вибрации
        for i in range(3):
            gamepad.vibrate(100)
            sleep(100)
        break
        
        