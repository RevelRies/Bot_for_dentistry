import logging
import config
import asyncio

from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, Text
from aiogram.types import Message, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

bot = Bot(token=config.bot_token)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

dict_counter = dict()


@dp.message(Command(commands=['start']))
async def main_menu(message: Message):
    buttuns = [
                  [KeyboardButton(text='Информация о клинике'),
                  KeyboardButton(text='Записаться на прием'),],

                  [KeyboardButton(text='Наши врачи'),
                  KeyboardButton(text='Мои записи')],

                  [KeyboardButton(text='Кнопка для тестов')]

    ]

    murkup = ReplyKeyboardMarkup(keyboard=buttuns, resize_keyboard=True, one_time_keyboard=True)
    await message.answer(text='Главное меню', reply_markup=murkup)

# создает и возвращает клавиатуру
async def keyboard():
    btn1 = InlineKeyboardButton(text='-1', callback_data='num_-')
    btn2 = InlineKeyboardButton(text='+1', callback_data='num_+')
    btn3 = InlineKeyboardButton(text='Подтвердить', callback_data='num_finish')

    murkup = InlineKeyboardMarkup(inline_keyboard=[[btn1, btn2], [btn3]])


    return murkup


@dp.message(Text(text='Кнопка для тестов'))
async def counter(message: Message):

    await message.answer(text=f'У меня {dict_counter.setdefault(message.from_user.id, 0)} задолженностей',
                         reply_markup=await keyboard())


@dp.callback_query(Text(startswith='num_'))
async def callback_hand(callback: CallbackQuery):
    command = callback.data.split('_')[-1]

    if command == '-':
        dict_counter[callback.from_user.id] -= 1
    if command == '+':
        dict_counter[callback.from_user.id] += 1
    if command == 'finish':
        await callback.answer(text='Нажата кнопка "Подтвердить"', show_alert=True)



async def main():
    await dp.start_polling(bot)


asyncio.run(main())