import config
import crud

import logging
import asyncio

from fsm_forms import User

from aiogram import Dispatcher, Bot
from aiogram.filters import Command, Text
from aiogram.types import Message
from aiogram.utils.keyboard import KeyboardButton, ReplyKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage




token = config.bot_token

storage = MemoryStorage()
dp = Dispatcher(storage=storage)
bot = Bot(token)

logging.basicConfig(level=logging.INFO)

def get_main_keyboard():
    builder = ReplyKeyboardBuilder()

    btn1 = KeyboardButton(text='Добавить пользователя')
    btn2 = KeyboardButton(text='Все пользователи')
    btn3 = KeyboardButton(text='Третья кнопка')

    builder.add(btn1, btn2, btn3)
    builder.adjust(1)
    markup = builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

    return markup

# отработка команды /start
@dp.message(Command('start'))
async def start_commad(message: Message):
    markup = get_main_keyboard()
    await message.answer(text='Приветственное сообщение', reply_markup=markup)


# при нажатии на кнопку "Добавить пользователя" переводим в состояние для ввода имени
# --------------------------------------------------------------------------------------------------------------------
@dp.message(Text(text='Добавить пользователя'))
async def add_user(message: Message, state: FSMContext):
    await state.set_state(User.name)

    text = 'Введите имя пользователя'
    await message.answer(text=text)


@dp.message(User.name)
async def get_name(message: Message, state: FSMContext):
    name = message.text
    if not name.isalpha():
        await message.answer(text='Имя должно содержать только буквы')
    else:
        await state.update_data(name=name)
        await state.set_state(User.age)

        text = f'Отлично {name}, теперь введите свой возраст'
        await message.answer(text=text)


@dp.message(User.age)
async def get_age(message: Message, state: FSMContext):
    age = message.text
    markup = get_main_keyboard()
    
    if not age.isdigit():
        await message.answer(text='Возраст должен содержать только цифры')
    else:
        await state.update_data(age=age)
        dt = await state.get_data()
        name = dt['name']
        text = f'Отлично {name}, вы зарегестрированны\n' \
               f'Ваш возраст: {age}'

        await state.clear()
        await message.answer(text=text, reply_markup=markup)
# --------------------------------------------------------------------------------------------------------------------

@dp.message(Text(text='Все пользователи'))
async def get_all_users(message: Message):
    dict_users = crud.get_all_users()

    await message.answer(text=str(dict_users))




















async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
