from microbit import *
import gamepad

TRACK_Y = 2
FRAME_MS = 70
MOVE_DELTA = 18
MAX_SPEED10 = 6
#шаг 2
GATES = [(1, 700, 0), (2, 900, 200), (3, 800, 400)]
smooth = 0
noise_floor = 0

def gate_is_open(x, t_ms):
    for gx, period, phase in GATES:
        if gx == x:
            m = (t_ms + phase) % period
            return m < (period // 2)
    return True

def read_sound_smooth():
    global smooth
    level = microphone.sound_level()
    smooth = (smooth * 3 + level) // 4
    return smooth

def speed10_from_sound(level):
    diff = level - (noise_floor + MOVE_DELTA)
    if diff <= 0:
        return 0
    if diff > 200:
        diff = 200
    return (diff * MAX_SPEED10) // 200

def calibrate_noise():
    total = 0
    samples = 0
    start = running_time()
    while running_time() - start < 1200:
        total += microphone.sound_level()
        samples += 1
        sleep(30)
    if samples > 0:
        return total // samples
    return 0

def draw_world(player_x, t_ms, speed10):
    display.clear()
    display.set_pixel(0, 0, min(9, speed10 + 2))
    for gx, _, _ in GATES:
        if gate_is_open(gx, t_ms):
            display.set_pixel(gx, TRACK_Y, 2)
        else:
            display.set_pixel(gx, TRACK_Y, 9)
    display.set_pixel(4, TRACK_Y, 5)
    display.set_pixel(player_x, TRACK_Y, 9)

def crash():
    gamepad.vibrate(220)
    display.show(Image.SAD)
    sleep(900)

def win():
    display.show(Image.HAPPY)
    sleep(900)

display.scroll("CAL")
noise_floor = calibrate_noise()

pos10 = 0
player_x = 0
last_frame = running_time()

while True:
    now = running_time()

    if now - last_frame >= FRAME_MS:
        last_frame = now

        level = read_sound_smooth()
        speed10 = speed10_from_sound(level)

        pos10 += speed10
        new_x = pos10 // 10

        while player_x < new_x and player_x < 4:
            next_x = player_x + 1

            if not gate_is_open(next_x, now):
                crash()
                pos10 = 0
                player_x = 0
                break

            player_x = next_x

            if player_x == 4:
                win()
                pos10 = 0
                player_x = 0
                break
        draw_world(player_x, now, speed10)
        
    sleep(10)