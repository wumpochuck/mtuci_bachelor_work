import pyautogui as pg
import random
import time
import win32api
import win32con
import ctypes
from module_logger import CSVLogger

logger = CSVLogger()

def human_delay(min_sec=0.1, max_sec=0.5):
    # Внутренняя функция для создания небольших пауз.
    time.sleep(random.uniform(min_sec, max_sec))

def move_to(x, y, duration=None):
    if duration is None:
        duration = random.uniform(0.5, 1.2)
    try:
        logger.log("debug", f"Перемещение мыши в ({x}, {y})", f"duration={duration}")
        pg.moveTo(x, y, duration=duration, tween=pg.easeInOutQuad)
    except Exception as e:
        logger.log("error", "Ошибка при перемещении мыши", str(e))

def click(x=None, y=None, clicks=1, button='left'):
    try:
        ctx = f"coords=({x},{y}), clicks={clicks}, button={button}"
        logger.log("info", "Клик мышью", ctx)
        pg.click(x=x, y=y, clicks=clicks, interval=random.uniform(0.1, 0.3), button=button)
        human_delay()
    except Exception as e:
        logger.log("error", "Ошибка при клике", str(e))

def type_text(text, interval=None):
    if interval is None:
        interval = random.uniform(0.2, 0.4)
    try:
        logger.log("info", "Ввод текста", f"Длина текста: {len(text)} симв.")
        # pg.typewrite(text, interval=interval)
        pg.write(text, interval=interval)
        human_delay()
    except Exception as e:
        logger.log("error", "Ошибка при вводе текста", str(e))

def press_key(key, presses=1):
    try:
        logger.log("debug", f"Нажатие клавиши: {key}", f"Кол-во: {presses}")
        pg.press(key, presses=presses, interval=random.uniform(0.3, 0.5))
        human_delay()
    except Exception as e:
        logger.log("error", f"Ошибка при нажатии {key}", str(e))

def hotkey(*args):
    try:
        logger.log("info", "Комбинация клавиш", "+".join(args))
        pg.hotkey(*args)
        human_delay()
    except Exception as e:
        logger.log("error", f"Ошибка комбинации {args}", str(e))

def alt_tab():
    hotkey('alt', 'tab')

def win_d():
    hotkey('win', 'd')

def ctrl_s():
    hotkey('ctrl', 's')

def alt_f4():
    hotkey('alt', 'f4')

def win_r_run(command):
    hotkey('win', 'r')
    time.sleep(0.5)
    type_text(command)
    press_key('enter')
    logger.log("info", "Запуск команды через Win+R", f"Команда: {command}")

def sleep(seconds):
    logger.log("info", "Ожидание (Idle)", f"{seconds} сек.")
    time.sleep(seconds)