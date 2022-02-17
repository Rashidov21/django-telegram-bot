from aiogram import types
from . bot import dsp
from .keyboards import inline_kb


@dsp.message_handler(commands=["random"])
async def random_train(message:types.Message):
    await message.reply("random", reply_markup=inline_kb)