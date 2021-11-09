
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.inline.languages_callback import start_markup_register, languages_markup_start
from loader import dp, _
from middlewares.language_moddleware import get_lang
from states.registerstate import RegisterUsers
from utils.db_api.quick_commands import add_user


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    lang = await get_lang(user_id)
    if not lang:
        await add_user(fullname_tg=message.from_user.full_name, id=message.from_user.id)
        await message.answer(_('Пришли мне язык для продолжения(Send me a tongue to continue)'), reply_markup=languages_markup_start)
    else:
        await message.answer(_('Привет'))
        await message.answer(_('У нас запланировано мероприятие'))
        await message.answer(_('Желаете зарегистрироваться?'), reply_markup=start_markup_register)





@dp.callback_query_handler(text_contains="startregister")
async def call_start_register(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer(_('Начнем регистрацию'), reply_markup=ReplyKeyboardRemove())
    await call.message.answer(_('Пришли свое имя'), )
    await RegisterUsers.name.set()


@dp.callback_query_handler(text_contains="noregister")
async def call_cancel_register(call: CallbackQuery):
    await call.message.edit_reply_markup()
    await call.message.answer(_('Хорошего дня'))


