from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove



b1=KeyboardButton('Да')
b2=KeyboardButton('Нет')
b3=KeyboardButton('/Пункт3')
b4=KeyboardButton('/Пункт4')
b5=KeyboardButton('/Пункт5')


kb_client=ReplyKeyboardMarkup(resize_keyboard=True)
#kb_client.row(b1,b2,b3,b4,b5)
kb_client.add(b1).add(b2)

#row insert