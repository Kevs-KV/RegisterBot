import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from handlers.users.register import register_users
from keyboards.inline.languages_callback import languages_markup, languages_markup_update, start_markup_register
from loader import dp, bot, _
from middlewares.language_moddleware import get_lang
from states.registerstate import RegisterUsers
from utils.db_api import quick_commands as db
from utils.db_api.quick_commands import add_user


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    chat_id = message.from_user.id
    name = message.from_user.full_name
    user_id = message.from_user.id
    user = await get_lang(user_id)
    if not user:
        await add_user(fullname_tg=message.from_user.full_name, id=message.from_user.id)
        await message.answer(_('Пришли мне язык для продолжения', reply_markup=languages_markup_update))
    await message.answer(_( f'Привет, {name}'))
    await message.answer(_( f'У нас запланировано мероприятие,\n'
                            f'Желаете зарегистрироваться?\n'))
    await message.answer('Желаете зарегистрироваться?', reply_markup=start_markup_register)

@dp.callback_query_handler(text_contains="startregister")
async def call_start_register(call: CallbackQuery):
    await call.message.answer(_('Начнем регистрацию'))
    await call.message.answer(_('Пришли свое имя'))
    await RegisterUsers.name.set()

