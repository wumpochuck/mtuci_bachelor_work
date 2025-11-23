from custom_functions import *

# Пример создания Word документа на рабочем столе
def create_word_doc_on_desktop():
    # Внутренняя часть функции может отличаться в зависимости от ОС
    # (Там где писалось это, Windows настроена под личное пользование)
    win_d()
    move_to(400, 400)
    click(button='right')
    press_key('up', presses=3, interval=0.3)
    press_key('enter')
    press_key('down', presses=4, interval=0.3)
    press_key('enter')
    sleep(0.5)
    type_text('Year report 2023', interval=0.1)
    press_key('enter')
    return (400, 400)  # Возвращаем координаты иконки документа

# Пример открытия созданного Word документа
def open_word_doc(coords):
    move_to(coords[0] + 5, coords[1] + 5, duration=1)
    click()
    sleep(1)
    press_key('enter')

def type_text_in_word(text):
    type_text(text, interval=0.05)

# Основной сценарий
word_coords = create_word_doc_on_desktop()
move_to(1200, 800, duration=1)
open_word_doc(word_coords)
sleep(5)
type_text_in_word("Privet, eto testovyy dokument dlya proverki avtomatizatsii sozdaniya i otkrytiya faylov v Windows.")
ctrl_s()
alt_f4()


