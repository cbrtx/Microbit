from microbit import *
import gamepad
import random  # Подключаем генератор случайностей

# --- НАСТРОЙКИ ИГРЫ ---
player_x = 2  # Игрок начинает в центре (0, 1, 2, 3, 4)

enemy_x = random.randint(0, 4)  # Случайный X от 0 до 4
enemy_y = 0                    # Враг появляется сверху

timer = 0  # Таймер для замедления падения врага

# --- ГЛАВНЫЙ ЦИКЛ ---
while True:
    # 1. ПРОВЕРКА УПРАВЛЕНИЯ (Движение игрока)
    # Если наклоняем джойстик влево И мы не у левого края
    if gamepad.joystick_x() < 200 and player_x > 0:
        player_x -= 1

    # Если джойстик вправо И мы не у правого края
    elif gamepad.joystick_x() > 800 and player_x < 4:
        player_x += 1

    # 2. ЛОГИКА ВРАГА
    timer += 1
    if timer == 5:  # Каждые 5 циклов враг делает шаг вниз
        enemy_y += 1
        timer = 0   # Сбрасываем таймер

    # Если враг улетел за низ экрана — спавним нового
    if enemy_y > 4:
        enemy_x = random.randint(0, 4)
        enemy_y = 0

    # 3. СТРЕЛЬБА (Лазерная пушка)
    if gamepad.button_X():
        # Отрисовка луча лазера вверх от игрока
        for y in range(4):
            display.set_pixel(player_x, y, 3)  # Тусклый луч
        sleep(50)  # Короткая вспышка

        # Проверяем, попали ли во врага
        if player_x == enemy_x:
            gamepad.vibrate(100)        # Вибрация от взрыва
            display.show(Image.TARGET)  # Картинка взрыва
            sleep(200)

            # Создаем нового врага взамен уничтоженного
            enemy_y = 0
            enemy_x = random.randint(0, 4)

    # 4. ПРОВЕРКА ПРОИГРЫША (GAME OVER)
    # Если враг достиг низа (Y=4) И его X совпал с X игрока
    if enemy_y == 4 and enemy_x == player_x:
        gamepad.vibrate(500)       # Длинная вибрация (полсекунды)
        display.show(Image.SKULL)  # Показываем череп грустного финала
        break                      # Прерывание основного цикла и выход из игры

    # 5. РИСОВАНИЕ
    display.clear()
    display.set_pixel(player_x, 4, 9)       # Игрок (Яркий)
    display.set_pixel(enemy_x, enemy_y, 5)  # Враг (Потусклее)

    # 6. ПАУЗА (Скорость игры)
    sleep(150)

