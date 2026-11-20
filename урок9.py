from microbit import *
import radio
import music

# --- Настройки радио ---
GROUP = 9
POWER = 6

radio.on()
radio.config(group=GROUP, power=POWER)

# --- Параметры игры ---
MAX_HP = 5
BLOCK_MS = 400
PUNCH_COOLDOWN_MS = 350
VIBRO_MS = 180

# --- Звуковая отдача ---
def vibrate(freq=180, ms=VIBRO_MS):
    music.pitch(freq, ms, wait=False)

# --- Кнопки по краю ---
prev_a = False
prev_b = False

def just_pressed(current, prev):
    return current and (not prev)

# --- Отрисовка ---
def draw_bars(my_hp, enemy_hp, blocking, flash_hit):
    display.clear()
    # Враг (верх)
    for x in range(enemy_hp):
        display.set_pixel(x, 0, 6)
    # Мы (низ)
    for x in range(my_hp):
        display.set_pixel(x, 4, 9)
    # Значок блока в центре
    if blocking:
        display.set_pixel(1, 2, 7)
        display.set_pixel(2, 2, 9)
        display.set_pixel(3, 2, 7)
    # Вспышка при ударе или попадании
    if flash_hit:
        display.set_pixel(0, 2, 9)
        display.set_pixel(4, 2, 9)

# --- Радио ---
def send_punch():
    radio.send("PUNCH")

def handle_radio_message(msg, my_hp, blocking):
    flash = False
    if msg == "PUNCH":
        if blocking:
            flash = True
            vibrate(880, 80)
        else:
            my_hp -= 1
            flash = True
            vibrate(150, VIBRO_MS)
    elif msg == "KO":
        return my_hp, flash, "WIN"
    return my_hp, flash, None

# --- Переменные матча ---
my_hp = MAX_HP
enemy_hp = MAX_HP
block_until = 0
last_punch_time = 0
flash_hit = False
flash_until = 0

display.show(Image.SQUARE)
sleep(300)
display.clear()

# --- Главный цикл игры ---
while True:
    now = running_time()

    # 1) Чтение кнопок A (удар) и B (блок)
    btn_a = button_a.is_pressed()
    btn_b = button_b.is_pressed()

    jp_a = just_pressed(btn_a, prev_a)
    jp_b = just_pressed(btn_b, prev_b)

    prev_a = btn_a
    prev_b = btn_b

    # Блок (кнопка B)
    if jp_b:
        block_until = now + BLOCK_MS
    blocking = now < block_until

    # Удар (кнопка A)
    if jp_a and (now - last_punch_time >= PUNCH_COOLDOWN_MS):
        last_punch_time = now
        send_punch()
        enemy_hp = max(0, enemy_hp - 1)
        flash_hit = True
        flash_until = now + 120

    # 2) Приём радио
    msg = radio.receive()
    if msg:
        my_hp, got_flash, state = handle_radio_message(msg, my_hp, blocking)
        if got_flash:
            flash_hit = True
            flash_until = now + 160
        if state == "WIN":
            display.scroll("WIN")
            break

    # 3) Сброс вспышки по таймеру
    if flash_hit and now > flash_until:
        flash_hit = False

    # 4) Отрисовка
    draw_bars(my_hp, enemy_hp, blocking, flash_hit)

    # 5) Проверка KO
    if my_hp <= 0:
        radio.send("KO")
        display.scroll("KO")
        break

    sleep(30)
