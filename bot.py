import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5353577061:AAF8C8kqR8QIkxdM-lcvJMT80-dY-7WBARo'
wikipedia.set_lang('uz')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await message.reply("Hi\nI'm echobot\nPowered by aiogram.")

    @dp.message_handler()
    async def wiki(message: types.Message):
        try:
            respond = wikipedia.summary(message.text)
            await message.answer(respond)
        except:
            await message.answer('Bu mavzuga oid maqolalar topilmadi.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
