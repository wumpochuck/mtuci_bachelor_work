import pyautogui as pg

def move_to(x, y, duration=0.5):
    """Перемещает курсор мыши к указанным координатам (x, y) за заданное время duration."""
    pg.moveTo(x, y, duration=duration)

def click(x=None, y=None, clicks=1, interval=0.0, button='left'):
    """Выполняет клик мышью в указанных координатах (x, y). 
    Если координаты не указаны, кликает в текущем положении курсора.
    Можно задать количество кликов и интервал между ними."""
    pg.click(x=x, y=y, clicks=clicks, interval=interval, button=button)

def type_text(text, interval=0.0):
    """Вводит указанный текст с заданным интервалом между нажатиями клавиш."""
    pg.typewrite(text, interval=interval)

def press_key(key, presses=1, interval=0.0):
    """Нажимает указанную клавишу заданное количество раз с интервалом между нажатиями."""
    pg.press(key, presses=presses, interval=interval)

def alt_tab(alt_times=1):
    """Переключается между открытыми окнами с помощью Alt+Tab заданное количество раз."""
    for _ in range(alt_times):
        pg.keyDown('alt')
        pg.press('tab')
        pg.keyUp('alt')

def win_d():
    """Нажимает комбинацию клавиш Win+D для показа рабочего стола."""
    pg.keyDown('win')
    pg.press('d')
    pg.keyUp('win')

def sleep(seconds):
    """Приостанавливает выполнение программы на заданное количество секунд."""
    pg.sleep(seconds)

def ctrl_s():
    """Нажимает комбинацию клавиш Ctrl+S для сохранения документа."""
    pg.keyDown('ctrl')
    pg.press('s')
    pg.keyUp('ctrl')

def alt_f4():
    """Нажимает комбинацию клавиш Alt+F4 для закрытия текущего окна."""
    pg.keyDown('alt')
    pg.press('f4')
    pg.keyUp('alt')