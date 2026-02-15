import win32api
import win32con
import winreg
from module_logger import CSVLogger

logger = CSVLogger()

def set_resolution(width, height):
    print(f"Установка разрешения {width}x{height}...")
    logger.log("info", f"Установка разрешения {width}x{height}", "set_resolution")
    
    try:
        devmode = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
        print(f"Текущее разрешение: {devmode.PelsWidth}x{devmode.PelsHeight}")
        logger.log("debug", f"Текущее разрешение: {devmode.PelsWidth}x{devmode.PelsHeight}", "set_resolution")
        
        devmode.PelsWidth = width
        devmode.PelsHeight = height
        devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
        print(f"Новые параметры: {devmode.PelsWidth}x{devmode.PelsHeight}")
        
        result = win32api.ChangeDisplaySettings(devmode, win32con.CDS_UPDATEREGISTRY)
        if result == win32con.DISP_CHANGE_SUCCESSFUL:
            print("Разрешение успешно изменено.")
            logger.log("info", "Разрешение успешно изменено", "set_resolution")
        else:
            print(f"Ошибка изменения разрешения. Код: {result}")
            logger.log("error", f"Ошибка изменения разрешения. Код: {result}", "set_resolution")
    except Exception as e:
        logger.log("error", f"Исключение при смене разрешения: {e}", "set_resolution")
        raise

def set_scaling_100():
    print("Установка масштаба 100%...")
    logger.log("info", "Установка масштаба 100%", "set_scaling_100")
    
    try:
        registry_path = r"Control Panel\Desktop"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_SET_VALUE)
        
        winreg.SetValueEx(key, "LogPixels", 0, winreg.REG_DWORD, 96) # 96 DPI = 100% масштаба
        winreg.CloseKey(key)
        
        win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, "LogPixels")
        
        print("Параметры масштаба записаны.")
        logger.log("info", "Параметры масштаба успешно записаны", "set_scaling_100")
    except Exception as e:
        print(f"Ошибка при смене масштаба: {e}")
        logger.log("error", f"Ошибка при смене масштаба: {e}", "set_scaling_100")

if __name__ == "__main__":
    logger.log("info", "Запуск подготовки винды", "main")
    
    set_scaling_100()
    set_resolution(1366, 768)