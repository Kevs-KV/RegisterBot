from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from aiogram.types import ReplyKeyboardRemove

from keyboards.default.cancel_button import cancel_register_markup
from keyboards.inline.languages_callback import languages_markup_update
from loader import dp, _
from states.registerstate import RegisterUsers
from utils.db_api import quick_commands as db


@dp.message_handler(Command('update_language'))
async def update_language(message: types.Message):
    await message.answer(_('Выберите язык для обновления'), reply_markup=languages_markup_update)


@dp.callback_query_handler(text_contains="lang")
async def change_language(call: CallbackQuery):
    await call.message.edit_reply_markup()
    command_update = call.data.split('_')
    language = command_update[-1]
    await db.set_language(language)
    await call.message.answer(_("Язык был установлен(Language set)"))
    await call.message.answer(_("Обновить язык(Update language) - /update_language"))
    if command_update[0] == 'start':
        await call.message.answer('/register - для прохождения регистрации(for registration)',
                                  reply_markup=ReplyKeyboardRemove())
    if command_update[0] == 'lang':
        await call.message.answer(_('Пришли свое имя(Send your name)'), reply_markup=cancel_register_markup)
        await RegisterUsers.name.set()
