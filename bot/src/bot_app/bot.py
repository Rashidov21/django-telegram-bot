from .local_settings import API_KEY
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token=API_KEY)
dsp = Dispatcher(bot, storage=MemoryStorage())

