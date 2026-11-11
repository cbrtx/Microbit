from microbit import *
import player, random, music, gamepad

notes = []           # Наш "шкаф" для летящих нот
score = 0            # Счет игрока
spawn_timer = 0      # Счетчик для появления новых нот
game_speed = 300     # Интервал движения нот (мс)
last_move_time = running_time() # Время последнего сдвига нот

while True:
    # 1. БЫСТРЫЙ ОПРОС КНОПОК
    pressed = player.get_pressed_lane()
    if pressed is not None:
        hit = False
        for note in notes[::-1]:
            if note[0] == pressed and note[1] == 4:
                notes.remove(note)
                score += 1
                hit = True
                music.pitch(440 + (pressed * 100), 50, wait=False)
                break
        if not hit:
            gamepad.vibrate(50)
        sleep(120) # Защита от дребезга (двойного нажатия)

    # 2. ДВИЖЕНИЕ НОТ
    if running_time() - last_move_time > game_speed:
        last_move_time = running_time()
        for note in notes:
            note[1] += 1
    
        spawn_timer += 1
        if spawn_timer >= 5:
            new_lane = random.choice([0, 1, 3, 4])
            notes.append([new_lane, 0])
            spawn_timer = 0

    # 3. ОТРИСОВКА И ПРОВЕРКА GAME OVER
    display.clear()
    player.draw_zone()
    
    game_over = False
    for note in notes:
        if note[1] > 4:
            game_over = True
            break
        if 0 <= note[1] <= 4:
            display.set_pixel(note[0], note[1], 9)

    if game_over:
        music.play(music.POWER_DOWN)
        gamepad.vibrate(500)
        display.show(Image.SKULL)
        sleep(1000)
        display.scroll("SCORE: " + str(score))
        notes, score, last_move_time = [], 0, running_time()
        continue
    
    sleep(10)