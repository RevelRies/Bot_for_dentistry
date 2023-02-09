import logging
import config
import asyncio

from datetime import datetime
from typing import Optional
from aiogram import Bot, Dispatcher, types
from magic_filter import F
from aiogram.filters import Command, Text
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


bot = Bot(token=config.bot_token)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

dict_counter = dict()

fake_db = {'doctors': {'Иванов И.И.':
                {'full_name': 'Иванов Иван Иванович',
                'profession': 'Ортодонт',
                'experience': '5 лет',
                'raiting': '4.8'},

                       'Петров П.П.':
               {'full_name': 'Петров Петр Петрович',
                'profession': 'Терапевт',
                'experience': '2 года',
                'raiting': '4.6'},

                        'Сидоров С.С.':
               {'full_name': 'Сидоров Сидор Сидорович',
                'profession': 'Терапевт',
                'experience': '2 года',
                'raiting': '4.6'},

                        'Ященко П.И.':
               {'full_name': 'Ященко Петр Иванович',
                'profession': 'Терапевт',
                'experience': '2 года',
                'raiting': '4.6'},

                        'Азизов А.М.':
               {'full_name': 'Азизов Азад Мудрагимович',
                'profession': 'Терапевт',
                'experience': '2 года',
                'raiting': '4.6'}
                       }



           }

@dp.message(Command(commands=['start']))
async def main_menu(message: Message):
    buttuns = [
                  [KeyboardButton(text='Информация о клинике'),
                  KeyboardButton(text='Записаться на прием'),],

                  [KeyboardButton(text='Наши врачи'),
                  KeyboardButton(text='Мои записи')]

    ]

    murkup = ReplyKeyboardMarkup(keyboard=buttuns, resize_keyboard=True)
    await message.answer(text='Главное меню', reply_markup=murkup)


# функция обработки сообщения "Главное меню" для вывода главного меню
@dp.message(Text(text='Главное меню'))
async def get_main_menu(message: Message):
    await main_menu(message)


# функция вывода кнопки "Главное меню"
async def main_menu_markup():
    button = [[KeyboardButton(text='Главное меню')]]
    markup = ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)

    return markup


# вывод простым сообщением информации о клинике
@dp.message(Text(text='Информация о клинике'))
async def get_dentistry_info(message: Message):

    text = 'Тут будет выводиться информация о клинике\n' \
           '-----------------------------------------\n' \
           '-----------------------------------------\n' \
           '-----------------------------------------\n' \
           '-----------------------------------------\n' \
           '-----------------------------------------\n' \
           'Конец'

    await message.answer(text=text, reply_markup=await main_menu_markup())


# класс для инлайн кнопок врачей
class DoctorsCallback(CallbackData, prefix='doctors'):
    action: str
    doctor: str


# инлайн разметка для врачей
async def get_doctors_markup():
    builder = InlineKeyboardBuilder()

    for doc in fake_db['doctors']:
        builder.button(text=doc, callback_data=DoctorsCallback(action='appointment', doctor=doc))

    builder.adjust(1)

    return builder.as_markup()


# выаод врачей клиники
@dp.message(Text(text='Наши врачи'))
async def get_doctors(message: Message):
    text = text = 'Выберите врача⬇️'
    await message.answer(text=text, reply_markup=await get_doctors_markup())


# обработка callback запросов с просмотром информации о враче
@dp.callback_query(DoctorsCallback.filter(F.action == 'appointment'))
async def get_doctor_info(callback: CallbackQuery, callback_data: DoctorsCallback):
    dict_doc = fake_db['doctors'][callback_data.doctor]

    text = f'Доктор {dict_doc["full_name"]}\n' \
           f'Профессия: {dict_doc["profession"]}\n' \
           f'Стаж работы: {dict_doc["experience"]}\n' \
           f'Рейтинг: {dict_doc["raiting"]}'

    # разметка
    builder = InlineKeyboardBuilder()

    builder.button(text='⬅️Назад', callback_data='back_to_doctors')
    builder.button(text='Записаться на прием', callback_data='test')

    # builder.adjust(2)
    # ----------

    await callback.message.edit_text(text=text, reply_markup=builder.as_markup())


# Вывод докторов при нажатии на кнопку "Назад"
@dp.callback_query(Text(text='back_to_doctors'))
async def get_doctors_again(callback: CallbackQuery):
    text = 'Выберите врача⬇️'
    await callback.message.edit_text(text=text, reply_markup=await get_doctors_markup())


async def main():
    await dp.start_polling(bot)


asyncio.run(main())