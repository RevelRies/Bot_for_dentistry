from aiogram.fsm.state import StatesGroup, State

class User(StatesGroup):
    name = State()
    age = State()