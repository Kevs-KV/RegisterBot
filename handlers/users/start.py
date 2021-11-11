from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from keyboards.inline.languages_callback import languages_markup_start
from keyboards.inline.start_callback import start_register_callback
from loader import dp, _
from middlewares.language_moddleware import get_lang
from states.registerstate import RegisterUsers
from utils.db_api.quick_commands import add_user, set_status_register


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id
    lang = await get_lang(user_id)
    if not lang:
        await add_user(fullname_tg=message.from_user.full_name, id=message.from_user.id)
        await message.answer(_('Пришли мне язык для продолжения(Send me a tongue to continue)'),
                             reply_markup=languages_markup_start)
    else:
        user_status_register = await set_status_register(user_id)
        if not user_status_register or user_status_register is None:
            start_markup = await start_register_callback()
            await message.answer(_('Привет'))
            await message.answer(_('У нас запланировано мероприятие'))
            await message.answer(_('Желаете зарегистрироваться?'), reply_markup=start_markup)
        else:
            await message.answer(_('Вы уже зарегестрированы'))


async def continue_start_register_callback(message, language):
    await message.answer(_(f'Привет', locale=language))
    start_markup = await start_register_callback()
    await message.answer(_(f'У нас запланировано мероприятие', locale=language))
    await message.answer(_('Желаете зарегистрироваться?', locale=language), reply_markup=start_markup)


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
