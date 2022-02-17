from aiogram import types
from aiogram.dispatcher import FSMContext
from . bot import dsp,bot
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

@dsp.callback_query_handler(lambda c:c.data in ["das","die","der"])
async def button_click_callback(callback_query : types.CallbackQuery, state : GameStates.random_ten):
    await bot.answer_callback_query(callback_query.id)
    answer = callback_query.data
    async with state.proxy() as data:
        if answer.data == data.get("answer"):
            res = await get_random()
            data["step"] += 1
            data["answer"] = res.get("gender")
            data["word"] = res.get("word")
            if data["step"] > 10:
                await bot.send_message(callback_query.from_user.id, "Game over !")
                await GameStates.start.set()
            else:
                await bot.send_message(
                    callback_query.from_user.id ,
                    f"YES ! \n {data['step']} of 10. This is word = {data['word']}",
                    reply_markup=inline_kb
                    )
        else:
            await bot.send_message(
                callback_query.from_user.id,
                f"No !",
                reply_markup=inline_kb
                )