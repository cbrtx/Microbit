# gamepad.py - Драйвер для Yahboom Game Handle (Compact)
# Этот файл скрывает сложную работу с пинами и резисторами.

from microbit import *

# --- НАСТРОЙКИ ОБОРУДОВАНИЯ (КОНСТАНТЫ) ---
# Пины, к которым подключены кнопки на плате Yahboom
_PIN_RED = pin16     # Красная кнопка (X)
_PIN_BLUE = pin15    # Синяя кнопка (A)
_PIN_YELLOW = pin14  # Желтая кнопка (B)
_PIN_GREEN = pin13   # Зеленая кнопка (Y)

# Пины джойстика
_PIN_JOY_X = pin1
_PIN_JOY_Y = pin2

# Пин вибромотора
_PIN_VIBRO = pin12

# --- ИНИЦИАЛИЗАЦИЯ (АВТОМАТИЧЕСКАЯ) ---
# Этот код срабатывает сразу при импорте библиотеки.
# Мы включаем PULL_UP резисторы, чтобы кнопки не "шумели".
_PIN_RED.set_pull(pin16.PULL_UP)
_PIN_BLUE.set_pull(pin15.PULL_UP)
_PIN_YELLOW.set_pull(pin14.PULL_UP)
_PIN_GREEN.set_pull(pin13.PULL_UP)

# --- (API) ---

def button_A():
    """Возвращает True, если нажата СИНЯЯ кнопка (A)"""
    return _PIN_BLUE.read_digital() == 0

def button_B():
    """Возвращает True, если нажата ЖЕЛТАЯ кнопка (B)"""
    return _PIN_YELLOW.read_digital() == 0

def button_X():
    """Возвращает True, если нажата КРАСНАЯ кнопка (X)"""
    return _PIN_RED.read_digital() == 0

def button_Y():
    """Возвращает True, если нажата ЗЕЛЕНАЯ кнопка (Y)"""
    return _PIN_GREEN.read_digital() == 0

def joystick_x():
    """Возвращает положение стика по горизонтали (0..1023)"""
    return _PIN_JOY_X.read_analog()

def joystick_y():
    """Возвращает положение стика по вертикали (0..1023)"""
    return _PIN_JOY_Y.read_analog()

def vibrate(duration=100):
    """
    Включает вибрацию на указанное время (в миллисекундах).
    Пример: gamepad.vibrate(200)
    """
    _PIN_VIBRO.write_digital(1) # Вкл
    sleep(duration)             # Ждем
    _PIN_VIBRO.write_digital(0) # Выкл