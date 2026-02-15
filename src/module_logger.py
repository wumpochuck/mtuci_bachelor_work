import logging
import os
import datetime

class CSVLogger:
    def __init__(self, filename="activity_log.csv"):
        self.filename = filename
        self._prepare_file()
        
        self.logger = logging.getLogger("UserSimulator")
        self.logger.setLevel(logging.DEBUG)
        
        if self.logger.hasHandlers():
            self.logger.handlers.clear()
        
        handler = logging.FileHandler(self.filename, encoding='utf-8')
        
        formatter = logging.Formatter(
            fmt='%(asctime)s;%(levelname)s;%(message)s',
            datefmt='%Y-%m-%dT%H:%M:%S'
        )
        
        formatter.default_msec_format = '%s.%03d'
        
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def _prepare_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write("timestamp;level;message;context\n")

    def log(self, level, message, context="None"):
        clean_message = str(message).replace(';', ',')
        clean_context = str(context).replace(';', ',')
        
        full_msg = f"{clean_message};{clean_context}"
        
        if level.lower() == "info":
            self.logger.info(full_msg)
        elif level.lower() == "error":
            self.logger.error(full_msg)
        elif level.lower() == "debug":
            self.logger.debug(full_msg)

if __name__ == "__main__":
    logger = CSVLogger()
    logger.log("info", "Запуск имитатора", "Система инициализирована")
    logger.log("debug", "Поиск иконки Word", "Координаты не найдены, пробую Win+R")
    logger.log("error", "Не удалось открыть файл", "C:\\Docs\\report.docx")
    print(f"Логирование завершено. Проверьте файл {os.path.abspath('activity_log.csv')}")