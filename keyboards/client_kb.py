from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button1 = KeyboardButton('/Время_работы')
button2 = KeyboardButton('/Адрес')
button3 = KeyboardButton('/Меню')
# button4 = KeyboardButton('Отправить номер', request_contact=True)
# button5 = KeyboardButton('Отправить геопозицию', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.row(button1, button2, button3)#.row(button4, button5)
