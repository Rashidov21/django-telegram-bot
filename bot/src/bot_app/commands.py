from aiogram import types
from .bot import dsp
from . import messages

@dsp.message_handler(commands=['start'])
async def send_welcome(message : types.Message):
    await message.reply(messages.WELCOME_MSG)