import time
import pyautogui as pg
import module_custom_funcs as cf
import module_prepare_environment
from module_logger import CSVLogger

logger = CSVLogger()

def clear_trash_bin():
    logger.log("info", "Действие", "Очистка корзины")

    # Свернулся на рабочий стол 
    cf.win_d()

    # Открываем корзину
    cf.move_to(35, 35) # Верхний левый ярлычок на рабочем столе - корзина
    cf.click(35,35,2)

    # Очистка
    cf.move_to(700,450)
    cf.click(700,450,1,'right')
    cf.press_key('down', 8)
    cf.press_key('enter')
    cf.press_key('enter')
    # Если вдруг корзина пуста, то тут мы зайдем в "Свойства" и закроем

    # Закрываем проводник
    cf.alt_f4()

    return

def open_notepad_and_write(text="Тестовая запись", path_to_txt=""):
    logger.log("info", "Действие", "Открытие Блокнота через Win+R")

    cf.win_d() # Необязательное но я сворачиваю на всякий
    
    # Вызываем окно "Выполнить"
    cf.hotkey('win', 'r')
    cf.sleep(1) # Ждем появления окна
    
    # Печатаем команду запуска
    cf.type_text(f"notepad {path_to_txt}")
    cf.press_key('enter')
    cf.sleep(2) # Ждем открытия самого Блокнота
    
    # Пишем текст
    logger.log("info", "Действие", f"Печать текста в блокноте...")
    cf.type_text(text)
    cf.sleep(1)
    
    # Сохраняем (Ctrl+S)
    cf.ctrl_s()
    cf.sleep(1)
    
    if path_to_txt == "":
        # Ввод имени файла
        cf.type_text(f"note_{time.strftime('%Y%m%d_%H%M%S')}.txt")

        cf.press_key('tab', 4)
        cf.press_key('enter') # Сохраняется в документы
    
    cf.sleep(1)

    # Закрываем
    cf.alt_f4()
    logger.log("info", "Действие", "Блокнот закрыт")

    return

if __name__ == "__main__":

    # module_prepare_environment.set_resolution(1280, 720)

    # clear_trash_bin()
    open_notepad_and_write("rysskaya raskladka ne rabotaet, nado fiksit ")
    open_notepad_and_write("dopisivaem v tot je fail ", "C:/Users/user/Documents/note_20260215_203104.txt")

    pass