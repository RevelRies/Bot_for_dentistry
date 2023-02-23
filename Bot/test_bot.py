import config
import logging
import asyncio
import fsm_forms

from aiogram import Dispatcher, Bot
from aiogram.filters import Command, Text
from aiogram.types import Message
from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder, ReplyKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage




token = config.bot_token

storage = MemoryStorage()
dp = Dispatcher(storage=storage)
bot = Bot(token)

logging.basicConfig(level=logging.INFO)

# отработка команды /start
@dp.message(Command('start'))
async def start_commad(message: Message):
    builder = ReplyKeyboardBuilder()

    btn1 = KeyboardButton(text='Добавить пользователя')
    btn2 = KeyboardButton(text='Вторая кнопка')
    btn3 = KeyboardButton(text='Третья кнопка')

    builder.add(btn1, btn2, btn3)
    builder.adjust(1)
    markup = builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

    await message.answer(text='Приветственное сообщение', reply_markup=markup)


@dp.message(Text(text='Добавить пользователя'))
async def add_user(message: Message):
    text = 'Введите имя пользователя'

    await message.answer(text=text)























async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
