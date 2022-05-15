from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import asyncio

loop = asyncio.get_event_loop()

bot=Bot(token='5378984818:AAH_P8iUyt1Wp_EsCN6XxGFQu_v5sFIkaFw')
dp=Dispatcher(bot, loop=loop)
