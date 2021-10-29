import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery

from keyboards.inline import languages_callback
from keyboards.inline.languages_callback import languages_markup
from loader import dp, _
from middlewares.language_moddleware import get_lang
from states.registerstate import RegisterUsers
from utils.db_api import quick_commands as db
from utils.db_api.commands_admin import all_register_users
from utils.db_api.quick_commands import get_user, add_user, register_user_db, select_all_users


@dp.message_handler(Command('all_register_users'))
async def get_all_register_users(message: types.Message):
    users = await all_register_users()
    await message.answer(f'{users}')