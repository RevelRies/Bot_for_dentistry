import logging
import config
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

bot = Bot(token=config.bot_token)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)


@dp.message(Command(commands=['start']))
async def hello(message: types.Message):
    await message.answer(text='test "hello" func')


@dp.message()
async def echo(message: types.Message):
    await message.answer(text=message.text)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())