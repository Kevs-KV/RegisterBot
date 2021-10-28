from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterUsers(StatesGroup):
    name = State()
    username = State()
    email = State()
    location = State()
    phone = State()