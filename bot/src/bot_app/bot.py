from .local_settings import API_KEY
from aiogram import Bot, Dispatcher

bot = Bot(token=API_KEY)
dsp = Dispatcher(bot)

