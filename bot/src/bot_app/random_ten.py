from aiogram import types
from aiogram.dispatcher import FSMContext
from . bot import dsp
from . states import GameStates
from .keyboards import inline_kb
from .data_fetcher import get_random


@dsp.message_handler(commands=["random"], state='*')
async def random_train(message : types.Message,state : FSMContext):
    await GameStates.random_ten.set()
    res = await get_random()
    async with state.proxy() as data:
        data["step"] = 1
        data["answer"] = res.get("gender")
        data["word"] = res.get("word")
        await message.reply(f"{data['step']} of 10. This is word = {data['word']}", reply_markup=inline_kb)