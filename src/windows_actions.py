import time
import module_custom_funcs as cf
from module_logger import CSVLogger

logger = CSVLogger()

def open_task_manager():
    """Открывает диспетчер задач через горячие клавиши."""
    logger.log("info", "Действие ОС", "Открытие диспетчера задач (Ctrl+Shift+Esc)")
    cf.hotkey('ctrl', 'shift', 'esc')
    cf.sleep(2) # Ждем прорисовки окна

def close_current_window():
    """Закрывает активное окно."""
    logger.log("info", "Действие ОС", "Закрытие текущего окна (Alt+F4)")
    cf.alt_f4()
    cf.sleep(1)

def open_windows_settings():
    """Открывает параметры Windows через Win+I."""
    logger.log("info", "Действие ОС", "Открытие параметров Windows (Win+I)")
    cf.hotkey('win', 'i')
    cf.sleep(3)

def check_system_info():
    """Имитирует проверку свойств системы."""
    logger.log("info", "Действие ОС", "Запуск проверки свойств системы (Win+Pause/Break)")
    # Если на клавиатуре нет Pause, можно использовать Win+R -> msinfo32
    cf.hotkey('win', 'r')
    cf.sleep(0.5)
    cf.type_text("msinfo32")
    cf.press_key('enter')
    cf.sleep(4)

def search_in_start_menu(query):
    """Ищет что-либо через меню Пуск."""
    logger.log("info", "Действие ОС", f"Поиск в меню Пуск: {query}")
    cf.press_key('win')
    cf.sleep(1)
    cf.type_text(query)
    cf.sleep(2)
    cf.press_key('enter')

if __name__ == "__main__":
    logger.log("info", "Тест", "Запуск сценария взаимодействия с ОС")
    
    cf.win_d() # Свернуть всё
    
    search_in_start_menu("Калькулятор") # не работает ?????
    cf.sleep(2)
    cf.type_text("123*4")
    cf.press_key('enter')
    cf.sleep(2)
    
    open_task_manager()
    cf.sleep(3)
    
    # Переключаемся на калькулятор и закрываем его
    cf.alt_tab()
    close_current_window()
    
    # Закрываем диспетчер задач
    close_current_window()
    
    logger.log("info", "Тест", "Сценарий завершен")