# from aiogram.utils import executor
# from create_bot import dp
# import client, admin, other,voice_in_text
# from voice_in_text import voice_recognizer
#
# async def on_startup(_):
#     print("Бот вышел в онлайн!")
#
# #   Функция распознования речи
# #voice_recognizer(dp)
#
#
# voice_in_text.register_handlers_voice_in_text(dp)
#
# #client.register_handlers_client(dp)
# #other.register_handlers_other(dp)
# # admin.register_handlers_admin(dp)
#
# #executor.start_polling(dp)
#
# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)
#     #executor.start_polling(dp)

import logging

from aiogram import Bot, Dispatcher, executor, types
from create_bot import dp, bot
import subprocess
import speech_recognition as sr

# Переменная с токеном
API_TOKEN = '5308280606:AAFFASHke-43AEvvV9vB6w-6AslnD8auSVI'

# Конфигурация логов
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Хэндлер для принятия сообщений /start и /help
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    # Была сделана отдельная функция которая сразу отвечает на сообщение пользователя
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


# Хэндлер для принятия остальных сообщений
@dp.message_handler()
async def echo(message: types.Message):
    # Отправляем сообщение обратно
    await bot.send_message(message.chat.id, message.text)

@dp.message_handler(content_types=['voice'])
async def voice_recognizer(message: types.Message): #Функция распознования речи
    r = sr.Recognizer()
    file_id = message.voice.file_id
    newFile = await bot.get_file(file_id)
    await newFile.download(f'voice.ogg')
    # ###Конвертация файла###
    src_filename = f'voice.ogg'
    dest_filename = 'voice.wav'
    process = subprocess.run([f'ffmpeg', '-i', src_filename, dest_filename, '-y'])
    # ###Распознование слов###
  #  try:
    user_audio_file = sr.AudioFile(dest_filename)
    with user_audio_file as source:
        user_audio = r.record(source)
    text = r.recognize_google(user_audio, language='ru-RU')

        #await bot.send_message(message.from_user.id, text)
        #return text
    print(text)

    # except:
    #    await message.reply('Моя твоя не понимает, повтори!')



if __name__ == '__main__':
    # Начинаем получать сообщения и все события
    executor.start_polling(dp, skip_updates=True)