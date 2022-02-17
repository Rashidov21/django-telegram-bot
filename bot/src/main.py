from aiogram import executor
from bot_app.bot import dsp

if __name__ == '__main__':
    executor.start_polling(dsp, skip_updates=True)
else:
    pass