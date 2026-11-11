from microbit import *
import gamepad  # Подключаем наш файл-драйвер

# Первая часть 
"""display.scroll("Hello Bit!")

while True:
    if gamepad.button_A():
        display.show("A")
        
    elif gamepad.button_B():
        display.show("B")
        
    elif gamepad.button_Y():
        display.show("Y")
        
    elif gamepad.button_X():
        display.show("X")"""

#  Вторая часть
"""while True:
    # Получаем координаты стика
    x = gamepad.joystick_x()
    y = gamepad.joystick_y()
    
    # Выводим их в консоль компьютера
    print("X:", x, "Y:", y)
    
    sleep(100)"""

# Третья часть
"""while True:
    x = gamepad.joystick_x()
    y = gamepad.joystick_y()
        
    if x < 200:
        display.show(Image.ARROW_W)
    elif x > 800:
        display.show(Image.ARROW_E)
    elif y < 200:
        # ВНИМАНИЕ: Проверьте свой джойстик. 
        # Часто 0 - это Верх (North), но бывает наоборот!
        display.show(Image.ARROW_N) 
    elif y > 800:
        display.show(Image.ARROW_S)
    else:
        display.clear()"""

# Четвертая часть

display.show(Image.HAPPY)
sleep(500)

while True:
    # 1. Сначала проверяем кнопки
    if gamepad.button_A():
        display.show("A")
        
    elif gamepad.button_B():
        display.show("B")
        
    elif gamepad.button_Y():
        display.show("Y")
        
    elif gamepad.button_X():
        display.show("X")
        gamepad.vibrate(100) # Короткая вибрация!
        sleep(200) # Пауза, чтобы не вибрировал сплошным гулом
        
    # 2. Если кнопки не трогали, проверяем джойстик
    else:
        x = gamepad.joystick_x()
        y = gamepad.joystick_y()
        
        if x < 200:
            display.show(Image.ARROW_W)
        elif x > 800:
            display.show(Image.ARROW_E)
        elif y < 200:
            # ВНИМАНИЕ: Проверьте свой джойстик. 
            # Часто 0 - это Верх (North), но бывает наоборот!
            display.show(Image.ARROW_N) 
        elif y > 800:
            display.show(Image.ARROW_S)
        else:
            display.clear()


