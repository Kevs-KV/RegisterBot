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
from utils.db_api.quick_commands import get_user, add_user, register_user_db
from validations.validations_state import validations_phone


@dp.message_handler(Command('register'))
async def register_users(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user = await get_lang(user_id)
    print(user)
    if not user:
        await add_user(fullname_tg=message.from_user.full_name, id=message.from_user.id)
        await message.answer('Пришли мне язык', reply_markup=languages_markup)
    else:
        await message.answer(_('Начнем регистрацию'))
        await message.answer(_('Пришли свое имя'))
        await RegisterUsers.name.set()


@dp.message_handler(state=RegisterUsers.name)
async def register_name_user(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data(name=name)
    await message.answer(_('Пришли свою фамилию'))
    await RegisterUsers.username.set()


@dp.message_handler(state=RegisterUsers.username)
async def register_username_user(message: types.Message, state: FSMContext):
    username = message.text
    await state.update_data(username=username)
    await message.answer(_('Пришли свой email'))
    await RegisterUsers.email.set()


@dp.message_handler(state=RegisterUsers.email)
async def register_email_user(message: types.Message, state: FSMContext):
    email = message.text
    await state.update_data(email=email)
    await message.answer(_('Пришли свой номер телефона'))
    await RegisterUsers.phone.set()


@dp.message_handler(state=RegisterUsers.phone)
async def register_phone_user(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    text = message.text
    phone = await validations_phone(user_id, phone=text)
    print(phone)
    if phone != None:
        await state.update_data(phone=phone)
        result = await state.get_data()
        name = result.get('name')
        username = result.get('username')
        email = result.get('email')
        phone = result.get('phone')
        await register_user_db(name, username, email, phone)
        await message.answer(_('Регистрация завершена'))
        await state.finish()
    else:
        await message.answer(_('Номер не валидный'))
        await message.answer(_('Пришлите номер заново'))
        await RegisterUsers.phone.set()




