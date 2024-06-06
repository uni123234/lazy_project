
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'your_token'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hello, I'm your bot!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
