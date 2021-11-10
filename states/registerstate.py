from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterUsers(StatesGroup):
    name = State()
    username = State()
    country = State()
    city = State()
    age = State()
    email = State()
    phone = State()
