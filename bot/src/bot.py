from local_settings import API_KEY
from aiogram import Bot,Dispatcher,executor

bot = Bot(token=API_KEY)
dp = Dispatcher(bot)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)