import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor

TOKEN = 'TOKEN_PUT_HERE'
FILE_PATH = 'FILE_TO_DROP'
SECRET_CODE = 'YOUR_SECRET_PHRASE'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: Message):
    await message.answer("Hello get secret-phrase to drop file!")


@dp.message_handler(content_types=types.ContentType.TEXT)
async def send_file(message: Message):
    text = message.text
    chat_id = message.chat.id
    if text == SECRET_CODE:
        with open(FILE_PATH, 'rb') as f:
            await bot.send_document(chat_id, f)
    else:
        await message.answer("No valid phrase!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
