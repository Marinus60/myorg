from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import asyncio

loop = asyncio.get_event_loop()

bot=Bot(token='5308280606:AAFFASHke-43AEvvV9vB6w-6AslnD8auSVI')
dp=Dispatcher(bot, loop=loop)
